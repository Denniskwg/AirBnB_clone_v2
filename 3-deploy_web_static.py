#!/usr/bin/python3
"""creates and distributes an archive to two
web servers using the function deploy
"""


from fabric.api import *
import os
do_pack = __import__("1-pack_web_static").do_pack
do_deploy = __import__("2-do_deploy_web_static").do_deploy
env.hosts = ["54.237.98.199", "100.26.152.160"]


def deploy():
    """deploys to two servers using
    two imported functions
    """
    archive = do_pack()
    if not os.path.exists(archive):
        return False
    return do_deploy(archive)
