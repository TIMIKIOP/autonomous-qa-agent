import streamlit as st
import requests
import json

BACKEND_URL = "http://127.0.0.1:8000"

st.title("Autonomous QA Agent")

# ------------------------------------------------------
# Upload Support Documents
# ------------------------------------------------------
st.header("📄 Upload Support Documents")

doc_files = st.file_uploader(
    "Upload MD / TXT / JSON / PDF documents",
    accept_multiple_files=True
)

if st.button("Upload Documents"):
    if doc_files:
        files = [("files", (f.name, f, "text/plain")) for f in doc_files]
        with st.spinner("Uploading documents..."):
            res = requests.post(f"{BACKEND_URL}/upload_docs/", files=files)

        try:
            st.success(res.json()["message"])
        except:
            st.error("Backend error: " + res.text)
    else:
        st.warning("Please upload at least one document.")


# ------------------------------------------------------
# Upload checkout.html
# ------------------------------------------------------
st.header("📄 Upload checkout.html")

html_file = st.file_uploader("Upload checkout.html", type=["html"])

if st.button("Upload HTML File"):
    if html_file:
        file = {"file": (html_file.name, html_file, "text/html")}
        with st.spinner("Uploading HTML..."):
            res = requests.post(f"{BACKEND_URL}/upload_html/", files=file)

        try:
            st.success(res.json().get("message", "HTML uploaded successfully!"))
        except:
            st.error("Backend error: " + res.text)
    else:
        st.warning("Please upload checkout.html first.")


# ------------------------------------------------------
# Build Knowledge Base
# ------------------------------------------------------
st.header("🧠 Build Knowledge Base")

if st.button("Build KB"):
    with st.spinner("Building vector knowledge base..."):
        res = requests.post(f"{BACKEND_URL}/build_knowledge_base/")

    try:
        st.success(res.json()["message"])
    except:
        st.error("Backend Error: " + res.text)


# ------------------------------------------------------
# Generate Test Cases
# ------------------------------------------------------
st.header("🧪 Generate Test Cases")

query = st.text_input("Enter QA request (e.g., Generate test cases for checkout page)")

if st.button("Generate Test Cases"):
    if query.strip() != "":
        with st.spinner("Generating test cases using LLM..."):
            res = requests.post(
                f"{BACKEND_URL}/generate_test_cases/",
                params={"query": query}
            )

        # Safe JSON handling
        try:
            response = res.json()
        except:
            st.error("Backend returned non-JSON response:")
            st.text(res.text)
            st.stop()

        st.subheader("📌 Backend Response:")
        st.json(response)

        if "test_cases" in response:
            st.markdown(response["test_cases"])
        else:
            st.error("Backend Error: " + str(response))

    else:
        st.warning("Please enter a query.")


# ------------------------------------------------------
# Generate Selenium Script
# ------------------------------------------------------
st.header("🤖 Generate Selenium Script")

test_case_text = st.text_area("Paste a selected test case here")

if st.button("Generate Selenium Script"):
    if test_case_text.strip() != "":
        with st.spinner("Generating Selenium script..."):
            res = requests.post(
                f"{BACKEND_URL}/generate_selenium/",
                params={"test_case": test_case_text}
            )

        try:
            response = res.json()
        except:
            st.error("Backend returned invalid response:")
            st.text(res.text)
            st.stop()

        st.subheader("📌 Backend Response:")
        st.json(response)

        if "script" in response:
            st.code(response["script"], language="python")
        else:
            st.error("Backend Error: " + str(response))
    else:
        st.warning("Paste a test case first.")
