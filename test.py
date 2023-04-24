#!/usr/bin/python3

from fabric.api import *

def create():
    local("mkdir dennis")
