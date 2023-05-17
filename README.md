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

is this enough? probably not.

lets state more options
The number query occurs somewhere in the middle of the list cards.
query is the first element in cards.
query is the last element in cards.
The list cards contains just one element, which is query.
The list cards does not contain number query.
The list cards is empty.
The list cards contains repeating numbers.
The number query occurs at more than one position in cards.
(can you think of any more variations?)

Edge cases : could be a scenario where its rare or extreme cases.

tests.append({
    'input':{
        'cards': [4,2,1,-1],
        'query': 1
    },
    'output':0
})
#query is the last element
tests.append({
    'input': {
        'cards':[3, -1, -9, -127],
        'query': -127
    },
    'output': 3
})
#cards just coins just one elelment, query
tests.append({
    'input': {
        'cards':[6],
        "query": 6
    },
    'output': 0
})

The problem statement does not specify what to do if the list cards does not contain the number query.

Read the problem statement again, carefully.

Look through the examples provided with the problem.

Ask the interviewer/platform for a clarification.

Make a reasonable assumption, state it and move forward.

We will assume that our function will return -1 in case cards does not contain query.

3. come up witha correct solution for the problem.

when you're solving a problem, you need to come up with a most efficient solution.
the simplest or most obvious solution to a problem after checking all possible answers is called BRUTE FORCE SOLUTION

solution for lesson 1-1 is simple
bob turns over a card one by one, untill he finds the card.

create a variable position with value of 0
check whether the number 

Create a variable position with the value 0.
Check whether the number at index position in card equals query.
If it does, position is the answer and can be returned from the function
If not, increment the value of position by 1, and repeat steps 2 to 5 till we reach the last position.
If the number was not found, return -1.

and this above is our first algorithm called Linear Search Algorithm
linear search algorithm : searching through a list in a linear fashion.

tip : always try to write and speak the algorithm, sometimes, you might not even understand what's going on, but by writing and speaking you'll be able to understand the problem, and may result in solving the problem.

4. implement the solution and t est it using example inputs

