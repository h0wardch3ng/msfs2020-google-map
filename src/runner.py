import atexit
from python_hosts import Hosts, HostsEntry
import subprocess

import urllib3
from python_hosts import Hosts, HostsEntry

urllib3.disable_warnings()


def add_cert():
    subprocess.run(["certutil", "-addstore", "-f", "root",
                    ".\certs\cert.crt"], shell=True, check=True)

my_hosts = Hosts()
domains = ['kh.ssl.ak.tiles.virtualearth.net', 'khstorelive.azureedge.net']

# origin_ips = {}
# dns_resolver = dns.resolver.Resolver()
# dns_resolver.nameservers = ['8.8.8.8']
# for d in domains:
#     origin_ips[d] = dns_resolver.query(d)[0].to_text()

def override_hosts():
    for domain in domains:
        my_hosts.remove_all_matching(name=domain)
        new_entry = HostsEntry(
            entry_type='ipv4', address='127.0.0.1', names=[domain])
        my_hosts.add([new_entry])
    my_hosts.write()

def restore_hosts():
    for domain in domains:
        my_hosts.remove_all_matching(name=domain)
    my_hosts.write()