# AI-CHATBOT-WITH-NLP

**COMPANY**: CODTECH IT SOLUTIONS PVT.LTD

**NAME**: SINDHUJA VAVILALA

**INTERN ID**: CT08FWC

**DOMAIN**: Python Programming

**BATCH DURATION**: December 25th, 2024 to January 25th, 2025

**MENTOR NAME**: NEELA SANTHOSH

# AI Chatbot with Natural Language Processing (NLP)

## Project Description

This project is an AI-powered chatbot that uses **Natural Language Processing (NLP)** techniques to interact with users in a human-like manner. The chatbot is designed to answer general queries, provide support for common requests, and improve the user experience with intelligent responses. It integrates **SpaCy** for entity extraction from user inputs, making the conversation context-aware. This chatbot can be utilized for various real-world applications such as customer support, technical assistance, and more.

## Tools and Libraries Used

1. **Python:**
   - Python was used as the primary programming language for this project. Its simplicity and extensive library support make it ideal for developing NLP-based applications like chatbots.

2. **NLTK (Natural Language Toolkit):**
   - NLTK is a powerful library in Python for working with human language data. It is used here to manage conversations, match user inputs with predefined patterns, and generate appropriate responses. Specifically, NLTK's `Chat` class and `reflections` dictionary were utilized for simple conversation flow.

3. **SpaCy:**
   - SpaCy is a robust NLP library focused on performance and ease of use. For this project, SpaCy’s entity recognition capabilities were leveraged to extract relevant information (such as names, dates, and locations) from user inputs, making the chatbot's responses more personalized and context-sensitive.

4. **Regular Expressions (Regex):**
   - Regular expressions were used to match user input patterns and trigger corresponding responses. This allows the chatbot to recognize various types of input such as greetings, farewells, and specific queries.

5. **Jupyter Notebook (Optional for Testing):**
   - Jupyter Notebook was used for initial testing and experimenting with small code snippets, making it easier to debug and refine the chatbot’s logic before moving to the final Python script.

## Resources Used

- **NLTK Documentation:** Used for understanding the usage of the `Chat` class and `reflections` dictionary to handle conversation patterns.
  
- **SpaCy Documentation:** Provided insights on how to use the entity recognition features, helping to enhance the chatbot’s ability to extract meaningful information from user queries.

- **Python Libraries:** Built-in Python libraries like `re` for regular expressions and `input()` for capturing user input were also utilized for pattern matching and simple conversation handling.

## How the Chatbot Works

1. **User Input:**
   - The chatbot listens for user input, which can be any query or statement. The user can interact with the chatbot by typing messages such as greetings or asking questions.

2. **Pattern Matching:**
   - Upon receiving the user’s input, the chatbot uses regular expressions to match the query with predefined patterns. Each pattern corresponds to specific types of queries, like greetings, asking for the chatbot’s name, or general information. When a match is found, the chatbot generates an appropriate response.

3. **Entity Extraction (Optional):**
   - The chatbot uses SpaCy to identify entities within the user’s input, such as dates, locations, names, or any other important information. This enables the chatbot to provide responses that are more context-aware and relevant to the user’s query.

4. **Response Generation:**
   - Based on the pattern matched, the chatbot generates a response. If the user asks for the chatbot's name or expresses a greeting, the chatbot will respond accordingly. If no match is found, it will prompt the user to rephrase their query.

5. **Termination:**
   - The chatbot will continue interacting with the user until the user types "bye" or a similar termination command. At that point, the conversation ends, and the chatbot exits.

## Example Output

Here is an example of how the conversation flow looks:

Hello! I'm here to assist you. Type 'bye' to end the conversation. You: Hello ChatBot: Hello! How can I assist you today?

You: What is your name? ChatBot: I'm a chatbot created to assist you. You can call me 'ChatBot.'

You: I need help with my account. ChatBot: I'm here to help! What do you need assistance with?

You: bye ChatBot: Goodbye! Have a great day!


When using **SpaCy** for entity extraction, the output may also include detected entities:


ChatBot (Entities): [('New York', 'GPE')]



This shows that the chatbot recognized "New York" as a **GPE** (Geopolitical Entity), which could be used for more dynamic and context-aware responses.


## How to Run the Project

1. **Install the necessary libraries:**

pip install nltk pip install spacy python -m spacy download en_core_web_sm


2. **Run the Python script:**

Save the code as `chatbot.py` and run it in the terminal.


3. **Start interacting with the chatbot:**

Once the chatbot is running, you can type queries and get responses. Type `bye` to end the conversation.

## Conclusion

This AI chatbot demonstrates the power of **Natural Language Processing (NLP)** for building intelligent systems capable of understanding and responding to human language. By utilizing **NLTK** for conversation management and **SpaCy** for advanced entity recognition, the chatbot offers a dynamic, interactive experience for users.

The project is a great starting point for anyone looking to develop more sophisticated NLP systems. Future improvements could include sentiment analysis, machine learning-based responses, integration with external APIs, and much more.

## The Output Of The Task

![image](https://github.com/user-attachments/assets/a4b0b6de-7f26-4f61-94b0-a12f51dbd8f4)
