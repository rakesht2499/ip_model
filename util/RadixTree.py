"""
@Copyrights 2020 Rakesh Kumar T
author: Rakesh Kumar T
github: rakesht2499
"""

class RadixTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def _add_left(self, data):
        self.left = RadixTree(data)

    def _add_right(self, data):
        self.right = RadixTree(data)

    # For development purpose alone
    def _print_data(self):
        print(self.data, end=" ")
        if self.left:
            print("-L-",end="")
            self.left.print_data()
        if self.right:
            print("-R-",end="")
            self.right.print_data()

    def add(self, ip):
        return self._add_ip(ip)

    def _add_ip(self, ip):
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
                i += j
                if i == 32:
                    flag = True
                if flag:
                    break
                if ip[i] == "0":
                    self = self.left
                else:
                    self = self.right
            else:
                if ip[i] == "0":
                    if self.left is None:
                        self._add_left(ip[i:])
                        flag = True
                        break
                    self = self.left
                else:
                    if self.right is None:
                        self._add_right(ip[i:])
                        flag = True
                        break
                    self = self.right
            i += 1
        return flag

    def remove(self, ip) -> bool:
        self._remove_ip("N" + ip)

    def _remove_ip(self, ip):
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
                        return
                i += j
            if i == 32:
                if prev_node[1] == "L":
                    prev_node[0].left = None
                else:
                    prev_node[0].right = None
                return
            if ip[i + 1] == "0":
                prev_node = [self, "L"]
                if self.left:
                    self = self.left
                else:
                    return
            else:
                prev_node = [self, "R"]
                if self.right:
                    self = self.right
                else:
                    return
            i += 1

    '''
    :argument ip, Accepts an IP as a string
    :return True, if element is present
            False, if not present
    '''
    def is_present(self, ip) -> bool:
        return self._check_data("N" + ip)

    def _check_data(self, ip):
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

