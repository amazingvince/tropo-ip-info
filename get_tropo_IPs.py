import subprocess
import shlex


"""
If there are multiple service you need to this information for this scrip is easily expandable 
and reusable by adding sys argv for command and prefix.

This script gets IP addresses to whitelist then formats and sends them to STDOUT.

Expected output format:
    Prefix + , + IP

Example:
    tropo,10.10.0.10/24
"""

Prefix = "tropo"  # This will proceed the IP address
Command = "nslookup -q=TXT _netblocks.tropo.com 8.8.8.8"

def get_ips(command):
    p = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    ips, err = p.communicate()
    if ips:
        return ips
    if err:
        print "standard error of subprocess:"
        print err

def clean_ip(line, prefix):
    # rearanged line processing to work cross platform
    ip = line[line.find('"') + 1:] 
    ip = ip[:ip.find('"')]
    return prefix + "," + ip


def process_ips(ips, prefix):
    for line in ips.split("\n"):
        if '"' in line:
            print clean_ip(line, prefix)


def main():
    ips = get_ips(Command)
    process_ips(ips, Prefix)


if __name__ == '__main__':
    main()
