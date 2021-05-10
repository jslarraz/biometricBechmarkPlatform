
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


def from_file(location, device, dataset):

    path = location + '/' + device + '/' + dataset

    signalsData = []
    for file_name in os.listdir(path):
        with open(path + '/' + file_name, 'r') as f:

            resource = json.loads(f.read())

            name = resource['subject']['display']
            period = resource['valueSampledData']['period']
            data = resource['valueSampledData']['data']
            data = map(float, data.split(' '))

            signalData = {'name': name, 'fs': 1/period, 'rawSignal': data}
            signalsData.append(signalData)

    return signalsData
