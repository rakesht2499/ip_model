from RadixTree import RadixTree

if __name__ == "__main__":
    tree = RadixTree("N")
    ip = "192.168.0.152"
    ip2 = "192.168.0.153"
    ip3 = "192.168.0.154"
    ip4 = "192.168.0.155"
    ip5 = "192.168.128.155"
    ip6 = "192.168.128.127"

    tree.add(ip)
    tree.print_data()
    print(tree.is_present(ip))
    print(tree.is_present(ip2))

    tree.add(ip2)
    tree.print_data()
    print(tree.is_present(ip))
    print(tree.is_present(ip2))
    print(tree.is_present(ip3))

    tree.add(ip3)
    tree.print_data()
    print(tree.is_present(ip))
    print(tree.is_present(ip2))
    print(tree.is_present(ip3))
    print(tree.is_present(ip4))

    tree.add(ip4)
    tree.print_data()
    print(tree.is_present(ip))
    print(tree.is_present(ip2))
    print(tree.is_present(ip3))
    print(tree.is_present(ip4))
    print(tree.is_present(ip5))

    tree.add(ip5)
    tree.print_data()
    print(tree.is_present(ip))
    print(tree.is_present(ip2))
    print(tree.is_present(ip3))
    print(tree.is_present(ip4))
    print(tree.is_present(ip5))

    print("Removal", tree.remove(ip3))
    print("Removal", tree.remove(ip5))
    print("Removal", tree.remove(ip6))
    tree.print_data()
    print(tree.is_present(ip))
    print(tree.is_present(ip2))
    print(tree.is_present(ip3))
    print(tree.is_present(ip4))
    print(tree.is_present(ip5))
