import requests
import json

myToken = {'token':'1affd2045f325a53eece718f96429a70'}
r = requests.post('http://challenge.code2040.org/api/prefix', data=myToken)
data = r.json()

print r.text
prefix = data["prefix"]
stringArray = data["array"]

print prefix

newArray = []

for strings in stringArray:
    if not strings.startswith(prefix):
        newArray.append(strings)

print newArray

jsonReturn = {'token':'1affd2045f325a53eece718f96429a70',
    'array': newArray}

validate = requests.post('http://challenge.code2040.org/api/prefix/validate',
    json=jsonReturn)

print validate.text
