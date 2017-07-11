import sys, os

basedir = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, basedir)

from beefactoryws import app as application

