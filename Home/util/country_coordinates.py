import requests

class CountryCoordinates():
    def getCoordinates(country, output_as='center'):
        url = '{0}{1}{2}'.format('http://nominatim.openstreetmap.org/search?country=',country,'&format=json&polygon=0')
        response = requests.get(url).json()[0]
        if output_as == 'boundingbox':
            lst = response[output_as]
            output = [float(i) for i in lst]
        if output_as == 'center':
            lst = [response.get(key) for key in ['lat','lon']]
            output = [float(i) for i in lst]
        return output
