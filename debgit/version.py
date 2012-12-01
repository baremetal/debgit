"""
Module for managing git versions.
"""
import time

import sh

def get_version():
    """
    Based on the version returned by `git describe --tags`, generate a
    date-based version number that shows this branch's relationship relative to the
    last tag in this repository.
    """

    git_version = ''
    git_sha = None
    now = time.strftime('%y%j.%H%M')

    try:
        git_describe = str(sh.git('describe', tags=True).strip())
        git_describe_split = git_describe.split('-')

        git_version = git_describe_split[0]

        if len(git_describe_split) > 1:
            git_sha = git_describe_split[-1]
    except sh.ErrorReturnCode_128:
        git_version = '0.0'

    # when no sha is found, we are on an actual tag rather than development
    # from a particular tag.  in this case, simply use the bare version
    # number rather than generating a date+sha-based version number.
    if git_sha:
        sw_version = '{0}+{1}+{2}'.format(git_version, now, git_sha)
    else:
        sw_version = git_version

    return sw_version
