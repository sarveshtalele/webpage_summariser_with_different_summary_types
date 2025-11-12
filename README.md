# 🧠 Web Page Summarizer with LangChain & Groq

[![Watch the Video Walkthrough](https://img.shields.io/badge/▶️%20Watch%20Demo-Click%20Here-blue?style=for-the-badge)](https://github.com/your-username/your-repo-name/assets/your-video-id)


---

## ✨ Features

- **Summarize Any URL** – Paste any public web page link and get a concise summary instantly.  
- **Multiple Summarization Strategies** – Choose from three LangChain summarization methods based on article length and complexity:
  - 🧩 **Stuff** – Fastest method, best for short articles that fit within the LLM’s context window.  
  - 🧮 **Map Reduce** – Great for long-form content; breaks text into chunks, summarizes them, and merges results.  
  - 🧠 **Refine** – Iterative summarization that improves the summary step-by-step as it processes chunks.  
- ⚡ **High-Speed Inference** – Powered by Groq API for near-instant LLM responses.  
- 🧱 **Robust Content Loading** – Uses `UnstructuredURLLoader` first, and automatically falls back to `PlaywrightURLLoader` for JS-heavy websites.  
- 🔐 **Secure & User-Friendly** – Input your API key privately via the Streamlit sidebar with a clean, intuitive UI.

---

## ⚙️ How It Works

1. **Input:**  
   The user provides a web page URL, their **Groq API key**, and chooses a summarization strategy.

2. **Content Loading:**  
   LangChain document loaders attempt to fetch and parse the text from the provided URL.  
   - First, it uses `UnstructuredURLLoader` for speed.  
   - If that fails (e.g., due to JavaScript rendering), it falls back to `PlaywrightURLLoader`, which uses a headless browser.

3. **LLM Initialization:**  
   A `ChatGroq` instance is created with the user’s API key, configured to use the **llama-3.1-8b-instant** model.

4. **Summarization Chain:**  
   Depending on the selected mode (`stuff`, `map_reduce`, or `refine`), a `load_summarize_chain` is constructed.  
   This packages the text and sends it to the Groq API for summarization.

5. **Output:**  
   The summary is streamed back and displayed in real time via the Streamlit UI.

---

## 🚀 Setup and Installation

Follow these steps to run the app locally:

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```
## 2. Create a Virtual Environment

### On macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

Windows:

```
python -m venv venv
venv\Scripts\activate
```

## ▶️ Running the Application

### 1. Get Your Groq API Key

- Sign up for a free account at [GroqCloud](https://groq.com).  
- Go to **API Keys** and create a new secret key.

---

### 2. Launch the Streamlit App

Run the app with:

```bash
streamlit run app.py
```

## 🎥 Video Walkthrough

Click the badge at the top to watch a **complete walkthrough** of how the app works — from URL input to summary generation.

---

## 🧩 Contributing

Pull requests are welcome!  
If you’d like to add new summarization methods or improve the UI, feel free to fork and submit a PR.

---

**Built with ❤️ using Streamlit, LangChain, and Groq.**

