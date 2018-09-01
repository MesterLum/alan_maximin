from utils.process import Process
import requests

class Test:
    
    @staticmethod
    def check_api(data):     
        url = 'localhost'
        port = 8000
        headers = {'Content-type': 'application/json'}
        response = requests.post('{}:{}/maximin'.format(url,port),
                        headers=headers,
                        data=data)

