import json



class MessageParser():
    def __init__(self):

        self.possible_responses = {
            'error': self.parse_error,
            'info': self.parse_info,
            'message': self.parse_message,
            'history': self.parse_history,
	    # More key:values pairs are needed	
        }

    def parse(self, payload):
        payload = json.loads(payload)

        if payload['response'] in self.possible_responses:
            return self.possible_responses[payload['response']](payload)
        else:
            return "error. Non-valid response from server"
            

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
