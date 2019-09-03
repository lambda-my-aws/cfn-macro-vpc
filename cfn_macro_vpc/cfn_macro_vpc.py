# -*- coding: utf-8 -*-

"""Main module."""

from datetime import datetime as dt
from cfn_macro_vpc import __version__

from troposphere import (
    Template, Output, Parameter,
    Ref, GetAtt, Sub, FindInMap
)


from cfn_macro_vpc_core import (
    init_vpc, add_vpc, add_dhcp_options,
    add_vpcmap, add_gateway
)

from cfn_macro_vpc_subnets import (
    init_subnet, add_layer_route_table,
    associate_subnets_to_layer_rtb
)

from subnets import get_subnets_cidrs

KEYISSET = lambda x, y: x in y.keys() and y[x]


def add_subnets(template, vpc, vpc_cidr, layers):
    """
    """
    subnets_cidrs = get_subnets_cidrs(vpc_cidr, len(azs), len(layers))

def generate_template(description=None, **settings):
    """
    """

    if description is None:
        description = 'VPC template generated via CFN Macro'
    template = Template(description)
    template.set_metadata({
        'Author': 'https://github.com/johnpreston',
        'Version': __version__,
        'Date': dt.utcnow().isoformat()
    })
    vpc = add_vpc(template, **settings['Properties'])
    if 'VpcSettings' in settings.keys():
        vpc_settings = settings['VpcSettings']
    if 'DhcpOptions' in vpc_settings.keys():
        add_dhcp_options(template, vpc, **vpc_settings['DhcpOptions'])
    if KEYISSET('PublicVpc', vpc_settings):
        add_gateway(template, vpc)
    if KEYISSET('UseCloudMap', vpc_settings):
            add_vpcmap(tpl, vpc)

    if KEYISSET('SubnetsLayers', settings):
        subnets_settings = settings['SubnetsLayers']
        add_subnets(
            template,
            vpc,
            settings['Properties']['VpcCidr'],
            subnet_settings,
            vpc_settings['AvailabilityZones']
        )
