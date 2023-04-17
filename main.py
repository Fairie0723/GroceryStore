import socket

# Set up the client socket and connect to the server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 8000))

# Send a SQL query to the server and receive the result
query = input('Enter a SQL query: ')
client_socket.send(query.encode())
result = client_socket.recv(1024).decode()
print(result)

# Clean up
client_socket.close()
