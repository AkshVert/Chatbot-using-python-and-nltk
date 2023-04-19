import nltk
from nltk.chat.util import Chat, reflections

pairs = [    
    ["(hi|hello|hey)", ["Hello, how was your day?"]],
    ["(good|ok|well|not good|bad|awesome|nice|fine)",["I wish to have you a great day ahead!"]],
    ["thanks|thank you|ok",["******Talking to you feels good!******\nNow can i tell you your todays'task?"]],
    ["no", ["Ok, do u want thought of the day(y or n)"]],
    ["ready",["Have a splendid day and energy for doing the tasks, Bye"]],
    ["what is your name?", ["My name is Maniac, How can I help you?"]],
    ["how are you?", ["I'm doing well, thanks for asking."]],
    ["what is your age?", ["I'm of your age only."]],
    ["what is your (location|city)?", ['I exist on your screen.']],
    ["How you were (created|made)?", ["I was created by A under idea of M."]],
    ["(y|Thought of the day)",["Love the life"]],
]

chatbot = Chat(pairs, reflections)

def chat():
    print("Hello, I'm maniac!")
    while True:
        user_input = input("> ")
        if user_input.lower() == 'bye':
            print("Goodbye!")
            break
        response = chatbot.respond(user_input)
        print(response)

chat()
