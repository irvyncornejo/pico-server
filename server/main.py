import umachine
import socket
from HTTP import Network
from config import ssid, password
from gpiopico import RaspiTemp
from handler_components import DashboardComponents

pico_temp_sensor = RaspiTemp()
components = DashboardComponents()

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
    address = (ip, 80)
    connection = socket.socket()
    connection.bind(address)
    connection.listen(1)
    return connection

def server(connection):
    #Start a web server
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
        client.close()

if __name__=='__main__':
    
    client = None
    
    try:
        http_wlan = Network(ssid, password)
        ip = http_wlan.ip
        components.run()
        socket_connection = open_socket(ip)
        server(socket_connection)
        
    
    except (KeyboardInterrupt) as err:
        print(err)


    finally:
        if client:
            client.close()
        if socket_connection:
            socket_connection.close()
        umachine.reset()
