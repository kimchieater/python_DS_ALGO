#Problem 1 

def locate_card(cards, query):
    pass




test = {
    'input': {
        'cards' : {13,11,10,7,4,3,1,0},
        'query': 7
    },
    'output':3
}
tests = []
tests.append(test)

#query occurs in the middle
tests.append({
    'input': {
        'cards': [13,11,10,7,4,3,1,0],
        'query': 1
    },
    'output': 6
})

#query is the first element
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
#card does not contain query
tests.append({
    'input':{
        'cards': [9,7,5,2,-9],
        'query': 4
    },
    'output': -1
})
#card is empty
tests.append({
    'input':{
        'cards': [],
        'query': 7
    },
    'output': -1
})
#numbers can repeat in cards
tests.append({
    "input":{
        'cards':[8,8,6,6,6,6,6,3,2,2,2,0,0,0],
        'query': 3
    },
    "output": 7
})

print(tests)