# Reverse Words In A Given String
# Cody Kostyak
# https://practice.geeksforgeeks.org/problems/reverse-words-in-a-given-string/0 

# not much input was given into how exactly the data should be ingested.I decided to assume it's all one string/line.

"""
Sample:

Input:
2 i.like.this.program.very.much pqr.mno

Output:
much.very.program.this.like.i
mno.pqr

"""

def reverse_string(string_input:str):

    commands = []
    strings_to_reverse = []
    commands = string_input.split(' ')

    output = ''

    # first determine # of inputs
    try:
        int(commands[0])
        no_of_inputs = int(commands[0])
    except:
        quit()

    
    for x in range(no_of_inputs):
        strings_to_reverse.append(commands[x+1])

    # now to split strings
    for string in strings_to_reverse:
        split_string = string.split('.')
        split_string.reverse()

        for word in range(len(split_string)):
            output += split_string[word]

            if word < len(split_string)-1:
                output += '.'

            else:
                output += '\n'
    
    return output

print(reverse_string('2 i.like.this.program.very.much pqr.mno'))