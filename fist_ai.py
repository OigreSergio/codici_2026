from google import genai 
import os 

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

from google.genai import types
config = types.GenerateContentConfig(
    system_instruction="    Prego , dimmi tutto.."
)

#   loop infinito 
while True : 
    domanda = input("user : ")
    if domanda.lower() == "esci":
        print("alla prossima..")
        break

    response = client.models.generate_content(
        model = "gemini-3.flash" , 
        contents=domanda,
        config=config
    )
    print(f"AI: {response.text}\n")