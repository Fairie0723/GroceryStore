import socket
import threading

host = 'localhost'
port = 9999


def handle_client(conn, addr):
    connected = True
    # read the item list from a file
    with open("items.txt", "r") as f:
        items = dict(line.strip().split(", ") for line in f)
    # create a dictionary to hold the prices for each item
    prices = {}
    for item, price in items.items():
        prices[item] = float(price)
    # receive items from the client
    while connected:
        data = conn.recv(1024).decode()
        if data == "done":
            connected = False
            continue

        if data in prices:
            price = prices[data]
            if price == 0.0:
                response = "Item not available"
            else:
                response = str(price)
                prices[data] = 0.0
        else:
            response = "Invalid item"
        conn.send(response.encode())

    # calculate the total cost and send it to the client
    total = sum(prices.values())
    response = "Items in cart:\n"
    for item, price in prices.items():
        if price > 0.0:
            response += "- {}: ${:.2f}\n".format(item, price)
    response += "Total: ${:.2f}".format(total)
    conn.send(response.encode())

    # close the connection
    print("[DISCONNECTED] Disconnected by {}:{}".format(addr[0], addr[1]))
    conn.close()


def main():
    # set up the socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen()

    print("[LISTENING] Server is listening on {}:{}".format(host, port))

    # accept connections from clients
    while True:
        conn, addr = s.accept()
        print("[CONNECTED] Connected by {}:{}".format(addr[0], addr[1]))
        thread = threading.Thread(target=handle_client, args=(conn, addr))  # create a new thread
        thread.start()  # start the thread
    s.close()


if __name__ == "__main__":
    main()
