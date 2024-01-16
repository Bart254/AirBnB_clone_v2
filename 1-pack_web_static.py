#!/usr/bin/python3
""" Packs webpages into an archive for deployment
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """ Function uses fabric to pack local web_static files
    """
    r1 = local("mkdir -p versions")
    archive_file = 'web_static' + datetime.now().strftime('%Y%m%d%H%M%S') +\
        '.tgz'
    archive_path = 'versions' + '/' + archive_file
    r2 = local("tar -cvzf {} web_static".format(archive_path))
    if r1.failed or r2.failed:
        return None
    return archive_path
