import re
import pandas as pd
from flask import Flask, request, jsonify

app = Flask(__name__)

# List of month names
months = [
    "January", "February", "March", "April", "May", "June", "July",
    "August", "September", "October", "November", "December",
    "janvier", "février", "mars", "avril", "mai", "juin", "juillet",
    "août", "septembre", "octobre", "novembre", "décembre",
    "Janv", "Fév","Fev" "Mars", "Avr", "Mai", "Juin", "Juil", "Août","Aout" "Sept", "Oct", "Nov", "Déc","Dec"
    "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec","janv", "fév", "fev", "mars", "avr", "mai", "juin", "juil", "août", "aout", "sept", "oct", "nov", "déc", "dec",
    "jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec","january", "february", "march", "april", "may", "june", "july",
    "august", "september", "october", "november", "december","fevrier","JANVIER", "FÉVRIER", "MARS", "AVRIL", "MAI", "JUIN", "JUILLET",
    "AOÛT", "SEPTEMBRE", "OCTOBRE", "NOVEMBRE", "DÉCEMBRE", "Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet",
    "Août", "Septembre", "Octobre", "Novembre", "Décembre","Fevrier","Decembre","Aout"
]

# Load DataFrames from CSV files
ecoles_df = pd.read_csv('ecoles_dataset.csv')
titres_df = pd.read_csv('titres_dataset.csv')

# Function to extract information
def extract_info(line):
    annee_match = re.search(r"\b\d{4}\b", line)
    annee = annee_match.group(0) if annee_match else None

    month_match = re.search(rf"\b(?:{'|'.join(re.escape(month) for month in months)})\b", line, re.IGNORECASE)
    month = month_match.group(0) if month_match else None

    # Lists of titles and schools from DataFrames
    titres = titres_df['titres'].tolist()
    ecoles = ecoles_df['ecoles'].tolist()

    titre_match = re.search(rf"\b(?:{'|'.join(re.escape(titre) for titre in titres)})\b", line, re.IGNORECASE)
    titre = titre_match.group(0) if titre_match else None

    ecole_match = re.search(rf"\b(?:{'|'.join(re.escape(ecole) for ecole in ecoles)})\b", line, re.IGNORECASE)
    ecole = ecole_match.group(0) if ecole_match else None

    return annee, month, titre, ecole

@app.route('/extract', methods=['POST']) 
def extract():
    # Get raw text from POST request
    input_text = request.data.decode('utf-8')

    # Split text into lines
    input_lines = input_text.split('\n')

    extracted_info = []
    for line in input_lines:
        annee, month, titre, ecole = extract_info(line)
        extracted_info.append({
            'line': line,
            'date': f"{month}:{annee}",
            'titre': titre,
            'ecole': ecole
        })

    return jsonify(extracted_info)

if __name__ == '__main__':
    app.run(debug=True)
