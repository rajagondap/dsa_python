from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer


def train_chatbot(chatbot):
    trainer = ChatterBotCorpusTrainer(chatbot)

    # Train the chatbot on English language data
    trainer.train("chatterbot.corpus.english")


def main():
    # Create a ChatBot instance
    chatbot = ChatBot("DynamicBot")

    # Train the chatbot
    train_chatbot(chatbot)

    print("DynamicBot: Hello! Type 'bye' to exit.")

    while True:
        user_input = input("You: ")

        if user_input.lower() == 'bye':
            print("DynamicBot: Goodbye!")
            break

        # Get response from the chatbot
        response = chatbot.get_response(user_input)
        print("DynamicBot:", response)


if __name__ == "__main__":
    main()
