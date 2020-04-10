from ip_model.Exceptions import InvalidIpException


class Validator:
    @staticmethod
    def validate(f):
        def validate_ip(*args):
            if len(args) != 2:
                type_error = "{}() takes exactly one argument ({} given)".format(f.__name__, len(args) - 1)
                raise TypeError(type_error)
            ip = args[1]
            if not isinstance(ip, str):
                type_error = "Expected 'str' not {}".format(str(type(ip)))
                raise TypeError(type_error)
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
