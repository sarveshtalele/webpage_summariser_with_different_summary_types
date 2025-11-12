import streamlit as st
import validators
from langchain_groq import ChatGroq
from langchain_classic.chains.summarize import load_summarize_chain
from langchain_community.document_loaders import UnstructuredURLLoader, PlaywrightURLLoader

# --- Streamlit App Configuration ---
st.set_page_config(page_title="Web Page Summarizer", page_icon="📝")

st.title("📝 Web Page Summarizer")
st.caption("Summarize any web page using different LangChain methods.")

# --- Sidebar for API Key ---
with st.sidebar:
    st.header("Configuration")
    groq_api_key = st.text_input("Groq API Key", type="password", placeholder="Enter your key here")
    st.markdown("[Get your Groq API Key](https://console.groq.com/keys)")

# --- Main App Interface ---
url = st.text_input("Enter the URL of the web page to summarize:", label_visibility="visible")

chain_type = st.selectbox(
    "Choose a summarization method:",
    ("Stuff", "map_reduce", "Refine"),
    help="""
    - **Stuff**: Fastest, but only works for smaller articles.
    - **Map_Reduce**: Best for very large articles, processes chunks in parallel.
    - **Refine**: Iteratively builds a detailed summary, good for coherent narratives.
    """
)

if st.button("Summarize"):
    # --- Input Validation ---
    if not groq_api_key:
        st.error("Please enter your Groq API Key in the sidebar.")
    elif not url:
        st.error("Please enter a URL to summarize.")
    elif not validators.url(url):
        st.error("Please enter a valid URL.")
    else:
        try:
            with st.spinner("Loading page content and summarizing... Please wait."):
                
                # --- Initialize LLM ---
                llm = ChatGroq(model="llama-3.1-8b-instant", groq_api_key=groq_api_key, temperature=0)

                # --- Load Content (with fallback) ---
                docs = None
                try:
                    # Try the faster loader first
                    loader = UnstructuredURLLoader(urls=[url], ssl_verify=False)
                    docs = loader.load()
                except Exception:
                    # Fallback to the more robust browser-based loader
                    st.toast("Simple loader failed, trying robust loader (Playwright)...")
                    loader = PlaywrightURLLoader(urls=[url], remove_selectors=["header", "footer"])
                    docs = loader.load()

                # --- Verify Content was Loaded ---
                if not docs or not docs[0].page_content.strip():
                    st.error("Failed to load content from the URL. The page might be empty or protected.")
                else:
                    # --- Create and Run Summarization Chain ---
                    # The chain type string must be lowercase for load_summarize_chain
                    summarize_chain = load_summarize_chain(
                        llm=llm,
                        chain_type=chain_type.lower(), # "Stuff" -> "stuff"
                        verbose=False # Set to True in console for debugging
                    )
                    
                    summary = summarize_chain.run(docs)

                    # --- Display Result ---
                    st.success("Summary Generated!")
                    st.subheader(f"Summary ({chain_type} Method)")
                    st.markdown(summary)

        except Exception as e:
            st.exception(f"An unexpected error occurred: {e}")