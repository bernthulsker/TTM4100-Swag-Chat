# -*- coding: utf-8 -*-
import SocketServer
import json
import re
import time

"""
Variables and functions that must be used by all the ClientHandler objects
must be written here (e.g. a dictionary for connected clients)
"""

class ClientHandler(SocketServer.BaseRequestHandler):
	"""
	This is the ClientHandler class. Everytime a new client connects to the
	server, a new ClientHandler object will be created. This class represents
	only connected clients, and not the server itself. If you want to write
	logic for the server, you must write it outside this class
	"""

	def handle(self):
		"""
		This method handles the connection between a client and the server.
		"""
		self.ip = self.client_address[0]
		self.port = self.client_address[1]
		self.connection = self.request
		self.username = None


		# Loop that listens for messages from the client
		while True:
			recieved_json = self.connection.recv(4096)

			recieved = json.loads(recieved_json)

			if (recieved['request'] == 'login') and (recieved['content'] is not None):
				self.login( recieved['content'])
				
			elif recieved['request'] == 'help':
				self.help()
			elif recieved['request'] == 'logout':
				if self.username is not None:
					self.logout()
				else:
					self.error("Not logged in.")

			elif recieved['request'] == 'msg':
				if self.username is not None:
					self.send_message(recieved['content'])
				else:
					self.error("Not logged in.")

			elif recieved['request'] == 'names':
				if self.username is not None:
					self.names()
				else:
					self.error("Not logged in.")

			else:
				self.error("The request is not supported.")

	def login(self, username):
		if not re.match('[A-Za-z0-9_-]+$', username):
			self.error("Username not valid")
		elif self.username is not None:
			self.error('Already logged in')
		elif self.user_connected(username):
			self.error("Username already taken")
		else:
			self.username = username
			print (username + " logged in.")
			server.connected_clients.append(self)
			self.send_response( "Server", "info", "Login sccuessful")
			self.history()

	def logout(self):
		self.send_response('Server', 'info', "logout successful")
		self.username = None
		if self in server.connected_clients:
			server.connected_clients.remove(self)


	def names (self):
		names = ""
		for user in server.connected_clients:
			if user.username is not None:
				names += user.username + ", "
		self.send_response( 'Server', 'info', names)

	def help(self):
		self.send_response( 'Server', 'info', "Available commands: login <username>, logout, msg <message>, names, help")

	def history(self):
		history = []
		for message in server.chat_history:
			history.append(message)
		self.send_response( 'Server', 'history', history)

	def error(self, content):

		self.send_response('Server', 'error', content)

	def send_message(self, content):
		for user in server.connected_clients:
			user.send_response(self.username, 'message', content)

	def send_response(self, sender, response, content):
		reply = {"timestamp": time.asctime(time.localtime(time.time())), "sender": sender, "response": response, "content": content}
		reply_json = json.dumps(reply)
		self.connection.send(reply_json.encode())

		if response == 'message' and reply not in server.chat_history:
			server.chat_history.append(reply_json)

	def user_connected(self, username):
		for user in server.connected_clients:
			if user.username == username:
				return True
		return False


class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
	"""
	This class is present so that each client connected will be ran as a own
	thread. In that way, all clients will be served by the server.

	No alterations are necessary
	"""
	allow_reuse_address = True
	connected_clients = []
	chat_history = []

if __name__ == '__main__':

	"""
	This is the main method and is executed when you type 'python Server.py'
	in your terminal.

	No alterations are necessary
	"""

	HOST = 'localhost'
	PORT = 9998
	print 'Server running...'

	# Set up and initiate the TCP server
	server = ThreadedTCPServer((HOST, PORT), ClientHandler)
	server.serve_forever()
