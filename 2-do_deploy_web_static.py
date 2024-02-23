#!/usr/bin/python3
""" Writes a function to deploy web_static website using fabric
"""
from fabric.api import run, put, env
import os
env.hosts = ['100.25.177.60', '54.87.205.15']
env.user = 'ubuntu'


def do_deploy(archive_path):
    """
    deploys the web_static to servers
    """
    if os.path.exists(archive_path):
        try:
            put(archive_path, '/tmp/')
            _filename = archive_path.split("/")[-1]
            filename = _filename.split(".")[0]
            run('mkdir -p /data/web_static/releases/{}'.format(filename))
            run('tar -xzf /tmp/{} -C /data/web_static/releases/{}'.format
                (_filename, filename))
            run('rm /tmp/{}'.format(_filename))
            run('mv /data/web_static/releases/{}/web_static/* \
                /data/web_static/releases/{}/'.format(filename, filename))
            run('rm -rf /data/web_static/releases/{}/web_static'
                .format(filename))
            run('rm -rf /data/web_static/current')
            run('ln -s /data/web_static/releases/{} /data/web_static/current'
                .format(filename))
            return True
        except Exception:
            return False
    return False
