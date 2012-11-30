"""
Module for managing changelog information
"""
import os

import sh

from pygit2 import Repository

from debgit.branch import get_branch_name

def get_changelog_entries():
    """
    Iterate through any changelog entries found
    """
    last_tag = None

    try:
        last_tag = str(sh.git('describe', '--tags', '--abbrev=0', 'HEAD^').strip())
        ref = '{0}..{1}'.format(last_tag, 'HEAD')
    except sh.ErrorReturnCode_128:
        ref = 'HEAD'

    repo = Repository('.git')

    for line in sh.git('rev-list', ref, _iter=True):
        commit_hash = line.strip()
        commit = repo[commit_hash]

        if 'Changelog:' in commit.message:
            yield commit.message.splitlines()[0]

def get_distribution(branch=None):
    branch = branch or get_branch_name()

    return 'stable' if branch == 'master' else branch
