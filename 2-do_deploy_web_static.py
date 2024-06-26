#!/usr/bin/python3
""" Writes a function to deploy web_static website using fabric
"""
from fabric.api import run, put, env
import os
env.hosts = ['100.25.109.13', '18.204.13.228']
env.user = 'ubuntu'


def do_deploy(archive_path):
    """
    deploys the web_static to servers
    """
    if os.path.exists(archive_path):
        put1 = put(archive_path, '/tmp/')
        _filename = archive_path.split("/")[-1]
        filename = _filename.split(".")[0]
        run1 = run('mkdir -p /data/web_static/releases/{}'.format(filename))
        run2 = run('tar -xzf /tmp/{} -C /data/web_static/releases/{}'.format
                   (_filename, filename))
        run3 = run('rm /tmp/{}'.format(_filename))
        run6 = run('rm -rf /data/web_static/current')
        run7 = run('ln -s /data/web_static/releases/{} \
                    /data/web_static/current'.format(filename))

        if True in (run1.failed, run2.failed, run3.failed,
                    run6.failed, run7.failed, put1.failed):
            return False
        return True
    return False
