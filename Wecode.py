import pandas as pd

# Loading dataset in a variable named data
try:
    data=pd.read_csv('das1.csv', encoding='latin1')
except FileNotFoundError:
    print("Error: could not find the symptoms file")
except pd.errors.ParserError:
    print("Error: the dataset is not properly formatted.")

# Get user input
user_input = input("Please enter your symptoms, separated by commas: ")
symptoms = [symptom.strip() for symptom in user_input.split(',')]

# Filter dataset for matching symptoms
try:
    match=data[data.isin(symptoms).any(axis=1)]
except KeyError:
    print("Error: the dataset is not properly formatted.")
except NameError:
    print("Error: the dataset could not be loaded.")

# Print possible diagnoses
if match.empty():
    print("Sorry, we could not find any diagnoses matching your symptoms.")
else:
    diagnoses = match['diagnosis'].unique()
    print("Possible diagnoses based on your symptoms:")
    for diagnosis in diagnoses:
        print(diagnosis)
