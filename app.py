import re
import pandas as pd
from flask import Flask, request, jsonify

app = Flask(__name__)

# Charger les DataFrames depuis les fichiers CSV
ecoles_df = pd.read_csv('ecoles_dataset.csv')
titres_df = pd.read_csv('titres_dataset.csv')

# Fonction pour extraire les informations
def extract_info(line):
    annee_match = re.search(r"\b\d{4}\b", line)
    annee = annee_match.group(0) if annee_match else None

    # Liste des titres et écoles à partir des DataFrames
    titres = titres_df['titres'].tolist()
    ecoles = ecoles_df['ecoles'].tolist()

    titre_match = re.search(rf"\b(?:{'|'.join(re.escape(titre) for titre in titres)})\b", line, re.IGNORECASE)
    titre = titre_match.group(0) if titre_match else None

    ecole_match = re.search(rf"\b(?:{'|'.join(re.escape(ecole) for ecole in ecoles)})\b", line, re.IGNORECASE)
    ecole = ecole_match.group(0) if ecole_match else None

    return annee, titre, ecole

@app.route('/extract', methods=['POST']) 
def extract():
    data = request.get_json()
    input_lines = data.get('input_lines', [])

    extracted_info = []
    for line in input_lines:
        annee, titre, ecole = extract_info(line)
        extracted_info.append({
            'line': line,
            'annee': annee,
            'titre': titre,
            'ecole': ecole
        })

    return jsonify(extracted_info)

if __name__ == '__main__':
    app.run(debug=True)
