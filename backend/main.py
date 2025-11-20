from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import uvicorn
from test_case_agent import generate_test_cases
from selenium_agent import generate_selenium_script
from vector_store import VectorStore



app = FastAPI()

# CORS for Streamlit Frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Temporary storage
DOCUMENTS = []
HTML_CONTENT = ""
VECTOR_DB = None   # GLOBAL VECTOR DB ✔️

# -------------------------------
# Upload Support Documents
# -------------------------------
@app.post("/upload_docs/")
async def upload_docs(files: List[UploadFile]):
    global DOCUMENTS
    DOCUMENTS = []

    for file in files:
        text = (await file.read()).decode("utf-8", errors="ignore")
        DOCUMENTS.append({"filename": file.filename, "content": text})

    return {"message": "Documents uploaded", "count": len(DOCUMENTS)}


# -------------------------------
# Upload checkout.html
# -------------------------------
@app.post("/upload_html/")
async def upload_html(file: UploadFile):
    global HTML_CONTENT
    HTML_CONTENT = (await file.read()).decode("utf-8", errors="ignore")
    return {"message": "HTML uploaded"}


# -------------------------------
# Build Knowledge Base (Vector DB)
# -------------------------------
@app.post("/build_knowledge_base/")
def build_knowledge_base():
    global VECTOR_DB, DOCUMENTS, HTML_CONTENT

    if not DOCUMENTS and not HTML_CONTENT:
        return {
            "status": "error",
            "message": "No documents or HTML uploaded"
        }

    VECTOR_DB = VectorStore()

    # combine documents + html
    all_docs = DOCUMENTS.copy()
    if HTML_CONTENT:
        all_docs.append({"filename": "checkout.html", "content": HTML_CONTENT})

    # Add to vector DB
    VECTOR_DB.add_documents(all_docs)

    return {
        "status": "success",
        "message": "Knowledge Base Built!"
    }

@app.post("/generate_test_cases/")
def generate_tc(query: str):
    global VECTOR_DB

    if VECTOR_DB is None:
        return {"status": "error", "message": "Knowledge Base not built yet"}

    result = generate_test_cases(query, VECTOR_DB)

    return {
        "status": "success",
        "test_cases": result
    }

# -------------------------------
# Health Check
# -------------------------------
@app.get("/health")
def health():
    return {"status": "Backend Running OK"}


# -------------------------------
# Run For Local Development
# -------------------------------
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

@app.post("/generate_selenium/")
def generate_sel_script(test_case: str):
    global HTML_CONTENT

    if HTML_CONTENT == "":
        return {"status": "error", "message": "HTML not uploaded"}

    script = generate_selenium_script(test_case, HTML_CONTENT)

    return {
        "status": "success",
        "script": script
    }

