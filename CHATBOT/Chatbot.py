import re
import operator
import time

# Define the rules and responses

# Define the operators and their corresponding functions

def calculate_expression(match):
    expression = match.group(1)
    tokens = re.split(r'(\+|\-|\*|\/|\^)', expression)
    numbers = [float(token) for token in tokens[::2]]
    operators = [ops[token] for token in tokens[1::2]]
    result = numbers[0]
    for op, num in zip(operators, numbers[1:]):
        result = op(result, num)
    return f"The result of {expression} is {result}"

ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '^': operator.pow
}

rules = {
    
    r'hi|hello|hey': ['Hello!', 'Hi there!', 'Hey, how can I help you?'],
    r'how are you?': ['I\'m doing well, thanks for asking!', 'I\'m an AI assistant, but I\'m functioning properly.'],
    r'what(\'s)? your name?': ['My name is Claude.', 'You can call me Claude.'],
    r'thank(s)?( you)?': ['You\'re welcome!', 'No problem, happy to help!'],
    r'bye|exit|quit|leave': ['Goodbye!', 'Take care!'],
    r'calculate (\d+\s*[\+\-\*\/\^]\s*\d+)': calculate_expression
}

print("Welcome to the rule-based chatbot! Type 'bye', 'exit', or 'quit' to end the conversation.")

while True:
    time.sleep(.5)
    user_input = input("> ").lower()

    # Check if the user wants to quit
    if user_input in ['bye', 'exit', 'quit' , 'leave']:
        print(rules[r'bye|exit|quit|leave'][0])
        break

    # Match the user input with the rules
    matched_rule = None
    for pattern, response in rules.items():
        match = re.search(pattern, user_input)
        if match:
            matched_rule = pattern
            if callable(response):
                print(response(match))
            else:
                import random
                print(random.choice(response))
            break

    if not matched_rule:
        print("I'm sorry, I didn't understand that. Could you rephrase your question?")