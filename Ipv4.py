"""
@Copyrights 2020 Rakesh Kumar T
github: rakesht2499
"""
from ip_model.IpObject import IpObject
from ip_model.util.IpTree import IpTree
from ip_model.util.Validator import Validator
from ip_model.util.Common import to_number

validate = Validator.validate
validate_cidr = Validator.validate_cidr


class Ipv4(IpObject):
    def __init__(self):
        """
        Creates an object of :class:`ip_model.util.IpTree.IpTree`
        """
        self.head = IpTree()


    @validate
    def add(self, ip: str) -> bool:
        """
        Adds the given valid IPv4

        :param ip: An Ipv4 as String
        :returns: True for every new addition
        :raises  :class:`ip_model.Exceptions.InvalidIpException` for invalid IPv4
        """
        num_ip = to_number(ip)
        self.head.add(num_ip)
        return True

    @validate_cidr
    def add_cidr(self, cidr) -> bool:
        """
        Adds the given valid IPv4 CIDR

        :param cidr: String in CIDR notation
        :return: True
        :raises  :class:`ip_model.Exceptions.InvalidIpException` for invalid IPv4 CIDR
        """
        return self._insert_cidr(cidr)


    @validate
    def remove(self, ip) -> bool:
        """
        Removed the given valid IPv4

        :param ip: An Ipv4 as String
        :returns: str: The IP which is removed
        :raises  :class:`ip_model.Exceptions.InvalidIpException` for invalid IPv4
        """
        num_ip = to_number(ip)
        self.head.remove(num_ip)
        return ip


    @validate_cidr
    def remove_cidr(self, cidr) -> bool:
        """
        Removes the given valid IPv4 CIDR

        :param cidr: String in CIDR notation
        :return: str: CIDR range which is removed
        :raises  :class:`ip_model.Exceptions.InvalidIpException` for invalid IPv4 CIDR
        """
        return self._remove_cidr(cidr)

    @validate
    def is_present(self, ip) -> bool:
        """
        Checks if a given valid IPv4 is present or not

        :param ip: An Ipv4 as String
        :returns: True, if the element is present
                  False, if the element is not present
        :raises  :class:`ip_model.Exceptions.InvalidIpException` for invalid IPv4
        """
        num_ip = to_number(ip)
        return self.head.is_present(num_ip)
