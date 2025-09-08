import os
import google.generativeai as genai
from dotenv import load_dotenv
from pdf_reader import read_pdf

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")

pdf_text = read_pdf("database_lab2.pdf")[:3000]

user_question = input("Enter your question from the PDF: ")

prompt = f"""
Tum ek intelligent AI ho. Neeche PDF ka content diya gaya hai.
Sirf isi content ka use karke user ke question ka jawab do.

PDF Content:
\"\"\"
{pdf_text}
\"\"\"

Question:
{user_question}
"""

response = model.generate_content(prompt)
print("\n🤖 Gemini ka jawab:\n", response.text)
