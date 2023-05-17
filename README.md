# python_DS_ALGO
This is for Data Structure and algo questions 

Lesson 1: 

Binaray Search, Linked lists and complexity and about steps that you need to take in order to succesfully understand any questions.

first of all, 

Why is Data structure and algorithms Important? and why should you learn it?

  - you can think about a problem systematically, and solve it step by  step
  - envision different inputs, outputs, and edge cases
  - can communicate ideas clearly
  - convert your vision and ideas into working code more efficiently


Steps that you need to take :



- state the problem clearly. Identify inputs and outputs
- come up with some example inputs and outputs. try to cover all edge cases
- come up with a correct solution for the problem. state it in plain english
- implement the solution and test it using example inputs.
- analyze the algortithm's complexity and identify inefficiencies.
- apply the right technique to overcome the inefficiency.


problem 1-1 Alice has some cards with numbers written on them. She arranges the cards in decreasing order, and lays them out face down in a sequence on a table. She challenges Bob to pick out the card containing a given number by turning over as few cards as possible. Write a function to help Bob locate the card.


1. State the problem clearly. identify the input and output formats

let's put sequence of cards as a list

[ 13, 12, 11, 7, 4, 3, 1, 0]

lets now state the input and outputs: 
inputs : 
1. A list of numbers sorted in decreawsing order
2. A number of the index of the specific number

output:
3. position(index) of the specific number.

lets now create a functinon
def locate_card(cards, query):
  pass


tip: 
name your function and variables clearly and descriptive.
do not start coding without finishing step 1 clearly.

2. come up with some example inputs and outputs

coming up with text cases with all the edge cases will be helpful during your interview session

ex1.

cards = [13, 11, 10, 7, 4, 3, 1, 0]
query = 7
output = 3 

result = locate_card(cards,query)
print(result)

result == output

we're going to represent test cases as dictionary

test = {
    'input': {
        'cards' : {13,11,10,7,4,3,1,0},
        'query': 7
    },
    'output':3
}

locate_card(**test['input']) == test['output']

