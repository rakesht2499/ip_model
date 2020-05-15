from ip_model.Ipv4 import Ipv4


class TestIpv4:
    tree = Ipv4()
    ip1 = "192.168.0.152"
    ip2 = "192.168.0.153"
    ip3 = "192.168.0.154"
    ip4 = "192.168.0.155"
    ip5 = "192.168.128.155"
    ip6 = "192.168.128.127"
    cidr = "192.168.52.0/24"
    cidr_fixed_part = "192.168.52."

    def test_add_ip1(self):
        assert self.tree.add(self.ip1) is True
        assert self.tree.is_present(self.ip1) is True
        assert self.tree.is_present(self.ip2) is False
        assert self.tree.is_present(self.ip3) is False

    def test_add_ip2(self):
        assert self.tree.add(self.ip2)
        assert self.tree.is_present(self.ip1) is True
        assert self.tree.is_present(self.ip2) is True
        assert self.tree.is_present(self.ip3) is False

    def test_add_ip3(self):
        assert self.tree.add(self.ip3)
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
        self.tree.remove(self.ip3)
        self.tree.remove(self.ip6)
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
