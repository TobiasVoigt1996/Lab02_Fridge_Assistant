import base64
import os
import pandas as pd
from dotenv import load_dotenv
from openai import OpenAI

# --------------------------------------------------
# Einstellungen
# --------------------------------------------------

IMAGE_PATH = "fridge.jpg"
OUTPUT_TXT = "fridge_analysis.txt"
OUTPUT_CSV = "fridge_results.csv"
MODEL = "gpt-4o-mini"

# --------------------------------------------------
# API-Key laden
# --------------------------------------------------

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY wurde nicht gefunden. Prüfe deine .env Datei.")

client = OpenAI(api_key=api_key)

# --------------------------------------------------
# Bild prüfen und codieren
# --------------------------------------------------

if not os.path.exists(IMAGE_PATH):
    raise FileNotFoundError(f"Bilddatei nicht gefunden: {IMAGE_PATH}")

with open(IMAGE_PATH, "rb") as image_file:
    image_base64 = base64.b64encode(image_file.read()).decode("utf-8")

# --------------------------------------------------
# Prompt
# --------------------------------------------------

prompt = """
Du bist ein Kühlschrank-Assistent.

Analysiere das Bild eines Kühlschranks und gib eine strukturierte Antwort auf Deutsch.

Bitte liefere:

1. Kurze Bildbeschreibung
2. Sichtbar erkannte Lebensmittel
3. Einen einfachen Rezeptvorschlag
4. Fehlende Zutaten / Einkaufsliste
5. Unsicherheiten oder Grenzen der Analyse

Wichtig:
- Nenne nur Dinge, die im Bild plausibel sichtbar sind.
- Wenn du etwas nicht sicher erkennst, markiere es als unsicher.
- Erfinde keine Zutaten.
"""

# --------------------------------------------------
# Anfrage an Foundation Model
# --------------------------------------------------

print("Sende Bild an das Foundation Model...")

response = client.chat.completions.create(
    model=MODEL,
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": prompt},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{image_base64}"
                    },
                },
            ],
        }
    ],
    max_tokens=700,
)

analysis = response.choices[0].message.content

# --------------------------------------------------
# Ausgabe
# --------------------------------------------------

print("\nAnalyse-Ergebnis:\n")
print(analysis)

with open(OUTPUT_TXT, "w", encoding="utf-8") as file:
    file.write(analysis)

results_df = pd.DataFrame([
    {
        "image_file": IMAGE_PATH,
        "model": MODEL,
        "analysis": analysis
    }
])

results_df.to_csv(
    OUTPUT_CSV,
    index=False,
    encoding="utf-8-sig",
    sep=";"
)

print(f"\nFertig. Ergebnisse gespeichert in {OUTPUT_TXT} und {OUTPUT_CSV}.")