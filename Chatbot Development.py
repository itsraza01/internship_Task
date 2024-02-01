#Chatbot Development
import spacy

nlp = spacy.load('en_core_web_sm')

def chatbot():
    while True:
        user_input = input('You: ')
        doc = nlp(user_input)
        for token in doc:
            if token.pos_ == 'VERB':
                print(f'Chatbot: You said {token.text}.')
                break
        else:
            print('Chatbot: I did not understand what you said.')

chatbot()

