from http import client

def main():
    cxn = client.HTTPConnection('https://jsonplaceholder.typicode.com/', 443)
    cxn.request('HEAD', '/')
    response = cxn.getresponse()

    if response.status == 200:
        print('Response:',response.status, '🎉🎉🎉', '\n')
    else:
        print('Uh Oh, got',response.status)

    print(response.headers)

main()