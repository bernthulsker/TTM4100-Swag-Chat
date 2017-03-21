# -*- coding: utf-8 -*-
import socket
from MessageReceiver import MessageReceiver
from MessageParser import MessageParser

class Client:
    def __init__(self, host, server_port):
        """
        This method is run when creating a new Client object
        """

        # Set up the socket connection to the server
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # TODO: Finish init process with necessary code
        self.run()

    def run(self):
        # Initiate the connection to the server
        self.connection.connect((self.host, self.server_port))

        while (1):
            new_payload = take_input(self)

            if payload['request'] == 'disconnect':
                self.disconnect()
                exit()

            send_payload(json.dumps(new_payload))
            
        
    def disconnect(self):
        self.connection.close()

    def receive_message(self, message):
        # TODO: Handle incoming message
        pass

    def send_payload(self, data):
        self.connection.send(data)
        
    def take_input(self):
        payload = {}
        payload['request'] = input('Enter request:')
        payload['content'] = input('Enter content:')

        return payload
    # More methods may be needed!


if __name__ == '__main__':
    """
    This is the main method and is executed when you type "python Client.py"
    in your terminal.

    No alterations are necessary
    """
    client = Client('localhost', 9998)
