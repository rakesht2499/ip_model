"""
@Copyrights 2020 Rakesh Kumar T
github: rakesht2499
"""


class RadixTree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.children = [left, right]

    # For development purpose alone
    def _print_data(self):
        print(self.data, end=" ")
        if self.children[0]:
            print("-L-", end="")
            self.children[0].print_data()
        if self.children[1]:
            print("-R-", end="")
            self.children[1].print_data()

    def add(self, ip):
        return self._add_ip(ip)

    def _add_ip(self, ip):
        i = 0
        flag = False
        while i < len(ip):
            if i == 0 and self.children[int(ip[0])] is None:
                self.children[int(ip[0])] = RadixTree(ip)
                flag = True
                break
            if len(self.data) > 1:
                for j, y in enumerate(self.data):
                    if y == ip[i+j-1]:
                        continue
                    else:
                        split_node = RadixTree(self.data[j:], self.children[0], self.children[1])
                        index = int(ip[i+j-1])
                        opp_index = int(not bool(index))
                        self.children[opp_index] = split_node
                        self.data = self.data[:j]
                        self.children[index] = RadixTree(ip[i+j-1:])
                        flag = True
                        break
                i += j
                """
                 * i becomes 32 is all the data is same, flag becomes true if the tree was split
                 * i becomes 32 & flag becomes true if there is a split in the last node
                """
                if i == 32 or flag:
                    return True
            self = self.children[int(ip[i])]
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
                prev_node[0].children[prev_node[1]] = None
                return
            prev_node = [self, int(ip[i+1])]
            if self.children[int(ip[i+1])]:
                self = self.children[int(ip[i+1])]
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
                    if ip[i+j] != bit:
                        return False
                i += j
            if i == 32:
                return True
            if self.children[int(ip[i+1])]:
                self = self.children[int(ip[i+1])]
            else:
                return False
            i += 1
        return True
