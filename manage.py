#!/usr/bin/env python
#import is used to import function 
import os
import sys

if __name__ == "___________main____________":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dipy_web.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
