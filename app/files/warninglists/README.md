# misp-warninglist

misp-warninglists are lists of well-known indicators that can be associated to potential false positives, errors or mistakes.

[![Build Status](https://travis-ci.org/MISP/misp-warninglists.svg?branch=master)](https://travis-ci.org/MISP/misp-warninglists)

The warning lists are integrated in MISP to display an info/warning box at the event and attribute level if such indicators
are available in one of the list. The list can be globally enabled or disabled in MISP following the practices of the organization.

# lists

- [lists/alexa](lists/alexa) - Top 1000 websites from Alexa
- [lists/amazon-aws](lists/amazon-aws) - Known Amazon AWS IP address ranges
- [lists/automated-malware-analysis](lists/automated-malware-analysis) - known domains used by automated malware analysis services
- [lists/bank-website](lists/bank-website) - List of known banking website
- [lists/cisco_top1000](lists/cisco_top1000) - Cisco (Umbrella) top 1000 websites
- [lists/common-ioc-false-positive](lists/common-ioc-false-positive) - common false-positives in IOCs
- [lists/eicar.com](lists/eicar.com) - hashes for EICAR test virus
- [lists/empty-hashes](lists/empty-hashes) - hash values of empty files
- [lists/google](lists/google) - known domains and hostnames from Google
- [lists/ipv6-linklocal](lists/ipv6-linklocal) - IPv6 link local prefix
- [lists/microsoft](lists/microsoft) - known Microsoft domains
- [lists/microsoft-azure](lists/microsoft-azure) - known Microsoft Azure Datacenter IP Ranges
- [lists/microsoft-office365](lists/microsoft-office365) - known Office 365 URLs and IP address ranges
- [lists/microsoft-office365-cn](lists/microsoft-office365-cn) - known Office 365 IP address ranges in China
- [lists/microsoft-attack-simulator](lists/microsoft-attack-simulator/) - known Office 365 hostnames and IP address used for Microsoft "Attack Simulator"
- [lists/microsoft-win10-connection-endpoints](lists/microsoft-win10-connection-endpoints/) - known Windows 10 connection endpoints
- [lists/multicast](lists/multicast) - known IPv4 multicast CIDR blocks
- [lists/ovh-cluster](lists/ovh-cluster) - List of known OVH Cluster IP
- [lists/public-dns-v4](lists/public-dns-v4) - IPv4 addresses and reverse of public DNS resolver
- [lists/public-dns-v6](lists/public-dns-v6) - IPv6 addresses and reverse of public DNS resolver
- [lists/rfc1918](lists/rfc1918) - RFC 1918 network subnets
- [lists/rfc3849](lists/rfc3849) - RFC 3849 - Documentation prefix for ipv6
- [lists/rfc5735](lists/rfc5735) - RFC 5735 CIDR blocks - Special Use IPv4 Addresses
- [lists/rfc6598](lists/rfc6598) - RFC 6598 IANA-Reserved IPv4 Prefix for Shared Address Space (Carrier- Grade NAT (CGN) devices)
- [lists/rfc6761](lists/rfc6761) - RFC 6761 Special-Use Domain Names
- [lists/security-provider-blogpost](lists/security-provider-blogpost) - Security providers or vendors blog domains
- [lists/second-level-tlds](lists/second-level-tlds) - Mozilla list of second level top-level domains
- [lists/sinkholes](lists/sinkholes) - List of known sinkholes
- [lists/tlds](lists/tlds) - top-level domains
- [lists/url-shortener](lists/url-shortener) - URL shorteners services
- [lists/whats-my-ip](lists/whats-my-ip) - "What's my IP" service

# Format of a warning list

~~~~json
{
  "name": "List of known public DNS resolvers",
  "version": 1,
  "description": "Event contains one or more public DNS resolvers as attribute with an IDS flag set",
  "matching_attributes": [
    "ip-src",
    "ip-dst"
  ],
  "list": [
    "8.8.8.8",
    "8.8.4.4",
    "208.67.222.222",
    "208.67.220.220",
    "195.46.39.39",
    "195.46.39.40"
  ]
}
~~~~

If matching_attributes are not set, the list is matched against any type of attributes.

## type of warning list

- ```string``` (default) - perfect match of a string in the warning list against matching attributes
- ```substring``` - substring matching of a string in the warning list against matching attributes
- ```hostname``` - hostname matching (e.g. domain matching from URL) of a string in the warning list against matching attributes
- ```cidr``` - IP or CDIR block matching in the warning list against matching attributes
- ```regex``` - regex matching of a string matching attributes

# Processing warning lists in python

See [PyMISPWarningLists](https://github.com/MISP/PyMISPWarningLists) for a
python interface to warning lists.

# License

MISP warning-lists are licensed under [CC0 1.0 Universal (CC0 1.0)](https://creativecommons.org/publicdomain/zero/1.0/) -  Public Domain Dedication. If a specific author of a taxonomy wants to license it under a different license, a pull request can be requested.
