class RadixTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def _add_left(self, data):
        self.left = RadixTree(data)

    def _add_right(self, data):
        self.right = RadixTree(data)

    def print_data(self):
        print(self.data, end=" ")
        if self.left:
            self.left.print_data()
        if self.right:
            self.right.print_data()

    def _verify(self, ip):
        valid_len = False
        valid_ip = False
        if len(ip.split(".")) == 4:
            valid_len = True
        if valid_len:
            binary_ip = self._to_binary(ip)
            if len(binary_ip) == 32:
                valid_ip = True
        return valid_ip and valid_len

    def add_ip(self, ip):
        self._verify(ip)
        self._add(ip)

    def _add(self, ip):
        i = 0
        while i < len(ip):
            flag = False
            if len(self.data) > 1:
                for j, y in enumerate(self.data):
                    if y == ip[i+j-1]:
                        continue
                    else:
                        if ip[i+j-1] == "0":
                            split_node = RadixTree(self.data[j:])
                            split_node.left = self.left
                            split_node.right = self.right
                            self.right = split_node
                            self.data = self.data[:j]
                            self._add_left(ip[i+j-1:])
                            flag = True
                            break
                        else:
                            split_node = RadixTree(self.data[j:])
                            split_node.left = self.left
                            split_node.right = self.right
                            self.left = split_node
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

    def remove(self, ip):
        self._verify(ip)
        i = 0
        prev_node = []
        # We iterate till 32 as we need to exclude the root node
        while i <= 32:
            if len(self.data) == 1:
                if ip[i] != self.data:
                    return False
            elif len(self.data) > 1:
                for j, bit in enumerate(self.data):
                    if ip[i+j] == bit:
                        continue
                    else:
                        return False
                i += j
            if i == 32:
                if prev_node[1] == "L":
                    prev_node[0].left = None
                else:
                    prev_node[0].right = None
                return True
            if ip[i + 1] == "0":
                prev_node = [self, "L"]
                if self.left:
                    self = self.left
                else:
                    return False
            else:
                prev_node = [self, "R"]
                if self.right:
                    self = self.right
                else:
                    return False
            i += 1

    def check_data(self, ip):
        i = 0
        # We iterate till 32 as we need to exclude the root node
        while i <= 32:
            if len(self.data) == 1:
                if ip[i] != self.data:
                    return False
            elif len(self.data) > 1:
                for j, bit in enumerate(self.data):
                    if ip[i+j] == bit:
                        continue
                    else:
                        return False
                i += j
            if i == 32:
                return True
            if ip[i + 1] == "0":
                if self.left:
                    self = self.left
                else:
                    return False
            else:
                if self.right:
                    self = self.right
                else:
                    return False
            i += 1
        return True

    def _to_binary(self, ip):
        binary_ip = ""
        for x in ip.split("."):
            binary_ip += f'{int(x):08b}'
        return binary_ip


if __name__ == "__main__":
    tree = RadixTree("N")
    ip = "192.168.0.152"
    ip2 = "192.168.0.153"
    ip3 = "192.168.0.154"
    ip4 = "192.168.0.155"
    ip5 = "192.168.128.155"
    ip6 = "192.168.128.127"

    tree.add_ip(ip)
    tree.print_data()
    print(tree.check_data("N"+ip))
    print(tree.check_data("N"+ip2))

    tree.add_ip(ip2)
    tree.print_data()
    print(tree.check_data("N" + ip))
    print(tree.check_data("N" + ip2))
    print(tree.check_data("N" + ip3))

    tree.add_ip(ip3)
    tree.print_data()
    print(tree.check_data("N"+ip))
    print(tree.check_data("N"+ip2))
    print(tree.check_data("N"+ip3))
    print(tree.check_data("N"+ip4))

    tree.add_ip(ip4)
    tree.print_data()
    print(tree.check_data("N"+ip))
    print(tree.check_data("N"+ip2))
    print(tree.check_data("N"+ip3))
    print(tree.check_data("N"+ip4))
    print(tree.check_data("N"+ip5))

    tree.add_ip(ip5)
    tree.print_data()
    print(tree.check_data("N"+ip))
    print(tree.check_data("N"+ip2))
    print(tree.check_data("N"+ip3))
    print(tree.check_data("N"+ip4))
    print(tree.check_data("N"+ip5))

    print("Removal", tree.remove("N" + ip3))
    print("Removal", tree.remove("N" + ip5))
    print("Removal", tree.remove("N" + ip6))
    tree.print_data()
    print(tree.check_data("N" + ip))
    print(tree.check_data("N" + ip2))
    print(tree.check_data("N" + ip3))
    print(tree.check_data("N" + ip4))
    print(tree.check_data("N" + ip5))
