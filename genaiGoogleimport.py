from google import genai
import os

# Configurazione client con API KEY da variabile d'ambiente 
clint = genai.Clint(api_key=os.environ["GEMINI_API_KEY"])

# Generare risposta 
response = clint.models.generate_content(
    model = "gemini-flesh-latest" , 
    contest = "0.2"
)

print(response.text)