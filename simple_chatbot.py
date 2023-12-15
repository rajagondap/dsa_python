import re
import random


def get_response(user_input):
    responses = {
        r"(hi|hello|hey)( there)*": ["Hello!", "Hi!", "Hey!"],
        r"how are you": ["I'm good, thanks!", "I'm doing well, how about you?"],
        r"what is your name": ["I'm a chatbot!", "Call me ChatGPT."],
        r"bye|goodbye": ["Goodbye!", "See you later!"]
    }

    for pattern, response_list in responses.items():
        if re.search(pattern, user_input, re.IGNORECASE):
            return random.choice(response_list)

    return "I'm sorry, I don't understand that."


def main():
    print("Chatbot: Hello! Type 'bye' to exit.")

    while True:
        user_input = input("You: ")

        if user_input.lower() == 'bye':
            print("Chatbot: Goodbye!")
            break

        response = get_response(user_input)
        print("Chatbot:", response)


if __name__ == "__main__":
    main()
