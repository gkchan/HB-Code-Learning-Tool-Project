# Questions for quiz in learning code program

# More questions to come depending on time

# import classes from model module
from model import User, Level, Module, Function

# import database necessities from model module
# from model import db, connect_to_db

from random import randint, choice, sample, shuffle

def ask_question():
    """Asks a question about the sample code and output"""
    
    # gets all functions with sample code and output, may need to be adapted if database ever becomes too big
    functions = Function.query.filter(Function.sample_code != "", Function.output != "").all()
    function_entry = choice(functions)
 
    sample_code_question = "What output do you get when you input the following code?"
    sample_code = function_entry.sample_code

    answer = function_entry.output
    answer_choices = [ answer ]

    # checks that output is not blank and is not repeated and then adds it until there are 4 answer choices
    while len(answer_choices) < 4:
        function = choice(functions)
        output = function.output
        if output and output not in answer_choices:
            answer_choices.append(output)

    shuffle(answer_choices)

    return sample_code_question, sample_code, answer, answer_choices


