#!/usr/bin/python3
"""deploys an archive to two remote
servers
"""

from fabric.api import *
import os
env.hosts = ["54.237.98.199", "100.26.152.160"]


def do_deploy(archive_path):
    flag = 1
    if os.path.exists(archive_path):
        r = put(archive_path, "/tmp/web_static_20230406173415.tgz")
        if r.failed:
            flag = 0
        r = sudo("mkdir -p /data/web_static/releases/\
web_static_20230406173415")
        if r.failed:
            flag = 0
        r = sudo("tar -zxf /tmp/web_static_20230406173415\
.tgz -C /data/web_static/releases/web_static_20230406173415")
        if r.failed:
            flag = 0
        r = sudo("rm /tmp/web_static_20230406173415.tgz")
        if r.failed:
            flag = 0
        r = sudo("mv /data/web_static/releases/web_static_20230406173415\
/web_static/* /data/web_static/releases/web_static_20230406173415")
        if r.failed:
            flag = 0
        r = sudo("rm -rf /data/web_static/releases/web_static_20230406173415\
/web_static/")
        if r.failed:
            flag = 0
        r = sudo("rm /data/web_static/current")
        if r.failed:
            flag = 0
        r = sudo("ln -s /data/web_static/releases\
/web_static_20230406173415 /data/web_static/current")
        if r.failed:
            flag = 0

        if flag == 1:
            return True
        else:
            return False
    else:
        return False
