import random
adjective = input('Adjective: ')
name = input('Name: ')
place = input('Place: ')
verb = input('Plural Verb: ')
animal = input('animal: ')

def game_choice():
    madlib1 = ['He was a', adjective, 'Man that goes by', name, 'He is well known for the situation at', place,'Where a/an ', animal, 'was and he', verb, 'it']
    madlib2 = ['The', animal, 'was roaming around the local', place,'He caught the attention of the law enforcement by', verb, 'the nearby citizens. The police describe this animal as', adjective, 'and he goes by the name of', name]
    madlib3 = [name, 'is the name of a man who does the unspeakable. He is known to ', verb, 'at a/an local', place,'He is usually seen with is pet', animal, 'that is describes as', adjective]

    listoflist = [madlib1, madlib2, madlib3]
    print(random.choice(listoflist))
game_choice() 
