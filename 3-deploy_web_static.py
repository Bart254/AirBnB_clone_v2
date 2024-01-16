#!/usr/bin/python3
""" Packs and deploys web_static files on remote servers
"""
from fabric.api import env
do_pack = __import__('1-pack_web_static').do_pack
do_deploy = __import__('2-do_deploy_web_static').do_deploy
env.hosts = ['ubuntu@100.25.177.60', 'ubuntu@54.87.205.15']


def deploy():
    """ Packs and deploys web_static files
    """
    archive_path = do_pack()
    if not archive_path:
        return False
    result = do_deploy(archive_path)
    return result
