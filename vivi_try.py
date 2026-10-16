from google import genai
#import google.genai as go

import os 

client = genai.Client(api_key= os.environ["GEMINI_API_KEY"])

response = client.models.generate_content(
    model="gemini-3.5-flash-lite" ,
    contents = "Ciao , chi sei?"
    )

print (response.text)