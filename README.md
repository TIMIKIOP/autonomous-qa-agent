# 🧠 Autonomous QA Agent for Test Case & Selenium Script Generation

This project is an **intelligent QA Automation Agent** that ingests project documents and HTML to generate:

✔ Documentation-grounded Test Cases  
✔ Executable Selenium Python Scripts  

The system uses:

- **FastAPI** backend  
- **Streamlit** frontend UI  
- **Vector Database (Chroma)** for knowledge retrieval  
- **Ollama LLM** for reasoning  
- **Support Documents + checkout.html** as the knowledge base  

---

## 🚀 Features

### **1. Knowledge Base Ingestion**
Upload:
- product_specs.md
- ui_ux_guide.txt
- api_endpoints.json
- checkout.html

System automatically:
- Extracts content  
- Chunks text  
- Generates embeddings  
- Stores vectors in Chroma DB  

---

### **2. Test Case Generation (RAG Agent)**

User types:
```
Generate all positive and negative test cases for the checkout page.
```

The agent:
- Retrieves relevant chunks  
- Synthesizes grounded test cases  
- Ensures NO hallucinations  
- Outputs JSON/Markdown test suite  

---

### **3. Selenium Script Generation**

User selects one test case → clicks **Generate Selenium Script**.

Agent:
- Reads checkout.html  
- Extracts correct selectors  
- Produces clean Selenium Python code using:
  - Chrome WebDriver
  - Explicit waits
  - Correct IDs/names/css selectors  

---

# 📂 Project Structure

```
QA_AGENT/
│
├── assets/
│   ├── checkout.html
│   ├── product_specs.md
│   ├── ui_ux_guide.txt
│   └── api_endpoints.json
│
├── backend/
│   ├── main.py
│   ├── test_case_agent.py
│   ├── selenium_agent.py
│   └── vector_store.py
│
├── frontend/
│   └── app.py
│
├── README.md
└── venv/
```

---

# ⚙️ Installation & Setup

### **1. Clone the Repository**
```
git clone https://github.com/<your-username>/<your-repo>.git
cd QA_AGENT
```

### **2. Create Virtual Environment**
```
python -m venv venv
venv\Scripts\activate  (Windows)
```

### **3. Install Dependencies**
```
pip install -r requirements.txt
```

---

# ▶️ Running the Project

### **Start FastAPI Backend**
```
uvicorn backend.main:app --reload
```

### **Start Streamlit Frontend**
```
streamlit run frontend/app.py
```

Both must run simultaneously.

Backend default URL:
```
http://127.0.0.1:8000
```

Frontend default URL:
```
http://localhost:8501
```

---

# 🧪 Usage Demo

### **Step 1 — Upload Documents**
- Upload MD, TXT, JSON
- Upload checkout.html

### **Step 2 — Build Knowledge Base**
System extracts → chunks → embeds → stores vectors.

### **Step 3 — Generate Test Cases**
Example Query:
```
Generate positive and negative test cases for the discount code feature.
```

### **Step 4 — Select Any Test Case**

### **Step 5 — Generate Selenium Script**
System outputs a full, runnable Python script.

---

# 📁 Included Support Documents

| File | Purpose |
|------|---------|
| product_specs.md | Business rules (discounts, shipping, item rules) |
| ui_ux_guide.txt | UI rules (button colors, error text) |
| api_endpoints.json | Mock backend API structure |
| checkout.html | Full front-end structure for selector extraction |

---

# 📹 Demo Video Requirements (5–10 min)

Your submission MUST include a video.  
Checklist:

✔ Upload docs  
✔ Upload HTML  
✔ Build KB  
✔ Generate test cases  
✔ Select a test case  
✔ Generate Selenium script  
✔ Run script (optional but good)  

---

# 🧩 Technologies Used

- Python  
- FastAPI  
- Streamlit  
- ChromaDB  
- LangChain  
- Selenium  
- Ollama LLM  
- HTML Parsing  
- Embedding models  

---

# 🧑‍💻 Author
**Utkarsh Thori**

---

# ✔ Assignment Checklist (All Completed)

- [x] Document ingestion  
- [x] Vector embeddings  
- [x] RAG-based test case generation  
- [x] Selenium script generation  
- [x] Streamlit UI  
- [x] FastAPI backend  
- [x] README  
- [x] Demo-ready  

---

# 🎉 You're Done!
This repository is complete and meets all requirements for the Autonomous QA Agent assignment.

