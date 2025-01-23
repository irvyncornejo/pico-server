from time import sleep
import network
import urequests


class HTTP:
    """
        Use Only with raspberry pi pico w
    """
    def __init__(self, ssid, password) -> None:
        self.ip = self._connect(ssid, password)
        self._response = None
        self._format = 'json'
    
    def _set_url(self, url:str):
        pass

    def _connect(self, ssid:str, password:str)->str:
        wlan = network.WLAN(network.STA_IF)
        wlan.active(True)
        wlan.connect(ssid, password)
        while wlan.isconnected() == False:
            print('Waiting for connection..')
            sleep(1)
        ip = wlan.ifconfig()[0]
        print(f'Connected on ip -> {ip}')
        return ip
            

    def _format_return(self):
        if self._format == 'json':
            return self._response.json()
        return self._response

    def get(self, url: str, format_response:str='json'):
        print(f'Get {url}')
        self._response = urequests.get(url)
        return self._format_return()
    
    def post(self):
        pass
    
