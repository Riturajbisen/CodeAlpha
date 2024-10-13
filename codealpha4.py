import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
import random

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('stopwords')

# Create a list of greetings and responses
greetings = ['hello', 'hi', 'hey', 'howdy', 'good morning', 'good afternoon', 'good evening']
responses = ['Hello there!', 'Hi!', 'Hey!', 'Howdy!', 'Good morning to you!', 'Good afternoon!', 'Good evening!']

# Create a list of questions and answers
questions = ['how are you?', 'what is your name?', 'where are you from?', 'what do you do for a living?']
answers = ['I am doing well, thank you!', 'My name is Chatbot.', 'I am from the digital world.', 'I am a language model designed to provide information and complete tasks.']

# Create a list of topics and related keywords
topics = {'sports': ['football', 'basketball', 'baseball', 'soccer', 'tennis'],
          'movies': ['action', 'comedy', 'drama', 'romance', 'sci-fi'],
          'music': ['pop', 'rock', 'hip hop', 'country', 'classical']}

# Create a chatbot function
def chatbot(user_input):
    # Tokenize the user input
    tokens = word_tokenize(user_input.lower())

    # Remove stop words
    stop_words = set(nltk.corpus.stopwords.words('english'))
    filtered_tokens = [word for word in tokens if word not in stop_words]

    # Stem the words
    stemmer = PorterStemmer()
    stemmed_tokens = [stemmer.stem(word) for word in filtered_tokens]   

    # Check for greetings
    if any(word in greetings for word in stemmed_tokens):
        return random.choice(responses)

    # Check for questions
    if any(word in questions for word in stemmed_tokens):
        return random.choice(answers)

    # Check for topics
    for topic, keywords in topics.items():
        if any(word in keywords for word in stemmed_tokens):
            return f"I am interested in {topic}. What would you like to know about it?"

    # Default response
    return "I'm sorry, I don't understand. Could you please rephrase your question?"

# Example usage
while True:
    user_input = input("You: ")
    chatbot_response = chatbot(user_input)
    print("Chatbot:", chatbot_response)
