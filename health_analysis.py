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
        eligiblity = "you are eligible for Medicare."
    elif age >= 65 and disability == "no":
        eligibility = "you are eligible for Medicare."
    elif age <65 and disability == "yes": 
        eligibility = "you may be eligible for Medicare."
    else: 
        eligibility = "you are not eligibe for Medicare."
    return eligibility 

Citizens = [
    [64,"yes"],
    [70, "no"],
    [40, "no"],
    [22, "yes"],
    [65, "no"]
]





    """ print("Your age:", age)
        print("According to Medicare guidelines, you are eligible to receive Medicare.")
    elif age >= 65 and disability == "no":
        print("Your age:", age)
        print("According to Medicare guidelines, you are eligible to receive Medicare.")
    elif age <65 and disability == "yes": 
        print("Your age:", age)
        print("According to Medicare guidelines, you may be eligible to receive Medicare.")
    else: 
        print("Your age:", age)
        print("According to Medicare guidelines, you are not eligible to receive Medicare.") 
"""







