import requests

myToken = {'token':'1affd2045f325a53eece718f96429a70'}
r = requests.post('http://challenge.code2040.org/api/reverse', params=myToken)

print (r.text)

reversedString = r.text[::-1]

jsonReturn = {'token':'1affd2045f325a53eece718f96429a70',
    'string': reversedString}

r = requests.post ('http://challenge.code2040.org/api/reverse/validate',
    params=jsonReturn)

print (reversedString)
