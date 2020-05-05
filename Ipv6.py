"""
@Copyrights 2020 Rakesh Kumar T
github: rakesht2499
"""

from ip_model.util.RadixTreeIpv6 import RadixTreeIpv6
from ip_model.util.Validator import Validator
from ipaddress import ip_address

validate = Validator.validateIpv6


class Ipv4:
    def __init__(self):
        self.head = RadixTreeIpv6("N")

    @validate
    def add(self, ip) -> bool:
        bin_ip = self._to_num(ip)
        return self.head.add(bin_ip)

    @validate
    def remove(self, ip) -> bool:
        bin_ip = self._to_num(ip)
        return self.head.remove(bin_ip)

    @validate
    def is_present(self, ip) -> bool:
        bin_ip = self._to_num(ip)
        return self.head.is_present(bin_ip)

    def _to_num(self, ip):
        return int(ip_address(ip))
