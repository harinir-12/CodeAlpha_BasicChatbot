print("=" * 40)
print("       WELCOME TO BASIC CHATBOT")
print("=" * 40)

print("Bot: Hello! I am your chatbot.")
print("Bot: Type 'bye' to end the chat.\n")

while True:
    user_input = input("You: ").lower().strip()

    if user_input == "hello" or user_input == "hi":
        print("Bot: Hi! Nice to meet you!")

    elif user_input == "how are you":
        print("Bot: I'm fine, thanks! How are you?")

    elif user_input == "i am fine":
        print("Bot: That's great to hear!")

    elif user_input == "what is your name":
        print("Bot: I am a Basic Python Chatbot!")

    elif user_input == "thank you" or user_input == "thanks":
        print("Bot: You're welcome!")

    elif user_input == "bye":
        print("Bot: Goodbye! Have a great day!")
        break

    else:
        print("Bot: Sorry, I don't understand that.")