from ip_model.Ipv4 import Ipv4
from ip_model.Ipv6 import Ipv6

if __name__ == "__main__":
    tree = Ipv4()
    ip = "192.168.0.152"
    ip2 = "192.168.0.153"
    ip3 = "192.168.0.154"
    ip4 = "192.168.0.155"
    ip5 = "192.168.128.155"
    ip6 = "192.168.128.127"

    add_template = "\nAdding Ip : {}"
    verify_templete = "Verify if {} is present : {}"
    print(add_template.format(ip))

    tree.add(ip)
    print(verify_templete.format(ip, tree.is_present(ip)))
    print(verify_templete.format(ip2, tree.is_present(ip2)))
    print(verify_templete.format(ip2, tree.is_present(ip3)))
    print(verify_templete.format(ip2, tree.is_present(ip4)))

    print(add_template.format(ip2))
    tree.add(ip2)
    print(verify_templete.format(ip, tree.is_present(ip)))
    print(verify_templete.format(ip2, tree.is_present(ip2)))
    print(verify_templete.format(ip3, tree.is_present(ip3)))
    print(verify_templete.format(ip3, tree.is_present(ip4)))

    print(add_template.format(ip3))
    tree.add(ip3)
    print(verify_templete.format(ip, tree.is_present(ip)))
    print(verify_templete.format(ip2, tree.is_present(ip2)))
    print(verify_templete.format(ip3, tree.is_present(ip3)))
    print(verify_templete.format(ip4, tree.is_present(ip4)))

    print(add_template.format(ip4))
    tree.add(ip4)
    print(verify_templete.format(ip, tree.is_present(ip)))
    print(verify_templete.format(ip2, tree.is_present(ip2)))
    print(verify_templete.format(ip3, tree.is_present(ip3)))
    print(verify_templete.format(ip4, tree.is_present(ip4)))
    print(verify_templete.format(ip5, tree.is_present(ip5)))

    print(add_template.format(ip5))
    tree.add(ip5)
    print(verify_templete.format(ip, tree.is_present(ip)))
    print(verify_templete.format(ip2, tree.is_present(ip2)))
    print(verify_templete.format(ip3, tree.is_present(ip3)))
    print(verify_templete.format(ip4, tree.is_present(ip4)))
    print(verify_templete.format(ip5, tree.is_present(ip5)))

    print("\nRemoving {}\n".format(ip3, tree.remove(ip3)))
    print("Removing {}\n".format(ip5, tree.remove(ip5)))
    print("Removing {}\n".format(ip6, tree.remove(ip6)))
    print(verify_templete.format(ip, tree.is_present(ip)))
    print(verify_templete.format(ip2, tree.is_present(ip2)))
    print(verify_templete.format(ip3, tree.is_present(ip3)))
    print(verify_templete.format(ip4, tree.is_present(ip4)))
    print(verify_templete.format(ip5, tree.is_present(ip5)))

    print(tree.add_cidr("192.168.52.0/24"))

    is_cidr_inserted = True
    for x in range(0,256):
        is_cidr_inserted = is_cidr_inserted and tree.is_present("192.168.52."+str(x))

    print("All cidr range present : {}".format(str(is_cidr_inserted)))

    print(tree.remove_cidr("192.168.52.0/24"))

    is_cidr_removed = True
    for x in range(0,256):
        is_cidr_removed = is_cidr_removed or tree.is_present("192.168.52."+str(x))

    print("All cidr range removed : {}".format(str(is_cidr_removed)))

    tree = Ipv6()

    ipv61 = "192::155"
    ipv62 = "::fff:f345:127"

    add_template = "\nAdding Ip : {}"
    verify_templete = "Verify if {} is present : {}"

    print(add_template.format(ipv61))
    tree.add(ipv61)
    print(verify_templete.format(ipv61, tree.is_present(ipv61)))
    print(verify_templete.format(ipv62, tree.is_present(ipv62)))

    print(add_template.format(ipv62))
    tree.add(ipv62)
    print(verify_templete.format(ipv61, tree.is_present(ipv61)))
    print(verify_templete.format(ipv62, tree.is_present(ipv62)))
    print("Removing {}".format(ipv61, tree.remove(ipv61)))
    print(verify_templete.format(ipv61, tree.is_present(ipv61)))
    print(verify_templete.format(ipv62, tree.is_present(ipv62)))
    print("Removing {}".format(ipv62, tree.remove(ipv62)))
    print(verify_templete.format(ipv61, tree.is_present(ipv61)))
    print(verify_templete.format(ipv62, tree.is_present(ipv62)))

    print(tree.add_cidr("8653:53fe::/122"))

    print("Checking if 8653:53FE::0004 is present : {}".format(tree.is_present("8653:53fe::14")))

    print(tree.remove_cidr("8653:53FE::/122"))

    print("Checking if 8653:53FE::15 is present : {}".format(tree.is_present("8653:53FE::15")))
