import socket

host = 'localhost'
port = 9999


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    print("[CONNECTED] Connected to {}:{}".format(host, port))

    cart = {}
    print("====================================================")
    print("====================================================")
    print("======                                         =====")
    print("======  WELCOME TO THE ONLINE GROCERY STORE    =====")
    print("======                                         =====")
    print("====================================================")
    print("====================================================")
    print("Please begin your order..."
          "\nType 'done' to finish your order...")

    while True:
        item = input("Item: ")

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
                print("Item not available")
    s.send("done".encode())
    print("===== Items in cart =====")
    total = 0
    for item, price in cart.items():
        print("----- {}: ${:.2f}".format(item, price))
        total += price
    print("=========================")
    print("     Total: ${:.2f}".format(total))

    print("\n==================================================")
    print("THANK YOU FOR SHOPPING WITH US! COME AGAIN SOON!")
    print("==================================================")

    print("[DISCONNECTED]")
    # s.close()


if __name__ == '__main__':
    main()
