#!/usr/bin/python3
""" Writes a function to deploy web_static website using fabric
"""
from fabric.api import run, put, env
import os
env.hosts = ['ubuntu@100.25.177.60', 'ubuntu@54.87.205.15']


def do_deploy(archive_path):
    """ Deploys web to remote host using fabric
    """
    if not os.path.exists(archive_path):
        return False
    put_result = put(archive_path, '/tmp/')
    filename = archive_path.split('/')[-1]
    remote_folder = '/data/web_static/releases/' + filename.split('.')[0]
    run_a = run('mkdir -p {}'.format(remote_folder))
    run_b = run('tar -xzf /tmp/{} -C {}'.format(filename, remote_folder))
    run_c = run('rm -f /tmp/{}'.format(filename))
    run_d = run('rm -f /data/web_static/current')
    run_e = run('ln -s {}/web_static /data/web_static/current'
                .format(remote_folder))
    if False in [put_result.failed, run_a.failed, run_b.failed, run_c.failed,
                 run_d.failed, run_e.failed]:
        return False
    return True
