class Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def _add_left(self, data):
        self.left = Tree(data)

    def _add_right(self, data):
        self.right = Tree(data)

    def print_data(self):
        print(self.data, end=" ")
        if self.left:
            print("{}-L-".format(self.data), end="")
            self.left.print_data()
        if self.right:
            print("{}-R-".format(self.data), end="")
            self.right.print_data()

    def add(self, ip):
        i = 0
        while i < len(ip):
            flag = False
            if len(self.data) > 1:
                for j, y in enumerate(self.data):
                    if y == ip[i+j-1]:
                        continue
                    else:
                        if ip[i+j-1] == "0":
                            temp = Tree(self.data[j:])
                            temp.left = self.left
                            temp.right = self.right
                            self.right = temp
                            self.data = self.data[:j]
                            self._add_left(ip[i+j-1:])
                            flag = True
                            break
                        else:
                            temp = Tree(self.data[j:])
                            temp.left = self.left
                            temp.right = self.right
                            self.left = temp
                            self.data = self.data[:j]
                            self._add_right(ip[i+j-1:])
                            flag = True
                            break
                if flag:
                    break
                if ip[i] == "0":
                    self = self.left
                else:
                    self = self.right
                i += j
            else:
                if ip[i] == "0":
                    if self.left is None:
                        self._add_left(ip[i:])
                        break
                    self = self.left
                else:
                    if self.right is None:
                        self._add_right(ip[i:])
                        break
                    self = self.right
            i += 1

    def check_data(self, data):
        if len(data) == 1:
            return True
        if data[1] == "0":
            if self.left:
                return self.left.check_data(data[1:])
            else:
                return False
        elif data[1] == "1":
            if self.right:
                return self.right.check_data(data[1:])
            else:
                return False


def get_binary_ip(ip):
    binary_ip = ""
    for x in ip.split("."):
        binary_ip += f'{int(x):08b}'
    return binary_ip


if __name__ == "__main__":
    tree = Tree("N")
    ip = get_binary_ip("192.168.0.152")
    ip2 = get_binary_ip("192.168.0.153")
    ip3 = get_binary_ip("192.168.0.154")
    ip4 = get_binary_ip("192.168.0.155")
    ip5 = get_binary_ip("192.168.128.155")

    tree.add(ip)
    tree.print_data()

    tree.add(ip2)
    tree.print_data()

    tree.add(ip3)
    tree.print_data()

    tree.add(ip4)
    tree.print_data()

    tree.add(ip5)
    tree.print_data()
