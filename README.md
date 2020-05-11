[![](https://img.shields.io/badge/pypi-v2.0.1-blue.svg)](https://pypi.org/project/ip-model/)
[![License](https://img.shields.io/badge/Licence-Apache--2.0-orange)](https://github.com/rakesht2499/Ip-Model/blob/master/LICENSE/)

# Ip-Model

A Data Structure for efficiently storing, removing and checking all Ipv4 addresses in O(1) time.

## Pre-requisite

* pytest

## How to Test

```shell script
cd tests/
pytest
```

### For generating a html report of tests
```shell script
cd tests/
pytest --html=report.html
```

## Usage

## Single Ip's

### Ipv4

```python
from ip_model.Ipv4 import Ipv4

blacklist = Ipv4()
```

#### To add an IP:

```python
# arg: String
blacklist.add("192.0.0.18")
```

#### To remove an IP:

```python
# arg: String
blacklist.remove("192.0.0.18")
```

#### To check if an IP is present/not:

```python
# arg: String
# returns: bool
blacklist.is_present("192.0.0.18")
```

### Ipv6

```python
from ip_model.Ipv4 import Ipv6

blacklist = Ipv6()
```

#### To add an IP:

```python
# arg: String
blacklist.add("192::18")
```

#### To remove an IP:

```python
# arg: String
blacklist.remove("192:ffff:e034::23")
```

#### To check if an IP is present/not:

```python
# arg: String
# returns: bool
blacklist.is_present("::5:4fed")
```


## CIDR

### Ipv4:

#### To Add

```python
# arg: String
blacklist.add_cidr("192.92.53.0/24")
```

```python
# arg: String
blacklist.add_cidr("192.92.53.0/255.255.255.252")
```

#### To remove:

```python
# arg: String
blacklist.remove_cidr("192.92.53.0/24")
```

### Ipv6:

#### To Add

```python
# arg: String
blacklist.add_cidr("8653:53fe::/122/24")
```

#### To remove:

```python
# arg: String
blacklist.remove_cidr("8653:53fe::/122")
```

> Note:
>
> The tradeoff is, the call for how to handle with overlapping CIDR's must be taken by the service using the DS. 
> The DataStructure only performs the requested operation with the given data



### Exception Handling

- Throws `TypeError`: passing Invalid Datatype, incorrect number of arguments
- Throws `InvalidIpException`: When an invalid Ip is passed

```python
from ip_model.Exceptions import InvalidIpException

try:
    blacklist.add("192.455.554.343")
except InvalidIpException:
    print("Incorrect Ipv4 Address")

# For CIDR
try:
    blacklist.add("192.12.65.0/16")
except InvalidIpException:
    print("Incorrect CIDR")
```

***
## Section For Geeks
Click [here](https://github.com/rakesht2499/ip_model/wiki) for ip-model: Under the Hood
