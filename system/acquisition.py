
# Get signals
import json
import requests
import os

def from_fhir(url, device, dataset):

    # Recogemos los datos del servidor fhir
    r = requests.get(url + 'observation?device=' + device + '&date=' + dataset)

    if r.status_code == 200:

        # Trabajamos con ASCII, no podremos utilizar tildes
        data = r.text.encode('ascii', 'ignore')
        data = data.replace("\'", '\"')
        data = data.replace('u\"', '\"')
        aux = json.loads(data)

        # Construyo la estructura
        signalsData = []
        for element in aux['entry']:
            name = element['resource']['subject']['reference']
            period = element['resource']['valueSampledData']['period']
            data = element['resource']['valueSampledData']['data']
            data = map(float, data.split(' '))

            signalData = {'name': name, 'fs': 1/period, 'rawSignal': data}
            signalsData.append(signalData)

        return signalsData

    else:
        return None


def from_file(location, device, dataset, start=0, end=None):

    # TODO Por alguna razon el 'period' vale 0 en los recursos de nonin y berry asi que no puedo cargarlo directamente
    if device == 'prrb':
        period = 1/float(300)
    elif device == 'nonin':
        period = 1/float(75)
    elif device == 'berry':
        period = 1/float(100)
    else:
        print("Unsupported device")
        exit(0)
    path = location + '/' + device + '/' + dataset

    signalsData = []
    for file_name in os.listdir(path):
        with open(path + '/' + file_name, 'r') as f:

            resource = json.loads(f.read())

            name = resource['subject']['display']
            #period = resource['valueSampledData']['period']
            fs = 1 / period
            data = resource['valueSampledData']['data']
            data = map(float, data.split(' '))

            data = data[int(round(start*fs)):None] if not(end) else data[int(round(start*fs)):int(round(end*fs))]
            signalData = {'name': name, 'fs': fs, 'rawSignal': data}
            signalsData.append(signalData)

    return signalsData

