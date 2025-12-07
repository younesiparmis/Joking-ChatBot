import random

jokes = [
    "Why is the computer always tired? Because it keeps eating bytes 😆",
    "Why do programmers never get lost? Because they always follow recursion 😂",
    "Want to know a secret? I never sleep 😎"
]

print("Hi! I'm a Joke Chatbot. Talk to me :)")

while True:
    user_input = input("You: ").lower()
    
    if "bye" in user_input:
        print("Chatbot: Bye! Keep smiling 😄")
        break
    else:
        print("Chatbot:", random.choice(jokes))