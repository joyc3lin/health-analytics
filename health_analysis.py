import pandas as pd
import numpy as np

num = 100
word = 'pineapples are great'
lis = ["this","is","a","list"]

aboutBob = {
    "bob" : "the main character",
    "age" : 66,
    "residence" : "apartment",
    "jobs" : ["dog walker", "babysitter","president"],
    "bobs_things": {
        "phone": "iphone 14",
        "clothes": ["shirt","suit","shoes","a sock"],
        "money" : 20.23
    }
}

def seniorCitizen(age, disability):
    if age >= 65 and disability == "yes":
        eligiblity = "you are eligible to recieve Medicare."
    elif age >= 65 and disability == "no":
        eligibility = "you are eligible to recieve Medicare."
    elif age <65 and disability == "yes": 
        eligibility = "you may be eligible to recieve Medicare."
    else: 
        eligibility = "you are not eligibe to recieve Medicare."
    return eligibility 

citizens = [
[64,"yes"],
[70, "no"],
[40, "no"],
[22, "yes"],
[65, "yes"]
]

for citizen in citizens:
    print('\n')
    print(f'Now reviewing your data: age: {citizen[0]}, disability: {citizen[1]}')
    
    """age = citizen[0]
    disability = citizen[1]
    outputFunction = seniorCitizen(age,disability)
    print(f'According to Medicare: {outputFunction}')
    print('\n')"""










