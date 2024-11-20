import pyjokes
from googletrans import Translator

def generate_joke():
    joke = pyjokes.get_joke()  # Get a random programming joke in English
    return joke

def translate_to_german(text):
    translator = Translator()
    translation = translator.translate(text, dest='de')  # Translate to Urdu
    return translation.text

if __name__ == "__main__":
    english_joke = generate_joke()
    print("Joke in English:")
    print(english_joke)

    german_joke = translate_to_german(english_joke)
    print("\nJoke in Urdu:")
    print(german_joke)
