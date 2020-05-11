"""
@Copyrights 2020 Rakesh Kumar T
github: rakesht2499
"""


class Node:
    def __init__(self, data, children=[None] * 10):
        self.data = data
        self.children = children


class Ipv6Tree:
    def __init__(self):
        self.head = Node("N")

    def add(self, ip):
        return self._add_ip(self.head, ip)

    def _add_ip(self, head, ip):
        i = 0
        while i <= 39:
            flag = False
            if len(head.data) > 1:
                for j, y in enumerate(head.data):
                    if y == ip[i + j - 1]:
                        continue
                    else:
                        split_node = Node(head.data[j:], head.children)
                        index = int(ip[i + j - 1])
                        opp_index = int(head.data[j])
                        head.children = [None] * 10
                        head.children[opp_index] = split_node
                        head.data = head.data[:j]
                        head.children[index] = Node(ip[i + j - 1:])
                        flag = True
                        break
                i += j
                if i == len(ip) or flag:
                    break
            child = int(ip[i])
            if head.children[child] is None:
                head.children[child] = Node(ip[i:])
                flag = True
                break
            head = head.children[int(ip[i])]
            i += 1
        return flag

    def remove(self, ip) -> bool:
        self._remove_ip(self.head, "N"+ip)

    def _remove_ip(self, head, ip):
        i = 0
        prev_node = []
        while i <= 39:
            if len(head.data) == 1:
                if ip[i] != head.data:
                    return False
            elif len(head.data) > 1:
                for j, bit in enumerate(head.data):
                    if ip[i + j] == bit:
                        continue
                    else:
                        return
                i += j
            if i == len(ip)-1:
                prev_node[0].children[prev_node[1]] = None
                return
            prev_node = [head, int(ip[i + 1])]
            if head.children[int(ip[i + 1])]:
                head = head.children[int(ip[i + 1])]
            else:
                return
            i += 1

    def is_present(self, ip) -> bool:
        return self._check_data(self.head, "N"+ip)

    def _check_data(self, head, ip):
        i = 0
        # We iterate till 32 as we need to exclude the root node
        while i <= 39:
            if len(head.data) == 1:
                if ip[i] != head.data:
                    return False
            elif len(head.data) > 1:
                for j, bit in enumerate(head.data):
                    if ip[i + j] != bit:
                        return False
                i += j
            if i == len(ip)-1:
                return True
            if head.children[int(ip[i+1])]:
                head = head.children[int(ip[i+1])]
            else:
                return False
            i += 1
        return True
