import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def get_analysis(df_columns, question):

    prompt = f"""
You are a Pandas Data Analyst.

Dataset Columns:
{df_columns}

User Question:
{question}

Rules:
1. Return only executable Python code.
2. Do NOT return markdown.
3. Do NOT return explanations.
4. DataFrame name is df.
5. Store final answer in variable result.

Example:
result = df["Sales"].sum()
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    code = response.choices[0].message.content.strip()

    # Remove markdown if model returns it
    code = code.replace("```python", "")
    code = code.replace("```", "")
    code = code.strip()

    return code