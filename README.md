# 📰 AI Article Summarizer

An AI-powered tool that extracts the content of any online article and generates a concise summary using **Google Gemini**.
The project combines **article extraction via RapidAPI** with **LLM summarization** and provides an interactive **Streamlit UI** for easy usage.

---

# 🚀 Features

* 🔗 Extract content from any article URL
* 🤖 Summarize articles using **Gemini 2.5 Flash**
* 🖥️ Interactive **Streamlit UI**
* 🔐 Secure API key handling with **.env**
* ⚡ Fast article parsing via **RapidAPI Article Extractor**

---

# 🏗️ Project Architecture

User enters article URL in Streamlit UI

↓

Article Extractor API (RapidAPI)

↓

Extract article content

↓

Send content to Gemini API

↓

Generate summary

↓

Display summary in UI

---

# 📂 Project Structure

```
article_summarizer/
│
├── app.py              # Streamlit UI
├── main.py             # Gemini summarization logic
├── test.py             # Article extraction via RapidAPI
├── .env                # API keys (not committed)
├── requirements.txt    # Project dependencies
└── README.md
```

---

# ⚙️ Installation

### 1️⃣ Clone the Repository

```
git clone https://github.com/yourusername/article-summarizer.git
cd article-summarizer
```

---

### 2️⃣ Create Virtual Environment

```
python -m venv venv
```

Activate it

**Windows**

```
venv\Scripts\activate
```

**Mac/Linux**

```
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file in the root directory.

```
RAPID_API_KEY=your_rapidapi_key
GEMINI_API_KEY=your_gemini_api_key
```

### Get API Keys

**RapidAPI Article Extractor**
https://rapidapi.com

**Google Gemini API**
https://ai.google.dev/

---

# ▶️ Run the Application

Run the Streamlit UI:

```
streamlit run app.py
```

Open the browser:

```
http://localhost:8501
```

---

# 🖥️ Application UI

1. Enter an **article URL**
2. Click **Generate Summary**
3. The application will:

   * Extract the article
   * Send it to Gemini
   * Display the summarized content

---

# 📦 Requirements

```
requests
python-dotenv
google-genai
streamlit
```

---

# 🔧 How It Works

### Article Extraction

`test.py` calls the **RapidAPI Article Extractor** to fetch structured article data.

Important fields returned:

* title
* author
* published date
* content (HTML)

---

### Summarization

`main.py` sends the article content to **Gemini 2.5 Flash** using the `google-genai` SDK.

Gemini processes the text and returns a concise summary.

---

### User Interface

`app.py` provides a simple **Streamlit interface** where users can:

* input an article URL
* trigger summarization
* view the results instantly

---

# ⚡ Future Improvements

* Clean HTML using **BeautifulSoup**
* Add **summary length control**
* Add **download summary button**
* Add **article preview**
* Convert backend to **FastAPI**
* Containerize with **Docker**
* Deploy on **Streamlit Cloud**

---

# 🧠 Tech Stack

* Python
* Streamlit
* Google Gemini API
* RapidAPI
* Requests
* dotenv

---

# 📜 License

This project is open-source and available under the **MIT License**.

---

# 👨‍💻 Author

Developed as a learning project for **LLM application development and API integration**.
