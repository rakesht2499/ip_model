from ip_model.Ipv6 import Ipv6
from ipaddress import ip_network


class TestIpv6:
    tree = Ipv6()
    ip1 = "192::155"
    ip2 = "::fff:f345:127"
    ip3 = "19:FFE:75::"
    cidr = "8653:53fe::/122"

    def test_add_ip1(self):
        assert self.tree.add(self.ip1) is True
        assert self.tree.is_present(self.ip1) is True
        assert self.tree.is_present(self.ip2) is False
        assert self.tree.is_present(self.ip3) is False

    def test_add_ip2(self):
        assert self.tree.add(self.ip2) is True
        assert self.tree.is_present(self.ip1) is True
        assert self.tree.is_present(self.ip2) is True
        assert self.tree.is_present(self.ip3) is False

    def test_add_cidr(self):
        assert self.tree.add_cidr(self.cidr) is True
        for ip in ip_network(self.cidr):
            assert self.tree.is_present(str(ip)) is True

    def test_remove_cidr(self):
        self.tree.remove_cidr(self.cidr)
        for ip in ip_network(self.cidr):
            assert self.tree.is_present(str(ip)) is False
