#!/usr/bin/env python3

import subprocess
import sys
import platform

try:
    from Foundation import *
except ModuleNotFoundError:
    print("PyObjC is not installed!\n$ pip3 install pyobjc")



prefix = "tell application \"System Events\" to tell appearance preferences to"


def show_help():
    help_message = """
Usage: python3 dark-mode.py [command]

Commands
  <none>  Toggle dark mode
  on      Enable dark mode
  off     Disable dark mode
  status  Dark mode status
  """
    
    print(help_message)


# Gives the current status, "Dark Mode" or "Light Mode"
def status():
    try:
        # Wish I could make the line below shorter but not sure how
        status = subprocess.check_output(["defaults", "read", "-g", "AppleInterfaceStyle"], stderr=subprocess.STDOUT).decode('UTF-8')
        status = status.replace("\n", "")

    except subprocess.CalledProcessError:
        return "Light Mode"

    if status == "Dark":
        return "Dark Mode"


def set_mode(mode):
    if mode == "Null":
        mode = "not dark mode"
    
    cmd = prefix+" set dark mode to {}".format(mode)
    
    s = NSAppleScript.alloc().initWithSource_(cmd)
    s.executeAndReturnError_(None)


def main():
    if platform.system() != "Darwin":
        print("Can only be run on macOS!")
        sys.exit()

    if len(sys.argv) == 1:
        set_mode("Null")

    elif sys.argv[1] == "on":
        set_mode("True")

    elif sys.argv[1] == "off":
        set_mode("False")

    elif sys.argv[1] == "status":
        print(status())

    else:
        show_help()


if __name__=="__main__":
	main()
