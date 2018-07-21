'''
externs.py

This file contains functions for use with all major external commands to be run.

'''
from base import baseClass, dprint
import saneConf
import subprocess


def labelAndComposite(inputFilename, text, offsetx, offsety, outputFilename):
    cmd=["convert", 
        inputFilename,
        "-pointsize", "20",
        "-font", "Verdana",
        "-background", "none",
        "-gravity", "SouthEast",
        "-density", "120",
        "-fill", "white",
        "label:@" + text,
        "-geometry", offsetx + offsety,
        "-composite", outputFilename
        ]
    dprint(cmd) 
    p = subprocess.Popen(cmd,stdout=subprocess.PIPE)
    return p

def getWallpaper():
    cmd = ["osascript", "src/osx/getBg.osa"]
    p = subprocess.Popen(cmd,stdout=subprocess.PIPE)
    return p.stdout.readlines()


def setWallpaper(path):
    cmd = ["wallpaper", "path"]
    subprocess.Popen(cmd)


def shell(cmd):
    dprint(cmd)
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    return p
    