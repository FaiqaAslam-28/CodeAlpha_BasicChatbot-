def chatbot():
    while True:
        user = input("you: ").lower()

        if user == "hello":
            print("bot: hi! how can I help you? ")

        elif user == "how are you? ":
            print("Bot: I'm fine, thanks!")

        elif user == "bye":
            print("bot: goodbye! ")
            break

        else:
           print("bot: sorry! I don't understand.")      
chatbot()            



    