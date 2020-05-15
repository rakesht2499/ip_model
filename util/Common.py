from ipaddress import ip_address, ip_network, IPv4Address

def to_number(ip):
    if isinstance(ip_address(ip), IPv4Address):
        padding_len = 10
    else:
        padding_len = 39
    return str(int(ip_address(ip))).rjust(padding_len, "0")


class Common:
    def _insert_cidr(self, cidr) -> bool:
        ins = True
        for ip in ip_network(cidr):
            ins = ins and self.add(str(ip))
        return ins

    def _remove_cidr(self, cidr) -> bool:
        for ip in ip_network(cidr):
            self.remove(str(ip))
