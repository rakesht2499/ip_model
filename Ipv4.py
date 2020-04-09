from ip_model.util.RadixTree import RadixTree


class Ipv4:
    def __init__(self):
        self.head = RadixTree("N")

    def add(self, ip) -> bool:
        if self._validate_ip(ip):
            bin_ip = self._to_binary(ip)
            return self.head.add(bin_ip)
        return False

    def remove(self, ip) -> bool:
        if self._validate_ip(ip):
            bin_ip = self._to_binary(ip)
            return self.head.remove(bin_ip)
        return False

    def is_present(self, ip) -> bool:
        if self._validate_ip(ip):
            bin_ip = self._to_binary(ip)
            return self.head.is_present(bin_ip)
        return False

    def _to_binary(self, ip):
        binary_ip = ""
        for x in ip.split("."):
            binary_ip += f'{int(x):08b}'
        return binary_ip

    def _validate_ip(self, ip):
        valid = sum([1 for bit8 in ip.split(".") if 255 >= int(bit8) >= 0]) == 4
        return valid
