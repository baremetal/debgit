"""
Debgit branch management
"""
import sh

def get_branch_name():
    return str(sh.basename(str(sh.git('symbolic-ref', 'HEAD')))).strip()
