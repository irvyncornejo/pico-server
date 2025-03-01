import umachine
import socket
from gpiopico import Network
from config import ssid, password
from gpiopico import RaspiTemp
from dashboard import Dashboard
from components import Component

pico_temp_sensor = RaspiTemp()
dashboard = Dashboard(title='Demo Jam', component=Component)

"""class Server(Network):
    def __init__(self, ssid:str, password:str)->None:
        super().__init__(ssid:str, password:str)
    
    def _open_ip(self):
        address = (self.ip, 80)
        connection = socket.socket()
        connection.bind(address)
        connection.listen(1)
        return connection
    
    def start_server()->None:
        while True:
            client = connection.accept()[0]
            request = client.recv(1024)
            request = str(request)
        
            try:
                request = request.split()[1]
            
            except IndexError:
                pass

            components.process_requests(request) 
            temperature = pico_temp_sensor.read()
            html = components.show(temperature) #webpage(temperature)
            client.send(html)
            client.close()"""


def open_socket(ip):
    # Open a socket
    
    try:
        address = (ip, 80)
        connection = socket.socket()
        connection.bind(address)
        connection.listen(1)
        return connection
    except Exception as e:
        print(e)

def server(connection):
    #Start a web server
    while True:
        client = connection.accept()[0]
        request = client.recv(1024)
        
        try:
            print(request)
        except Exception as e:
            print(e)
        
        request = str(request)
 
        try:
            request = request.split()[1]
        except IndexError:
            pass

        dashboard.process_requests(request) 
        temperature = pico_temp_sensor.read()
        html = dashboard.show(temperature) #webpage(temperature)

        client.send("HTTP/1.1 200 OK\r\nContent-Type: text/html\r\nConnection: keep-alive\r\n\r\n")

        for i in range(0, len(html), 512):
            client.send(html[i:i+512])

        client.close()

if __name__=='__main__':
    
    client = None
    
    try:
        http_wlan = Network(ssid, password)
        ip = http_wlan.ip
        socket_connection = open_socket(ip)
        server(socket_connection)
        
    
    except (KeyboardInterrupt) as err:
        print(err)
        if socket_connection:
            socket_connection.close()
