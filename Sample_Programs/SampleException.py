from ip_model.Ipv4 import Ipv4
from ip_model.Exceptions import InvalidIpException

if __name__ == "__main__":
    sample = Ipv4()
    try:
        sample.add()
    except TypeError as te:
        print(te)

    try:
        sample.add("","")
    except TypeError as te:
        print(te)

    try:
        sample.add(1234)
    except TypeError as te:
        print(te)

    try:
        sample.add("....")
    except InvalidIpException as te:
        print(te)

    # This statement will throw an InvalidIp Exception
    sample.add("192.168.0.985")
