#@author:Akhil P Jacob
#HLRobotics-Automation
import git
import cv2
import subprocess
import sys

def update():
    try:       
        print("HLEngine:updating MATTBot 2020......")
        git_dir = "../../../MATTBot/"
        g = git.cmd.Git(git_dir)
        g.pull()
        print("HLEngine:done updating ......")
        img = cv2.imread('HLEngine.png')
        cv2.imshow('HLEngine updates', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    except:
        return("HLEngine:cannot connect to MATTBot Server")







            


