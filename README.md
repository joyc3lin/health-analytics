# health-analytics
primer assignment for hha504/507

## variables explained 
There are 4 variables. A number variable named 'num', a string variable named 'word', a list variable named 'lis', and a dictionary named 'aboutBob'. 


### expected outputs of variables 
"""
100
pineapples are great
['this', 'is', 'a', 'list']
{'bob': 'the main character', 'age': 66, 'residence': 'apartment', 'jobs': ['dog walker', 'babysitter', 'president'], 'bobs_things': {'phone': 'iphone 14', 'clothes': ['shirt', 'suit', 'shoes', 'a sock'], 'money': 20.23}}
"""


## function explained 
The function seniorCitizen() determines whether a citizen is eligible for Medicare or not based on their inputted age and disability status. 

Their age is a number while their disability status can be noted with yes or no. 

Citizens are eligible for medicare if they are 65 or older. 
For those younger than 65, they may be eligible if they have a disability. 
For those that are not older than 65 and do not have any disabilites, they are not eligible for Medicare. 


### expected output of function based on example data
Example data: 
citizens = [
[64,"yes"],
[70, "no"],
[40, "no"],
[22, "yes"],
[65, "yes"]
]

Output: 
"""
Now reviewing your data: age: 64, disability: yes
According to Medicare: you may be eligible to recieve Medicare.




Now reviewing your data: age: 70, disability: no
According to Medicare: you are eligible to recieve Medicare.




Now reviewing your data: age: 40, disability: no
According to Medicare: you are not eligibe to recieve Medicare.




Now reviewing your data: age: 22, disability: yes
According to Medicare: you may be eligible to recieve Medicare.




Now reviewing your data: age: 65, disability: yes
According to Medicare: you are eligible to recieve Medicare.

"""