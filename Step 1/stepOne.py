import requests
r = requests.post('http://challenge.code2040.org/api/register',
    data = {'token':'1affd2045f325a53eece718f96429a70',
        'github': 'https://github.com/juanezamudio/Code2040-Tech-Assessment.git'})
