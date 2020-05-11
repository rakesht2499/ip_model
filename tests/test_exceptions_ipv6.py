from ip_model.Exceptions import InvalidIpException
from ip_model.Ipv6 import Ipv6
from ip_model.tests.Exceptions import Exceptions

import pytest


class TestExceptionsIpv4(Exceptions):
    tree = Ipv6()
    ip1 = "192::155"
    ip2 = "::fff:f345:127"
    invalid_ip1 = "353:3451"
    invalid_ip2 = "192.5.46.375"
    invalid_ip3 = "::9834"
    invalid_cidr = "1532::64/22"

    def test_throw_invalid_ip(self):
        with pytest.raises(InvalidIpException) as exception:
            self.tree.add(self.invalid_ip1)
        assert f"{self.invalid_ip1} is not a proper Ipv6 address" == str(exception.value)

        with pytest.raises(InvalidIpException) as exception:
            self.tree.add(self.invalid_ip2)
        assert f"{self.invalid_ip2} is not a proper Ipv6 address" == str(exception.value)

    def test_no_arg_passed(self):
        with pytest.raises(TypeError) as type_error:
            self.tree.add()
        assert "add() takes exactly one argument (0 given)" == str(type_error.value)
        with pytest.raises(TypeError) as type_error:
            self.tree.remove()
        assert "remove() takes exactly one argument (0 given)" == str(type_error.value)
        with pytest.raises(TypeError) as type_error:
            self.tree.is_present()
        assert "is_present() takes exactly one argument (0 given)" == str(type_error.value)

    def test_too_many_arguments(self):
        with pytest.raises(TypeError) as type_error:
            self.tree.add(self.ip1, self.ip2)
        assert "add() takes exactly one argument (2 given)" == str(type_error.value)

        with pytest.raises(TypeError) as type_error:
            self.tree.remove(self.ip1, self.ip2)
        assert "remove() takes exactly one argument (2 given)" == str(type_error.value)

        with pytest.raises(TypeError) as type_error:
            self.tree.is_present(self.ip1, self.ip2)
        assert "is_present() takes exactly one argument (2 given)" == str(type_error.value)

    def test_add_cidr_exceptions(self):
        with pytest.raises(InvalidIpException) as exception:
            self.tree.add_cidr(self.invalid_cidr)
        assert f"{self.invalid_cidr} is not a proper CIDR" == str(exception.value)

    def test_remove_cidr_exceptions(self):
        with pytest.raises(InvalidIpException) as exception:
            self.tree.remove_cidr(self.invalid_cidr)
        assert f"{self.invalid_cidr} is not a proper CIDR" == str(exception.value)
