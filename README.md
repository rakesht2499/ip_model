[![](https://img.shields.io/badge/pypi-v1.0.1-blue.svg)](https://pypi.org/project/ip-model/)
[![License](https://img.shields.io/badge/Licence-Apache--2.0-orange)](https://github.com/rakesht2499/Ip-Model/blob/master/LICENSE/)

# Ip-Model

A Data Structure for efficiently storing, removing and checking all Ipv4 addresses in O(1) time.

## Usage

```python
from ip_model.Ipv4 import Ipv4

blacklist = Ipv4()
```

### To add an IP:

```python
# arg: String
blacklist.add("192.0.0.18")
```

### To remove an IP:

```python
# arg: String
blacklist.remove("192.0.0.18")
```

### To check if an IP is present/not:

```python
# arg: String
# returns: bool
blacklist.is_present("192.0.0.18")
```

### Exception Handling

- Throws `TypeError`: passing Invalid Datatype, incorrect number of arguments
- Throws `InvalidIpException`: When an invalid Ip is passed

```python
from ip_model.Exceptions import InvalidIpException

try:
    blacklist.add("192.455.554.343")
except InvalidIpException:
    print("Incorrect Ipv4 Address")
```
