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
        """
        Adds the given valid IP

        :param ip: An Ip as String
        :returns: True for every new addition
        :raises  :class:`ip_model.Exceptions.InvalidIpException` for invalid IP
        """
        ipObject = self.__ip_decider(ip)
        return ipObject.add(ip)

    def remove(self, ip: str):
        """
        Removed the given valid IP

        :param ip: An Ip as String
        :returns: str: The IP which is removed
        :raises  :class:`ip_model.Exceptions.InvalidIpException` for invalid IP
        """
        ipObject = self.__ip_decider(ip)
        return ipObject.remove(ip)

    def is_present(self, ip: str):
        """
        Checks if a given valid IP is present or not

        :param ip: An Ip as String
        :returns: True, if the element is present
                  False, if the element is not present
        :raises  :class:`ip_model.Exceptions.InvalidIpException` for invalid IP
        """
        ipObject = self.__ip_decider(ip)
        return ipObject.is_present(ip)

    def add_cidr(self, cidr: str):
        """
        Adds the given valid IP CIDR

        :param cidr: String in CIDR notation
        :return: True
        :raises  :class:`ip_model.Exceptions.InvalidIpException` for invalid IP CIDR
        """
        ipObject = self.__cidr_decider(cidr)
        return ipObject.add_cidr(cidr)

    def remove_cidr(self, cidr: str):
        """
        Removes the given valid IP CIDR

        :param cidr: String in CIDR notation
        :return: str: CIDR range which is removed
        :raises  :class:`ip_model.Exceptions.InvalidIpException` for invalid IP CIDR
        """
        ipObject = self.__cidr_decider(cidr)
        return ipObject.remove_cidr(cidr)
