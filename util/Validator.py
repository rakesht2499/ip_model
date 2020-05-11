"""
@Copyrights 2020 Rakesh Kumar T
github: rakesht2499
"""

from ip_model.Exceptions import InvalidIpException
from ipaddress import ip_network, ip_address


def _argument_error(f, *args):
    if len(args) != 2:
        type_error = "{}() takes exactly one argument ({} given)".format(f.__name__, len(args) - 1)
        raise TypeError(type_error)


def _instance_error(ip):
    if not isinstance(ip, str):
        type_error = "Expected 'str' not {}".format(str(type(ip)))
        raise TypeError(type_error)


class Validator:
    @staticmethod
    def validate(f):
        def validate_ip(*args):
            _argument_error(f, *args)
            ip = args[1]
            _instance_error(ip)
            try:
                valid = sum([1 for bit8 in ip.split(".") if 255 >= int(bit8) >= 0]) == 4
            except ValueError:
                error_msg = "{} is not a proper Ipv4 address".format(ip)
                raise InvalidIpException(error_msg) from None
            else:
                if valid:
                    return f(*args)
                error_msg = "{} is not a proper Ipv4 address".format(ip)
                raise InvalidIpException(error_msg)

        return validate_ip

    @staticmethod
    def validate_ipv6(f):
        def validate_ip(*args):
            _argument_error(f, *args)
            ip = args[1]
            _instance_error(ip)
            try:
                ip_address(ip)
            except ValueError:
                error_msg = "{} is not a proper Ipv6 address".format(ip)
                raise InvalidIpException(error_msg) from None
            else:
                return f(*args)

        return validate_ip

    @staticmethod
    def validate_cidr(f):
        def validate_network(*args):
            _argument_error(f, *args)
            cidr = args[1]
            _instance_error(cidr)
            try:
                ip_network(cidr)
            except ValueError:
                error_msg = "{} is not a proper CIDR".format(cidr)
                raise InvalidIpException(error_msg)
            else:
                return f(*args)

        return validate_network
