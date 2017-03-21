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
            conntent = self.connection.recv(4096)
            if content:
                self.listener.recieve_message(content)