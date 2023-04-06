#!/usr/bin/python3
"""
file to practice use of Fabric and tar command
to create an archive
"""
from fabric.api import *
import time


def do_pack():
    """task that creates an archive using tar
    and will be ran by fabric
    """
    timestr = time.strftime("%Y%m%d%H%M%S")
    try:
        local("mkdir -p versions")
        local("tar -cvzf versions/web_static_{}\
.tgz web_static/".format(timestr))
        return ("versions/web_static_{}.tgz".format(timestr))
    except Exception as e:
        return None
