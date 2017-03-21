from threading import Thread


class MessageReceiver(Thread):
    def __init__(self, client, connection):
        Thread.__init__(self)

        self.daemon = True
        self.client = client
        self.connection = connection


    def run(self):
        # TODO: Make MessageReceiver receive and handle payloads
        while(1):
            content = self.connection.recv(4096)
            if content:
                self.client.recieve_message(content)