#!/usr/bin/env python

"""
POC for subnet calculator
"""

import ipaddress
from math import (
    log,
    ceil
)

clpow2 = lambda x: pow(2, int(log(x, 2) + 0.5))
nxtpow2 = lambda x: int(pow(2, ceil(log(x, 2))))
exppow2 = lambda x, y: x if pow(2, x) == y else exppow2(x + 1, y)

def get_subnets_layers(vpc_cidr_string, azs, layers):
    """
    """
    vpc_net = ipaddress.IPv4Network(vpc_cidr_string)
    subnet_mask = vpc_cidr_string.split('/')[-1]
    splits = azs * layers
    ips = vpc_net.num_addresses
    ips_split = ips / splits
    clpower2 = clpow2(ips_split)
    power = exppow2(1, clpower2)

    if power < splits:
        clpower2 /= 2
    diff = exppow2(1, clpower2)
    subnets_cidr_index = 32 - diff
    subnets_list = list(vpc_net.subnets(new_prefix=subnets_cidr_index))
    return [f'{subnet}' for subnet in subnets_list]

if __name__ == '__main__':
    subnets = get_az_layers_subnets('10.0.0.0/22', 3, 3)
    print(subnets)
