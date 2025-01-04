import nltk
import spacy
from nltk.chat.util import Chat, reflections

# Download necessary NLTK resources (if you haven't done it already)
nltk.download('punkt')

# Define chatbot patterns and responses
pairs = [
    (r"hi|hello|hey", ["Hello! How can I assist you today?"]),
    (r"how are you?", ["I'm doing great, thank you! How can I help you?"]),
    (r"bye", ["Goodbye! Have a great day!"]),
    (r"(.*)(help|support)(.*)", ["I'm here to help! What do you need assistance with?"]),
    (r"(.*) your name ?", ["I'm a chatbot created to assist you. You can call me 'ChatBot.'"]),
    (r"(.*) (who are you|what are you)", ["I am an AI-powered chatbot built with NLP to assist you."]),
    (r"(.*) (your favorite color|color)", ["I don't have preferences, but blue is often a popular color."]),
    (r"(.*)", ["I'm sorry, I didn't quite understand that. Could you please rephrase?"]),
]

# Define the Chatbot class using NLTK's Chat class
class SimpleChatBot:
    def __init__(self):
        self.chatbot = Chat(pairs, reflections)
    
    def respond(self, user_input):
        return self.chatbot.respond(user_input)

# Set up SpaCy for entity extraction (Optional)
nlp = spacy.load('en_core_web_sm')

def get_entities(text):
    doc = nlp(text)
    entities = [(entity.text, entity.label_) for entity in doc.ents]
    return entities

# Main function to run the chatbot
if __name__ == "__main__":
    chatbot = SimpleChatBot()
    print("Hello! I'm here to assist you. Type 'bye' to end the conversation.")
    
    while True:
        user_input = input("You: ")
        response = chatbot.respond(user_input)
        print("ChatBot: " + response)
        
        # Optional: Extract entities from user input
        entities = get_entities(user_input)
        if entities:
            print(f"ChatBot (Entities): {entities}")
        
        if user_input.lower() == "bye":
            break
