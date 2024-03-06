#making a rule based chatbot 
# will use regular expressions for pattern matching for our user input 

import re 
rules = {
    r"hello|hi|hey" : "Hello, how are you today?",
    r"what is your name?" : "I am a chatbot. What is your name?",
    


}

print("Say hi to your chatbot!")
responses = " "

def chatbot():
    while True : 

        human_input = input("Write your response: ").lower()
        print(" ")
        if human_input == "quit":
            print("Bye! Have a great day!")
            break
        else: 
            for pattern, responses in rules.items():
                match = re.match(pattern, human_input)
                if match:
                    response = responses
                    print("Chatbot: ",response)
                    break
    
   
if __name__ == "__main__":
    chatbot()