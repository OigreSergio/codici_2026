import os
from google import genai
from google.genai import types


def main() -> None:
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("Variabile d'ambiente GEMINI_API_KEY non impostata.")

    client = genai.Client(api_key=api_key)

    safety_settings = [
        types.SafetySetting(category="HARM_CATEGORY_DANGEROUS_CONTENT", threshold="BLOCK_NONE"),
        types.SafetySetting(category="HARM_CATEGORY_HATE_SPEECH", threshold="BLOCK_NONE"),
        types.SafetySetting(category="HARM_CATEGORY_HARASSMENT", threshold="BLOCK_NONE"),
        types.SafetySetting(category="HARM_CATEGORY_SEXUALLY_EXPLICIT", threshold="BLOCK_NONE"),
    ]

    while True:
        domanda = input(">>> ")
        if domanda.strip().lower() in {"exit", "quit"}:
            break

        config = types.GenerateContentConfig(
            temperature=0.2,
            max_output_tokens=1024,
            safety_settings=safety_settings,
        )
        response = client.models.generate_content(
            model="gemini-flash-lite-latest",
            contents=domanda,
            config=config,
        )

        if getattr(response, "text", None):
            print(response.text)
        else:
            print(response)


if __name__ == "__main__":
    main()