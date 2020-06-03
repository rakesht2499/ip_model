from ipaddress import ip_network
from ip_model.Ip import Ip


class TestIp:
    tree = Ip()
    ip1 = "192.168.0.52"
    ip2 = "192.168.0.53"
    ip3 = "192.168.0.54"
    ip4 = "192.168.0.55"
    ip5 = "192.168.128.55"
    ip6 = "192.168.128.27"
    cidr = "192.18.52.0/24"
    cidr_fixed_part = "192.18.52."

    ipv61 = "192::15"
    ipv62 = "::fff:f345:12"
    ipv63 = "19:FFE:7::"
    cidrv6 = "9653:53fe::/122"

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

    def test_add_ip3(self):
        assert self.tree.add(self.ip3) is True
        assert self.tree.is_present(self.ip1) is True
        assert self.tree.is_present(self.ip2) is True
        assert self.tree.is_present(self.ip3) is True

    def test_add_ip4_5_6(self):
        assert self.tree.add(self.ip4) is True
        assert self.tree.add(self.ip5) is True
        assert self.tree.add(self.ip6) is True
        assert self.tree.is_present(self.ip1) is True
        assert self.tree.is_present(self.ip2) is True
        assert self.tree.is_present(self.ip3) is True
        assert self.tree.is_present(self.ip4) is True
        assert self.tree.is_present(self.ip5) is True
        assert self.tree.is_present(self.ip6) is True

    def test_remove_ip3_6(self):
        self.tree.remove(self.ip3) is self.ip3
        self.tree.remove(self.ip6) is self.ip6
        assert self.tree.is_present(self.ip1) is True
        assert self.tree.is_present(self.ip2) is True
        assert self.tree.is_present(self.ip3) is False
        assert self.tree.is_present(self.ip4) is True
        assert self.tree.is_present(self.ip5) is True
        assert self.tree.is_present(self.ip6) is False

    def test_add_cidr(self):
        assert self.tree.add_cidr(self.cidr) is True
        for x in range(0, 256):
            assert self.tree.is_present(self.cidr_fixed_part + str(x)) is True

    def test_remove_cidr(self):
        self.tree.remove_cidr(self.cidr)
        for x in range(0, 256):
            assert self.tree.is_present(self.cidr_fixed_part + str(x)) is False

    def test_add_ipv61(self):
        assert self.tree.add(self.ipv61) is True
        assert self.tree.is_present(self.ipv61) is True
        assert self.tree.is_present(self.ipv62) is False
        assert self.tree.is_present(self.ipv63) is False

    def test_add_ipv62(self):
        assert self.tree.add(self.ipv62) is True
        assert self.tree.is_present(self.ipv61) is True
        assert self.tree.is_present(self.ipv62) is True
        assert self.tree.is_present(self.ipv63) is False

    def test_remove_ipv61(self):
        assert self.tree.remove(self.ipv61) is self.ipv61
        assert self.tree.is_present(self.ipv61) is False
        assert self.tree.is_present(self.ipv62) is True
        assert self.tree.is_present(self.ipv63) is False

    def test_add_cidrv6(self):
        assert self.tree.add_cidr(self.cidrv6) is True
        for ip in ip_network(self.cidrv6):
            assert self.tree.is_present(str(ip)) is True

    def test_remove_cidrv6(self):
        assert self.tree.remove_cidr(self.cidrv6) is self.cidrv6
        for ip in ip_network(self.cidrv6):
            assert self.tree.is_present(str(ip)) is False
