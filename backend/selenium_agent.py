import requests

def call_llm(prompt):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        }
    )
    return response.json()["response"]


def generate_selenium_script(test_case_text, html_content):
    prompt = f"""
You are a Selenium Python automation expert.

Use ONLY the given HTML and the test case to create a fully working Selenium Python script.

HTML CONTENT:
{html_content}

TEST CASE:
{test_case_text}

REQUIREMENTS:
- Use Chrome WebDriver
- Use correct CSS selectors, IDs, names from the HTML
- Include comments for each step
- Code must be ready to run
- Do NOT hallucinate elements not in the HTML
- Output ONLY the Python code with no explanation.

Begin generating the Selenium script now:
"""

    return call_llm(prompt)
