# Blacklist

A simple implementation of RadixTree used for efficiently storing and checking in O(1) time for all Ipv4 addresses.

## How to run sample program

#### Pre-requisite
- Python3

#### How to run
```shell script
python3 Sample.py
```

## Usage

Initialization
```python
from Blacklist import Blacklist

blasklist = Blacklist()
```

Adding an IP
```python
# argument: String (Eg., 10.0.0.1)
# returns: boolean
blacklist.add(ip)
```

Removing an IP
```python
# argument: String
# returns: boolean
blacklist.remove(ip)
```

Checking if present
```python
# argument: String
# returns: boolean
blacklist.is_present(ip)
```


Upcoming Support : 
1) Ipv6
2) CIDR ranges