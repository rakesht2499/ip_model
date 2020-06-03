from ipaddress import ip_address, IPv4Address, IPv4Network, ip_network
from ip_model.IpObject import IpObject
from ip_model.Ipv4 import Ipv4
from ip_model.Ipv6 import Ipv6


class Ip(IpObject):
    def __init__(self):
        self.ipv4 = Ipv4()
        self.ipv6 = Ipv6()

    def __ip_decider(self, ip):
        if isinstance(ip_address(ip), IPv4Address):
            return self.ipv4
        else:
            return self.ipv6

    def __cidr_decider(self, ip):
        if isinstance(ip_network(ip), IPv4Network):
            return self.ipv4
        else:
            return self.ipv6

    def add(self, ip: str):
        ipObject = self.__ip_decider(ip)
        return ipObject.add(ip)

    def remove(self, ip: str):
        ipObject = self.__ip_decider(ip)
        return ipObject.remove(ip)

    def is_present(self, ip: str):
        ipObject = self.__ip_decider(ip)
        return ipObject.is_present(ip)

    def add_cidr(self, cidr: str):
        ipObject = self.__cidr_decider(cidr)
        return ipObject.add_cidr(cidr)

    def remove_cidr(self, cidr: str):
        ipObject = self.__cidr_decider(cidr)
        return ipObject.remove_cidr(cidr)
