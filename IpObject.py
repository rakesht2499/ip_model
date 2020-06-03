import abc
from ipaddress import ip_network


class IpObject:
    @abc.abstractmethod
    def add(self, ip: str):
        pass

    @abc.abstractmethod
    def remove(self, ip: str):
        pass

    @abc.abstractmethod
    def is_present(self, ip: str):
        pass

    @abc.abstractmethod
    def add_cidr(self, cidr: str):
        pass

    @abc.abstractmethod
    def remove_cidr(self, cidr: str):
        pass

    def _insert_cidr(self, cidr) -> bool:
        for ip in ip_network(cidr):
            self.add(str(ip))
        return True

    def _remove_cidr(self, cidr) -> bool:
        for ip in ip_network(cidr):
            self.remove(str(ip))
        return cidr
