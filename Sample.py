from Ipv4 import Ipv4

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

    print(add_template.format(ip2))
    tree.add(ip2)
    print(verify_templete.format(ip, tree.is_present(ip)))
    print(verify_templete.format(ip2, tree.is_present(ip2)))
    print(verify_templete.format(ip3, tree.is_present(ip3)))

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
