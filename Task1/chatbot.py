def chatbot():
    print("Simple Rule-Based Chatbot Started")
    print("Type 'bye' to exit\n")

    while True:
        user_input = input("You: ").strip().lower()

        if user_input == "bye":
            print("Chatbot: Goodbye! Have a nice day 😊")
            break

        elif any(word in user_input for word in ["hi", "hello", "hey"]):
            print("Chatbot: Hello! How can I help you?")

        elif "how are you" in user_input:
            print("Chatbot: I'm fine, thank you! How about you?")

        elif any(word in user_input for word in ["your name", "who are you"]):
            print("Chatbot: I am a simple rule-based chatbot.")

        elif "what can you do" in user_input:
            print("Chatbot: I can answer basic predefined questions and help understand chatbot logic.")

        elif any(word in user_input for word in ["ai", "artificial intelligence"]):
            print("Chatbot: AI stands for Artificial Intelligence, which is the simulation of human intelligence in machines.")

        elif "nlp" in user_input:
            print("Chatbot: NLP stands for Natural Language Processing, which enables computers to understand human language.")

        elif "joke" in user_input:
            print("Chatbot: Why did the computer show up at work late? It had a hard drive!")

        elif "weather" in user_input:
            print("Chatbot: I don't have real-time weather data, but you can check a weather app.")

        elif "time" in user_input:
            from datetime import datetime
            print("Chatbot: The current time is", datetime.now().strftime("%H:%M:%S"))

        elif "date" in user_input:
            from datetime import datetime
            print("Chatbot: Today's date is", datetime.now().strftime("%Y-%m-%d"))

        elif "my name is" in user_input:
            name = user_input.replace("my name is", "").strip().title()
            print(f"Chatbot: Nice to meet you, {name}!")

        elif "prime minister of india" in user_input:
            print("Chatbot: The Prime Minister of India is Narendra Modi.")

        elif "what is python" in user_input:
            print("Chatbot: Python is a high-level programming language known for simplicity and versatility.")

        elif "machine learning" in user_input:
            print("Chatbot: Machine learning is a subset of AI that allows systems to learn from data.")

        elif "who created you" in user_input:
            print("Chatbot: I was created as part of an internship task.")

        elif "help" in user_input:
            print("Chatbot: You can ask me about AI, NLP, Python, time, date, or general questions.")

        elif "thank" in user_input:
            print("Chatbot: You're welcome! 😊")

        else:
            print("Chatbot: Sorry, I didn't understand that.")

if __name__ == "__main__":
    chatbot()

