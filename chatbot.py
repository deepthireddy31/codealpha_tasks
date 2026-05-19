# Simple Rule-Based Chatbot
# Step 1: Create chatbot function
def chatbot():
    print("Chatbot: Hello! Type 'bye' to exit.")

    # Step 2: Run chatbot continuously
    while True:
        user_input = input("You: ").lower()

        # Step 3: Define chatbot responses
        if user_input == "hello":
            print("Chatbot: Hi!")

        elif user_input == "how are you":
            print("Chatbot: I'm fine, thanks!")

        elif user_input == "what is your name":
            print("Chatbot: I am a simple chatbot.")

        elif user_input == "bye":
            print("Chatbot: Goodbye!")
            break

        else:
            print("Chatbot: Sorry, I don't understand.")

# Step 4: Call the function
chatbot()