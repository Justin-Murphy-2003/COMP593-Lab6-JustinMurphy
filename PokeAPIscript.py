from http import client
import requests

def main():
    response = requests.head('https://jsonplaceholder.typicode.com/')

    if response.status_code == 200:
        print('Response:',response.status_code, '🎉🎉🎉', '\n')
    else:
        print('Uh Oh, got',response.status_code)

    print(response.headers)

main()