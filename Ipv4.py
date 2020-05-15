"""
@Copyrights 2020 Rakesh Kumar T
github: rakesht2499
"""

from ip_model.util.Common import Common
from ip_model.util.IpTree import IpTree
from ip_model.util.Validator import Validator
from ip_model.util.Common import to_number

validate = Validator.validate
validate_cidr = Validator.validate_cidr


class Ipv4(Common):
    def __init__(self):
        self.head = IpTree()

    @validate
    def add(self, ip) -> bool:
        num_ip = to_number(ip)
        return self.head.add(num_ip)

    @validate_cidr
    def add_cidr(self, cidr) -> bool:
        return self._insert_cidr(cidr)

    @validate
    def remove(self, ip) -> bool:
        num_ip = to_number(ip)
        self.head.remove(num_ip)

    @validate_cidr
    def remove_cidr(self, cidr) -> bool:
        self._remove_cidr(cidr)

    @validate
    def is_present(self, ip) -> bool:
        num_ip = to_number(ip)
        return self.head.is_present(num_ip)
