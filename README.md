# 🧠 Local AI Chatbot (No-Cost Setup)

Build your own AI chatbot that answers questions using scraped web content — powered by local language models via Ollama and Mistral.

✅ Runs completely offline  
✅ Uses your own website or any public webpage as knowledge  
✅ No paid APIs required

---

## 📦 Features

- Scrape any webpage's content
- Generate semantic embeddings with `sentence-transformers`
- Perform vector search with `FAISS`
- Answer questions using `Mistral` LLM via [Ollama](https://ollama.com/)
- Chat interface powered by `Streamlit`

---

## 🚀 Quick Start

### 1. **Clone the Project**
```bash
git clone https://github.com/hitk95/chat-bot.git
cd chat-bot

---

### 2. **Install Dependencies**
```bash
pip install -r requirements.txt
```

---

### 3. **Install Ollama (Run Local AI Models)**

#### On macOS/Linux:
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

#### On Windows:
- Download installer from [https://ollama.com/download](https://ollama.com/download)
- OR use command curl -fsSL https://ollama.com/install.sh | sh (On Linux)
- Then run in terminal:
```bash
ollama run mistral
```

---

### 4. **Scrape a Web Page**

Use this command to scrape and index the content of a web page:

```bash
python app/scraper.py
```

🔤 When prompted, enter a full URL (e.g., `https://en.wikipedia.org/wiki/Canada`)  
📁 This creates:
- `data/chunks.pkl` (text chunks)
- `data/index.faiss` (vector index)

## FOR NOW CANADA WIKI PAGE IS ALREADY SCRAPPED AND AVAILABLE IN THE REPOSITORY STRUCTURE

---

### 5. **Start the Chatbot**

```bash
streamlit run app/chatbot.py
```

Then open the link shown in your terminal (usually `http://localhost:8501`) in your browser.

---

## 🧠 How It Works

1. Scrapes the page into readable text
2. Splits the text into chunks and embeds them using `sentence-transformers`
3. Builds a vector index with `FAISS`
4. Searches relevant chunks for your question
5. Constructs a prompt and passes it to the Mistral model via `Ollama`
6. Returns a locally generated answer

---

## 🛠 Project Structure

```
local-ai-chatbot/
├── app/
│   ├── chatbot.py         # Streamlit app
│   ├── chatbot_core.py    # Search + Ollama logic
│   └── scraper.py         # Web scraper + indexer
├── data/                  # Stores chunks and FAISS index
├── models/                # (Optional) For future model logic
├── requirements.txt
└── README.md
```
