import requests
from vector_store import VectorStore   # using our vector db

# Call Ollama model
def call_llm(prompt: str):
    import requests
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": "llama3.2:1b", "prompt": prompt, "stream": False},

        timeout=120
    )

    raw = response.text

    # The model returns plain text, not JSON → so just return raw
    # Or extract between triple quotes
    if "```" in raw:
        cleaned = raw.split("```")[1].strip()
        return cleaned

    return raw



def generate_test_cases(query: str, vector_db: VectorStore):
    # Step 1: retrieve relevant context
    results = vector_db.query(query, k=5)

    context_text = ""
    for i in range(len(results["documents"][0])):
        doc_text = results["documents"][0][i]
        source = results["metadatas"][0][i]["source"]
        context_text += f"[SOURCE: {source}]\n{doc_text}\n\n"

    # Step 2: create prompt for test case generation
    prompt = f"""
You are a QA Test Case generation expert.

Use ONLY the information from the context below.

CONTEXT:
{context_text}

USER REQUEST:
{query}

INSTRUCTIONS:
- Generate clear, structured test cases.
- Use IDs: TC-001, TC-002, etc.
- Include Feature, Test_Scenario, Steps, Expected_Result.
- Add "Grounded_In: <source_document>" for each test.
- DO NOT hallucinate anything outside the provided context.
- Output strictly in Markdown format.

Begin now:
"""

    return call_llm(prompt)
