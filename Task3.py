# Basic Rule-Based Chatbot

def chatbot():
	print("Chatbot: Hi! Type 'bye' to exit.")
	while True:
		user_input = input("You: ").strip().lower()
		if user_input in ("hello", "hi", "hey"):
			print("Chatbot: Hi!")
		elif user_input in ("how are you", "how are you doing", "how's it going"):
			print("Chatbot: I'm fine, thanks! How can I help you?")
		elif user_input in ("what is your name", "who are you"):
			print("Chatbot: I'm a simple chatbot.")
		elif user_input in ("what can you do", "help"):
			print("Chatbot: I can chat with you! Try saying hello, asking how I am, or say bye to exit.")
		elif user_input in ("bye", "goodbye", "exit"):
			print("Chatbot: Goodbye!")
			break
		elif user_input in ("thank you", "thanks"):
			print("Chatbot: You're welcome!")
		else:
			print("Chatbot: Sorry, I don't understand.")

if __name__ == "__main__":
	chatbot()
