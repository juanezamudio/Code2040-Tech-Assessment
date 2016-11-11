# Author: © Juan Zamudio 2016
# Date: October 7, 2016
# Code2040-Tech-Assessment: Step Two
#
# Makes a POST request with personal API token to receive string
# to be reversed. String is then reversed and put into a JSON
# dictionary to be sent as POST request to the validation url
# that checks if the string has been reversed

import requests

# The API token
myToken = {'token':'1affd2045f325a53eece718f96429a70'}

# POST request to get string needed to be reversed
r = requests.post('http://challenge.code2040.org/api/reverse', params=myToken)

# Print the string needed to be reversed
print r.text

# Reverse the string
reversedString = r.text[::-1]

# JSON dictionary with token and reversed string
jsonReturn = {'token':'1affd2045f325a53eece718f96429a70',
    'string': reversedString}

# POST request to validate if string has been reversed
validate = requests.post ('http://challenge.code2040.org/api/reverse/validate',
    params=jsonReturn)

print reversedString # Print reversed string
print validate.text # Print validation reponse
