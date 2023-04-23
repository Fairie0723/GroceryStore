import socket

def Main():
    host = '192.168.1.80'
    port = 9980

    s = socket.socket()
    s.connect((host, port))

    print("[CONNECTED] Connected to {}:{}".format(host, port))

    cart = {}

    while True:
        item = input("Enter an item to purchase (or type 'done' to finish): ")
        if item.lower() == 'done':
            break
        s.send(item.encode())

        data = s.recv(1024).decode()
        if data == "Item not available":
            print(data)
        else:
            try:
                price = float(data)
                print("{} added to cart. Price: ${:.2f}".format(item, price))
                cart[item] = price
            except ValueError:
                print("Invalid response from server: {}".format(data))

    print("Items in cart:")
    total = 0
    for item, price in cart.items():
        print("- {}: ${:.2f}".format(item, price))
        total += price
    print("Total: ${:.2f}".format(total))

    s.close()
    print("[DISCONNECTED] Disconnected from the server.")

if __name__ == '__main__':
    Main()
