import requests

def gencode(address):
    parameters = {'address': address, 'semsor': 'false'}
    base = 'http://maps.googleapis.com/maps/api/gencode/json'
    response = requests.get(base, params=parameters)
    answer = response.json()
    print(answer['results'][0]['geometry']['location'])

if __name__ == '__main__':
    gencode('207 N. Defiance St, Archbold, OH')