"""
@Copyrights 2020 Rakesh Kumar T
github: rakesht2499
"""

from ip_model.util.Ipv6Tree import Ipv6Tree
from ip_model.util.Validator import Validator
from ipaddress import ip_address, ip_network

validate = Validator.validate_ipv6
validate_cidr = Validator.validate_cidr


class Ipv6:
    def __init__(self):
        self.head = Ipv6Tree()

    @validate
    def add(self, ip) -> bool:
        num_ip = self._to_num(ip)
        return self.head.add(num_ip)

    @validate
    def remove(self, ip) -> bool:
        num_ip = self._to_num(ip)
        self.head.remove(num_ip)

    @validate
    def is_present(self, ip) -> bool:
        num_ip = self._to_num(ip)
        return self.head.is_present(num_ip)

    @validate_cidr
    def add_cidr(self, cidr) -> bool:
        return self._insert_cidr(cidr)

    @validate_cidr
    def remove_cidr(self, cidr) -> bool:
        self._remove_cidr(cidr)

    def _insert_cidr(self, cidr):
        ins = True
        for ip in ip_network(cidr):
            ins = ins and self.add(str(ip))
        return ins

    def _remove_cidr(self, cidr):
        for ip in ip_network(cidr):
            self.remove(str(ip))

    def _to_num(self, ip):
        return str(int(ip_address(ip)))
