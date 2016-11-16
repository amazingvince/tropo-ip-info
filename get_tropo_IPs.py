import subprocess
import shlex

Prefix = "tropo"  # This will proceed the IP address
Command = "nslookup -q=TXT _netblocks.tropo.com 8.8.8.8"

"""
This script gets IP addresses then formats and sends them to STDOUT.
Example:
    tropo,10.10.0.10/24
    Prefix + , + IP
"""


def get_ips(command):
    p = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    ips, err = p.communicate()
    return ips


def clean_ip(line, prefix):
    return prefix + "," + line[line.find('"') + 1:-1]


def process_ips(ips, prefix):
    for line in ips.split("\n"):
        if '"' in line:
            print clean_ip(line, prefix)


def main():
    ips = get_ips(Command)
    process_ips(ips, Prefix)


if __name__ == '__main__':
    main()
