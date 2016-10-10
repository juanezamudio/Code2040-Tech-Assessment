import requests
import json


myToken = {'token':'1affd2045f325a53eece718f96429a70'}
r = requests.post('http://challenge.code2040.org/api/haystack', params=myToken)
data = r.json()

print (r.text)
needle = data["needle"]
haystack = data["haystack"]

index = 0
for hay in haystack:
    if hay == needle:
        print index
        print haystack[index]
        break
    else:
        index += 1

jsonReturn = {'token':'1affd2045f325a53eece718f96429a70',
    'needle': index}

validate = requests.post ('http://challenge.code2040.org/api/haystack/validate',
    params=jsonReturn)

print validate.text
