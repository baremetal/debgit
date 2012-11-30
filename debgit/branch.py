"""
Debgit branch management
"""
import sh

def get_branch_name():
    return str(sh.basename(str(sh.git('symbolic-ref', 'HEAD')))).strip()

def get_branch_list():
    """
    return a list of all the branches in a given repository
    """

    for line in sh.git('branch', '-a', '--no-color', _iter=True):
        yield line[2:].strip()
