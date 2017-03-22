# -*- coding: utf-8 -*-
import socket
import json
from MessageReceiver import MessageReceiver
from MessageParser import MessageParser
from threading import Thread


class Client:
    def __init__(self, host, server_port):
        self.host = host
        self.server_port = server_port
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
        self.thread = MessageReceiver(self, self.connection)
        self.thread.start()

        while (1):
            new_payload = self.take_input()
            print new_payload

            if new_payload['request'] == 'disconnect':
                self.disconnect()
                exit()

            self.send_payload(json.dumps(new_payload))

        
    def disconnect(self):
        self.connection.close()

    def receive_message(self, message):
        msg_parser = MessageParser()

        print msg_parser.parse(message)

    def send_payload(self, data):
        self.connection.send(data)
        
    def take_input(self):
        payload = {}
        payload['request'] = raw_input('Enter request:')

        if payload['request'] == "login" or payload['request']=="message":
            payload['content'] = raw_input('Enter content:')

        return payload
    # More methods may be needed!


if __name__ == '__main__':
    dummy = {}


    """
    This is the main method and is executed when you type "python Client.py"
    in your terminal.

    No alterations are necessary
    """
    client = Client('localhost', 9998)
