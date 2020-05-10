"""
@Copyrights 2020 Rakesh Kumar T
github: rakesht2499
"""


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.children = [left, right]


class Ipv4Tree:
    def __init__(self):
        self.head = Node("N")

    # For development purpose alone
    def _print_data(self, head):
        print(head.data, end=" ")
        if head.children[0]:
            print("-L-", end="")
            self._print_data(head.children[0])
        if head.children[1]:
            print("-R-", end="")
            self._print_data(head.children[1])

    def add(self, ip):
        return self._add_ip(self.head, ip)

    def _add_ip(self, head, ip):
        i = 0
        flag = False
        while i < len(ip):
            if i == 0 and head.children[int(ip[0])] is None:
                head.children[int(ip[0])] = Node(ip)
                flag = True
                break
            if len(head.data) > 1:
                for j, y in enumerate(head.data):
                    if y == ip[i+j-1]:
                        continue
                    else:
                        split_node = Node(head.data[j:], head.children[0],head.children[1])
                        index = int(ip[i+j-1])
                        opp_index = int(not bool(index))
                        head.children[opp_index] = split_node
                        head.data = head.data[:j]
                        head.children[index] = Node(ip[i+j-1:])
                        flag = True
                        break
                i += j
                """
                 * i becomes 32 is all the data is same, flag becomes true if the tree was split
                 * i becomes 32 & flag becomes true if there is a split in the last node
                """
                if i == 32 or flag:
                    return True
            head = head.children[int(ip[i])]
            i += 1
        return flag

    def remove(self, ip) -> bool:
        self._remove_ip(self.head, "N" + ip)

    def _remove_ip(self, head, ip):
        i = 0
        prev_node = []
        # We iterate till 32 as we need to exclude the root node
        while i <= 32:
            if len(head.data) == 1:
                if ip[i] != head.data:
                    return False
            elif len(head.data) > 1:
                for j, bit in enumerate(head.data):
                    if ip[i+j] == bit:
                        continue
                    else:
                        return
                i += j
            if i == 32:
                prev_node[0].children[prev_node[1]] = None
                return
            prev_node = [head, int(ip[i+1])]
            if head.children[int(ip[i+1])]:
                head = head.children[int(ip[i+1])]
            else:
                return
            i += 1

    '''
    :argument ip, Accepts an IP as a string
    :return True, if element is present
            False, if not present
    '''
    def is_present(self, ip) -> bool:
        return self._check_data(self.head, "N" + ip)

    def _check_data(self, head, ip):
        i = 0
        # We iterate till 32 as we need to exclude the root node
        while i <= 32:
            if len(head.data) == 1:
                if ip[i] != head.data:
                    return False
            elif len(head.data) > 1:
                for j, bit in enumerate(head.data):
                    if ip[i+j] != bit:
                        return False
                i += j
            if i == 32:
                return True
            if head.children[int(ip[i+1])]:
                head = head.children[int(ip[i+1])]
            else:
                return False
            i += 1
        return True
