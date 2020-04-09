from ip_model.util.RadixTree import RadixTree
from ip_model.util.Validator import Validator
validate = Validator.validate


class Ipv4:
    def __init__(self):
        self.head = RadixTree("N")

    @validate
    def add(self, ip) -> bool:
        bin_ip = self._to_binary(ip)
        return self.head.add(bin_ip)

    @validate
    def remove(self, ip) -> bool:
        bin_ip = self._to_binary(ip)
        return self.head.remove(bin_ip)

    @validate
    def is_present(self, ip) -> bool:
        bin_ip = self._to_binary(ip)
        return self.head.is_present(bin_ip)

    def _to_binary(self, ip):
        binary_ip = ""
        for x in ip.split("."):
            binary_ip += f'{int(x):08b}'
        return binary_ip
