# Lab02 – Fridge Recipe Assistant 

## Projektbeschreibung

Dieses Projekt implementiert ein **multimodales KI-System**, das ein Bild eines Kühlschranks analysiert und daraus strukturierte Informationen sowie Handlungsempfehlungen generiert.

Das System kombiniert **Bildverarbeitung und natürliche Sprachverarbeitung (NLP)** durch die Nutzung eines Foundation Models über eine API.

---

## Zielsetzung

Ziel ist es, praktische Erfahrung mit **Foundation Models** zu sammeln und ein reales Szenario umzusetzen, bei dem Bilddaten in verwertbare Informationen überführt werden.

---

## Szenario  LAB02

Ein Nutzer fotografiert den Inhalt seines Kühlschranks.
Das System analysiert das Bild und erzeugt:

* eine Bildbeschreibung
* erkannte Lebensmittel
* einen Rezeptvorschlag
* eine Einkaufsliste
* eine Reflexion über Unsicherheiten

---

## Prozessablauf

1. Einlesen eines lokalen Bildes (`fridge.jpg`)
2. Umwandlung des Bildes in ein API-kompatibles Format (Base64)
3. Senden der Anfrage an ein multimodales Foundation Model
4. Analyse des Bildinhalts durch das Modell
5. Generierung einer strukturierten Textantwort
6. Speicherung der Ergebnisse als `.txt` und `.csv`

---

## Verwendete Technologien

* Python
* OpenAI API (Foundation Model)
* pandas
* python-dotenv
* Base64-Encoding

---

## Verwendetes Modell

* `gpt-4o-mini` (multimodales Foundation Model)

---

## Projektstruktur

```
Lab02_Fridge_Assistant/
│── fridge_assistant.py
│── fridge.jpg
│── fridge_analysis.txt
│── fridge_results.csv
│── requirements.txt
│── README.md
```

Nicht enthalten (aus Sicherheitsgründen):

```
.env
.venv
```

---

##  Ausführung

1. Abhängigkeiten installieren:

```bash
pip install -r requirements.txt
```

2. API-Key in `.env` hinterlegen:

```
OPENAI_API_KEY=
```

3. Programm starten:

```bash
python fridge_assistant.py
```

---

## Ergebnis

Das System erzeugt:

* `fridge_analysis.txt` → strukturierte Analyse
* `fridge_results.csv` → tabellarische Speicherung

---

## Grenzen 

* Es werden nur **sichtbare Inhalte erkannt**
* Teilweise Unsicherheiten bei verdeckten oder unklaren Objekten
* Keine Informationen über Haltbarkeit oder Mengen
* Rezeptvorschläge sind heuristisch und nicht garantiert optimal

---

## Nutzen

Der Proof of Concept zeigt, wie unstrukturierte Bilddaten automatisch verarbeitet werden können, um:

* Lebensmittel besser zu nutzen
* Rezepte vorzuschlagen
* Einkaufsplanung zu unterstützen
* Zeit im Alltag zu sparen

---

## Fazit

Das Projekt demonstriert erfolgreich die Integration eines **multimodalen Foundation Models** in einen realen Anwendungsfall.
Es zeigt, wie Bild- und Textdaten kombiniert werden können, um automatisierte Entscheidungen und Empfehlungen zu ermöglichen.

---
