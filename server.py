import socket
import pymysql

# Establish a connection to the MySQL server
conn = pymysql.connect(user='root', password='Fairie072315!',
                       host='127.0.0.1',
                       database='STORE')

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Set up the server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 8000))
server_socket.listen()

# Wait for a client to connect
client_socket, client_address = server_socket.accept()
print('Connected to', client_address)

# Receive data from the client and execute a SQL query
while True:
    data = client_socket.recv(1024).decode()
    if not data:
        break
    cursor.execute(data)
    result = cursor.fetchall()
    client_socket.send(str(result).encode())

# Fetch the results
results = cursor.fetchall()

# Close the connection
cursor.close()
conn.close()
client_socket.close()
server_socket.close()
