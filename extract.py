# -*- coding: utf-8 -*-
"""extract.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zRff6fFc4idmNoeBhjr-M-qhMeOlVxXK
"""

import re

def extract_month_and_year(text):
    # Define regular expression patterns for month and year extraction
    month_pattern = r'(?:January|February|March|April|May|June|July|August|September|October|November|December)'
    year_pattern = r'\d{4}'

    # Search for month and year patterns in the text
    month_match = re.search(month_pattern, text, re.IGNORECASE)
    year_match = re.search(year_pattern, text)

    # Extract and format the matched month and year
    if month_match:
        extracted_month = month_match.group(0)
    else:
        extracted_month = None

    if year_match:
        extracted_year = year_match.group(0)
    else:
        extracted_year = None

    return extracted_month, extracted_year

# Test the function with an example text
example_text = "The event will take place in October 2023."
month, year = extract_month_and_year(example_text)
if month and year:
    print(f"Extracted Month: {month}, Year: {year}")
elif month:
    print(f"Extracted Month: {month}")
elif year:
    print(f"Extracted Year: {year}")
else:
    print("No month or year found in the text.")
# Example 1
text1 = "The deadline for submission is September 2023."
month1, year1 = extract_month_and_year(text1)
print(f"Extracted Month: {month1}, Year: {year1}")

# Example 2
text2 = "Join us for the conference in May."
month2, year2 = extract_month_and_year(text2)
print(f"Extracted Month: {month2}, Year: {year2}")

# Example 3
text3 = "The project is scheduled for completion in December of 2022."
month3, year3 = extract_month_and_year(text3)
print(f"Extracted Month: {month3}, Year: {year3}")

# Example 4
text4 = "No specific date was mentioned."
month4, year4 = extract_month_and_year(text4)
if month4 or year4:
    print(f"Extracted Month: {month4}, Year: {year4}")
else:
    print("No month or year found in the text.")

import re

def extract_formation_or_university(text):
    # Définir un modèle d'expression régulière pour l'extraction du nom de formation/université
    pattern = r'(?:formation|université|école|faculté|institut)\s+(?:de|d\'|des)?\s*([A-Za-z\s\-]+)'

    # Rechercher le motif dans le texte
    match = re.search(pattern, text, re.IGNORECASE)

    # Extraire et formater le nom de formation/université
    if match:
        extracted_name = match.group(1)
        return extracted_name
    else:
        return None

# Tester la fonction avec des exemples de phrases
exemple1 = "J'étudie à l'université de Paris-Sud."
resultat1 = extract_formation_or_university(exemple1)
if resultat1:
    print("Nom de formation/université:", resultat1)
else:
    print("Aucun nom de formation/université trouvé.")

exemple2 = "Je suis inscrit(e) dans une école d'ingénieurs."
resultat2 = extract_formation_or_university(exemple2)
if resultat2:
    print("Nom de formation/université:", resultat2)
else:
    print("Aucun nom de formation/université trouvé.")