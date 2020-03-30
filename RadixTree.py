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
        print(self.data, end="")
        if self.left:
            self.left.print_data()
        if self.right:
            self.right.print_data()

    def add(self, ip):
        for x in ip:
            if x == "0":
                if self.left is None:
                    self._add_left(x)
                self = self.left
            else:
                if self.right is None:
                    self._add_right(x)
                self = self.right

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
    ip = get_binary_ip("192.168.0.153")
    ip2 = get_binary_ip("192.168.0.152")
    ip3 = get_binary_ip("192.168.0.155")
    ip4 = get_binary_ip("192.168.0.154")

    tree.add(ip)

    print(tree.check_data("N"+ip))
    print(tree.check_data("N"+ip2))

    temp = tree
    tree.add(ip2)
    print(tree.check_data("N"+ip))
    print(tree.check_data("N"+ip2))
    print(tree.check_data("N"+ip3))
    print(tree.check_data("N"+ip4))
