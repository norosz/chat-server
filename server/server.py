import socket
import threading

class Server:
    MAX_BUFF_SIZE = 1024
    def __init__(self, ip: str, port: int, sck: socket.socket = None)->None:
        self.__ip = ip
        self.__port = port
        self.__sck = sck
        self.__server_address = (self.ip, self.port)
        self.__connections = []

    @property
    def ip(self)-> str:
        return self.__ip
    @property
    def port(self)-> int:
        return self.__port
    @property
    def sck(self)-> socket:
        return self.__sck
    @property
    def server_address(self)-> socket:
        return self.__server_address

    def __accept_connection(self)-> None:
        """Accept connections with a socket"""
        while True:
            print(threading.get_ident())
            (client_socket, address) = self.__sck.accept()
            request = client_socket.recv(Server.MAX_BUFF_SIZE)
            print("Connected by", address)
            print("Request:", request)


    def start(self)-> None:
        """Start the server with the instance's ip and port"""
        self.__sck = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__sck.bind(self.server_address)
        self.__sck.listen()
        accept_socket_connections_thread = threading.Thread(target=self.__accept_connection)
        accept_socket_connections_thread.start()
        print("Server started...")


