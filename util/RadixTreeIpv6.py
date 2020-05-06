"""
@Copyrights 2020 Rakesh Kumar T
github: rakesht2499
"""


class RadixTreeIpv6:
    def __init__(self, data, children=[None] * 10):
        self.data = data
        self.children = children

    def add(self, ip):
        return self._add_ip(ip)

    def _add_ip(self, ip):
        i = 0
        while i < len(ip):
            flag = False
            if len(self.data) > 1:
                for j, y in enumerate(self.data):
                    if y == ip[i + j - 1]:
                        continue
                    else:
                        split_node = RadixTreeIpv6(self.data[j:], self.children)
                        index = int(ip[i + j - 1])
                        opp_index = int(self.data[j])
                        self.children = [None] * 10
                        self.children[opp_index] = split_node
                        self.data = self.data[:j]
                        self.children[index] = RadixTreeIpv6(ip[i + j - 1:])
                        flag = True
                        break
                i += j
                if i == len(ip) or flag:
                    break
            child = int(ip[i])
            if self.children[child] is None:
                self.children[child] = RadixTreeIpv6(ip[i:])
                flag = True
                break
            self = self.children[int(ip[i])]
            i += 1
        return flag

    def remove(self, ip) -> bool:
        self._remove_ip("N"+ip)

    def _remove_ip(self, ip):
        i = 0
        prev_node = []
        while i < len(ip):
            if len(self.data) == 1:
                if ip[i] != self.data:
                    return False
            elif len(self.data) > 1:
                for j, bit in enumerate(self.data):
                    if ip[i + j] == bit:
                        continue
                    else:
                        return
                i += j
            if i == len(ip)-1:
                prev_node[0].children[prev_node[1]] = None
                return
            prev_node = [self, int(ip[i + 1])]
            if self.children[int(ip[i + 1])]:
                self = self.children[int(ip[i + 1])]
            else:
                return
            i += 1

    def is_present(self, ip) -> bool:
        return self._check_data("N"+ip)

    def _check_data(self, ip):
        i = 0
        # We iterate till 32 as we need to exclude the root node
        while i < len(ip):
            if len(self.data) == 1:
                if ip[i] != self.data:
                    return False
            elif len(self.data) > 1:
                for j, bit in enumerate(self.data):
                    if ip[i + j] != bit:
                        return False
                i += j
            if i == len(ip)-1:
                return True
            if self.children[int(ip[i+1])]:
                self = self.children[int(ip[i+1])]
            else:
                return False
            i += 1
        return True
