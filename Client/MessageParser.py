import json



class MessageParser():
    def __init__(self):

        self.possible_responses = {
            'Error': self.parse_error,
            'Info': self.parse_info,
            'Message': self.parse_message,
            'History': self.parse_history,
	    # More key:values pairs are needed	
        }

    def parse(self, payload):
        payload = json.loads(payload)

        if payload['response'] in self.possible_responses:
            return self.possible_responses[payload['response']](payload)
        else:
            return "Error. Non-valid response from server"
            

    def parse_error(self, payload):
        dummy = str(payload['timestamp']) + "\n"
        dummy += "Sender: " + payload['sender'] + "\n"
        dummy += "Response: " + payload['response'] + "\n"
        dummy += payload['content'] + "\n"
        return dummy
    
    def parse_info(self, payload):
        dummy = str(payload['timestamp']) + "\n"
        dummy += "Sender: " + payload['sender'] + "\n"
        dummy += "Response: " + payload['response'] + "\n"
        dummy += payload['content'] + "\n"
        return dummy

    def parse_message(self,payload):
        dummy = str(payload['timestamp']) + "\n"
        dummy += "Sender: " + payload['sender'] + "\n"
        #dummy += "Response: " + payload['response'] + "\n"
        dummy += payload['content'] + "\n"
        return dummy

    def parse_history(self, payload):
        dummy = str(payload['timestamp']) + "\n"
        dummy += "Sender: " + payload['sender'] + "\n"
        dummy += "Response: " + payload['response'] + "\n"
        for word in payload['content']:
            dummy += self.parse_message(json.loads(word)) + '\n'
        return dummy

    
    # Include more methods for handling the different responses... 
