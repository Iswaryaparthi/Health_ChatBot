import pandas as pd
import numpy as np
import pickle
from flask import Flask, request, jsonify, render_template
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from fuzzywuzzy import process
from flask import Flask, request, jsonify
import difflib

# Load dataset
df = pd.read_csv("health_symptoms.csv")

# Encode prognosis labels
prognosis_mapping = {idx: condition for idx, condition in enumerate(df['prognosis'].unique())}
df['prognosis'] = df['prognosis'].map({v: k for k, v in prognosis_mapping.items()})

# Split dataset
X = df.drop(columns=['prognosis'])
y = df['prognosis']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save trained model
model_filename = "chatbot_model.pkl"
with open(model_filename, "wb") as file:
    pickle.dump(model, file)

# Flask App
app = Flask(__name__)

# Load model
try:
    with open(model_filename, "rb") as file:
        model = pickle.load(file)
    print("✅ Model loaded successfully.")
except Exception as e:
    print(f"❌ Error loading model: {e}")
    model = None

@app.route('/')
def home():
    """Render home page with symptoms list."""
    return render_template('index.html', symptoms=list(X_train.columns))

# Predefined responses for symptoms
symptom_responses = {
    # Common Symptoms
    "hi": "Hello! How can I assist you today? Please enter your symptoms.",
    "hello": "Hi there! Tell me your symptoms, and I'll try to help.",
    "hey": "Hey! I'm here to assist you with your symptoms.",
    "fever": "A fever can be caused by a common cold, flu, or infection. Drink plenty of fluids and rest well.",
    "sore throat": "Sore throat? Try warm salt water gargles and honey tea. If it persists, consult a doctor.",
    "cough": "A cough can be a sign of flu or allergies. Stay hydrated and try steam inhalation.",
    "cold": "It sounds like you have a cold. Stay warm, drink herbal teas, and rest well.",
    "headache": "Headache? It could be due to dehydration or stress. Try drinking water and resting in a quiet space.",
    "fatigue": "Feeling exhausted? Fatigue can be due to stress, lack of sleep, or illness. Get proper rest and stay hydrated.",
    "body pain": "Body pain can be caused by muscle strain or viral infections. Rest and a warm compress may help.",
    "dizziness": "Dizziness can result from dehydration or low blood pressure. Sit down and drink water.",
    
    # Mental Health & Stress
    "anxiety": "Feeling anxious? Try deep breathing exercises or meditation. If it persists, consult a therapist.",
    "depression": "If you're feeling persistently low, try speaking to a loved one or seeking professional support.",
    "insomnia": "Having trouble sleeping? Try limiting screen time before bed, drinking warm tea, or meditating.",
    
    # Respiratory Issues
    "chest pain": "Chest pain can be serious. If it's severe or persistent, seek medical attention immediately.",
    "shortness of breath": "Difficulty breathing? Stay calm, sit upright, and seek medical help if it worsens.",
    "wheezing": "Wheezing can be a sign of asthma or allergies. Try staying in a clean environment and consult a doctor if needed.",
    
    # Skin Issues
    "itching": "Itching? It might be due to allergies or dry skin. Try applying moisturizer or an anti-itch cream.",
    "skin rashes": "Skin rashes can be caused by allergies or infections. Keep the area clean and avoid scratching.",
    "dry skin": "Dry skin? Apply a good moisturizer and stay hydrated.",
    
    # Stomach & Digestion
    "nausea": "Feeling nauseous? Try ginger tea or deep breathing. If persistent, consult a doctor.",
    "vomiting": "Vomiting can be due to food poisoning or an infection. Stay hydrated and rest.",
    "diarrhea": "Frequent diarrhea? Drink ORS (Oral Rehydration Solution) and avoid greasy foods.",
    "constipation": "Constipation? Increase your fiber intake and drink plenty of water.",
    "stomach pain": "Stomach pain can have multiple causes. Try resting and avoiding heavy meals.",
    
    # Allergies & Infections
    "continuous sneezing": "Sneezing often? It could be allergies. Try avoiding dust and using antihistamines.",
    "runny nose": "A runny nose can be due to a cold or allergies. Keep warm and stay hydrated.",
    "sinus pain": "Sinus pain? Try steam inhalation or a saline rinse.",
    "eye redness": "Red eyes? It could be irritation or an allergy. Try washing your eyes with clean water.",
    
    # General Weakness
    "joint pain": "Joint pain? Try mild stretching and avoid overexertion.",
    "muscle cramps": "Muscle cramps? Ensure you're getting enough electrolytes and stay hydrated.",
    "weakness": "Feeling weak? It might be due to low blood sugar or dehydration. Try eating something light.",

     # Adding "bye" and "thank you"
    "bye": "Goodbye! Take care and stay healthy. 😊",
    "thank you": "You're welcome! I'm here to help. Stay safe! 😊"
}

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json["message"].lower()

    recognized_responses = []
    for keyword, response in symptom_responses.items():
        if keyword in user_input:  # Check if keyword exists in user input
            recognized_responses.append(response)

    if recognized_responses:
        final_response = " ".join(recognized_responses)  # Combine responses if multiple keywords are detected
    else:
        final_response = "I couldn't recognize any symptoms. Please enter valid symptoms from the list."

    return jsonify({"response": final_response})


if __name__ == '__main__':
    app.run(debug=True)

