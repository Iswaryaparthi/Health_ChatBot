# AI Chatbot for Symptom Identification

## Overview
The Health Chatbot is an AI-powered application designed to interact with users through text-based conversations, collect symptoms, and suggest possible conditions based on a trained Natural Language Processing (NLP) model.

## Features
- **Symptom Identification**: Matches user-inputted symptoms with predefined conditions.
- **Dynamic Responses**: Retrieves symptom-related advice from a dataset.
- **Machine Learning Integration** *(Future)*: Predicts possible conditions based on user input.
- **Real-Time Interaction**: Provides instant responses using Flask and JavaScript.
- **Scalability**: Can be expanded to support additional medical conditions and languages.

## Technology Stack

### Frontend (Client-Side)
- **HTML**: Structure of the chatbot interface (chat window, input box, buttons).
- **CSS**: Enhances the appearance of the chatbot.
- **JavaScript**: Handles user input, sends messages to the backend, and updates the chat UI dynamically.

### Backend (Server-Side) with Flask (Python)
- **Flask**: Serves the web page and processes chatbot responses.
- **Flask Routes**: The `/chat` route receives user messages, processes them, and returns responses.
- **Chatbot Logic**: Uses NLP or predefined responses to generate appropriate replies.

## How It Works
1. User enters a message in the input field.
2. JavaScript captures the input and sends it to the Flask backend via a fetch request.
3. Flask processes the request and returns a response.
4. JavaScript updates the chat window with the bot's response.

## Dataset Usage
- **Recognizing Symptoms**: Matches input symptoms with predefined ones.
- **Generating Responses**: Retrieves relevant health advice dynamically.
- **Future ML Predictions** *(If integrated)*: Predicts possible conditions based on historical records.

## Future Enhancements
- Integrate a machine learning model for improved symptom prediction.
- Expand the dataset to include more medical conditions.
- Implement voice-based interaction.
- Add support for multiple languages.


