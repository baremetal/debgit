"""
Debgit branch management
"""
import re
import sh

from debgit.ssh import cache_ssh_key

GIT_PUSH_URL_RE = re.compile(r'Push\s+URL:\s+(?P<git_uri>.*)')
GIT_SSH_URI_RE = re.compile(
    r'(?P<username>.*?)@(?P<hostname>[^:]+):(?P<repo_path>.*).git')

def get_branch_name():
    """
    Get the name of the current git branch.
    """
    return str(sh.basename(str(sh.git('symbolic-ref', 'HEAD')))).strip()

def get_branch_list():
    """
    return a list of all the branches in a given repository
    """

    for line in sh.git('branch', '-a', '--no-color', _iter=True):
        yield line[2:].strip()

def get_upstream_for_branch(branch):
    """
    From the given branch, determine the upstream URI.

    The URI will be inspected to see if it's an HTTP URL.  If it is an SSH URL,
    it will be converted to HTTP.
    """

    git = sh.git.bake('remote', '-v', 'show')

    git_push_uri = None

    for line in git(_iter=True):
        line = line.strip()

        if not line.endswith('(push)'):
            continue

        split_line = line.split()
        remote = split_line[0]

        # if this is an SSH upstream server, make sure the key is cached
        matches = GIT_SSH_URI_RE.match(split_line[1])
        if matches:
            hostname = matches.group('hostname')
            cache_ssh_key(hostname)

        found = False
        t_git_push_uri = None

        for info in git(remote, _iter=True):
            info = info.strip()

            matches = GIT_PUSH_URL_RE.match(info)
            if matches:
                t_git_push_uri = matches.group('git_uri')
            else:
                if info.startswith('{0} pushes to'.format(branch)):
                    found = True
                    break

        if found:
            git_push_uri = t_git_push_uri
            break

    if git_push_uri is None:
        raise Exception('Unable to find upstream for {0}'.format(branch))

    # attempt to convert to an HTTP URL
    matches = GIT_SSH_URI_RE.match(git_push_uri)
    if matches:
        git_push_uri = 'http://{hostname}/{repo_path}'.format(**matches.groupdict())

    return git_push_uri
