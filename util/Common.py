"""
@Copyrights 2020 Rakesh Kumar T
github: rakesht2499
"""

from ipaddress import ip_address, IPv4Address


def to_number(ip):
    if isinstance(ip_address(ip), IPv4Address):
        padding_len = 10
    else:
        padding_len = 39
    return str(int(ip_address(ip))).rjust(padding_len, "0")
