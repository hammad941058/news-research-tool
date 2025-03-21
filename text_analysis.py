import openai
from config import GROQ_API_KEY

# Set Groq API key and base URL
openai.api_key = GROQ_API_KEY
openai.api_base = "https://console.groq.com/docs/overview"  # Use Groq's API URL

def analyze_text(prompt):
    response = openai.ChatCompletion.create(
        model="mixtral-8x7b-32768",  # Use Groq's Mixtral model
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message["content"]

if __name__ == "__main__":
    text = "Tell me about AI trends in 2024."
    result = analyze_text(text)
    print(result)


    






