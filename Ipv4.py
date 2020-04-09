from ip_model.util.RadixTree import RadixTree

class Ipv4:
    def __init__(self):
        self.head = RadixTree("N")

    def validate(f):
        def validate_ip(*args):
            if len(args) != 2:
                raise TypeError("{}() takes exactly one argument ({} given)".format(f.__name__, len(args)-1))
            ip = args[1]
            if not isinstance(ip, str):
                raise TypeError("Expected 'str' not {}".format(str(type(ip))))
            try:
                if sum([1 for bit8 in ip.split(".") if 255 >= int(bit8) >= 0]) == 4:
                    return f(*args)
                raise ValueError("Input is not a proper Ipv4 address")
            except ValueError:
                raise ValueError("Input is not a proper Ipv4 address") from None
        return validate_ip

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
