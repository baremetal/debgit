"""
SSH helper function
"""
import os

import sh

SSH_KNOWN_HOSTS = os.path.expanduser('~/.ssh/known_hosts')

def cache_ssh_key(hostname):
    """
    Request the host's key and cache it in .ssh/known_hosts

    http://serverfault.com/questions/321167/add-correct-host-key-in-known-hosts-multiple-ssh-host-keys-per-hostname
    """

    try:
        sh.grep('-q', hostname, SSH_KNOWN_HOSTS)
    except sh.ErrorReturnCode:
        with open(SSH_KNOWN_HOSTS, 'ab') as known_hosts_file:
            known_hosts_file.write('\n')

            keyscan = sh.Command('ssh-keyscan')
            keyscan('-t', 'rsa', hostname, _out=known_hosts_file)
