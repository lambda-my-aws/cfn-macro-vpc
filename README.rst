=============
CFN Macro VPC
=============


.. image:: https://img.shields.io/pypi/v/cfn_macro_vpc.svg
        :target: https://pypi.python.org/pypi/cfn_macro_vpc

.. image:: https://img.shields.io/travis/johnpreston/cfn_macro_vpc.svg
        :target: https://travis-ci.org/johnpreston/cfn_macro_vpc

.. image:: https://readthedocs.org/projects/cfn-macro-vpc/badge/?version=latest
        :target: https://cfn-macro-vpc.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status




CFN Macro VPC


* Free software: Apache Software License 2.0
* Documentation: https://cfn-macro-vpc.readthedocs.io.


How-to
-------

.. code-block:: yaml

   Parameters:
     VpcCidr:
       Type: String
   Transform:
     - cfnmacro-vpc
       Properties:
         CidrBlock: !Ref VpcCidr
	 EnableDnsHostnames: True
	 Tags:
	   - KeyName: Name
	     Value: !Ref AWS::Stackname
       VpcSettings:
         AvailabilityZones:
	   Fn::GetAZs !Ref 'AWS::Region'
         PublicVpc: True
	 UseCloudMap: True
	 DhcpOptions: # DHCP Options as according to `DHCP Options Doc`_
	   DomainName: !Sub '${AWS::StackName}.local'
       SubnetsLayers:
         - Name: Public
	   Properties:
	     PublicIngress: True
	     PublicEgress: True
	     AvailabilityZones:
	       Fn::GetAzs !Ref AWS::Region
	     OnePerAzOnly: True
	 - Name: Application
	   Properties:
	     PublicIngress: False
	     PublicEgress: True
	     AvailabilityZones:
	       Fn::GetAzs !Ref AWS::Region
	     OnePerAzOnly: False
	 - Name: Storage
	   Properties:
	     PublicEgress: False
	     PublicIngress: False
	     AvailabilityZones:
	       Fn::GetAZs !Ref AWS::Region
	     OnePerAzOnly: True


Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

.. _`DHCP Options Doc`: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-dhcp-options.html
