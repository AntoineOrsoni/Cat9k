# Importing the variable file in the dir Variable
import sys
import os
import inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
dirParent = os.path.dirname(currentdir)
dirVariable = dirParent + "/Variables"
sys.path.insert(0, dirVariable)

from argparse import ArgumentParser
from SparkVariables import *
from SparkFunctions import *

arguments = sys.argv


print("room ID :" + roomID_SoftwareProject)

resp = post_message("Configuration has changed !", roomID_SoftwareProject, bearer_Bot)
resp = post_message_markdown("> Changes were made by " + str(arguments[9]) + " using " + str(arguments[7]), roomID_SoftwareProject, bearer_Bot)
resp = post_message_markdown("Antoine <3 !", roomID_SoftwareProject, bearer_Bot)

print("resp = " + resp.text)

