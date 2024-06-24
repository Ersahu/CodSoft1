def chatbot_response(user_input):
    user_input = user_input.lower()  # Convert input to lowercase for case-insensitive matching
    
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I assist you today?"
    elif "how are you" in user_input:
        return "I'm just a bot, but I'm doing great! How about you?"
    elif "your name" in user_input:
        return "I'm a simple chatbot created by Vaibhav. You can call me panda."
    elif "weather" in user_input:
        return "I can't provide real-time weather updates, but you can check a weather website for the latest information."
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a great day!"
    else:
        return "I'm sorry, I didn't understand that. Can you please rephrase?"

# Main loop to keep the chatbot running until the user says "bye"
def main():
    print("Chatbot: Hello! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")
        if "bye" in user_input.lower():
            break

if _name_ == "_main_":
    main()
