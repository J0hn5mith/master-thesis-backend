#!/usr/bin/env python
import os
import sys
from master_thesis_backend import load_env

load_env.load_env()

if __name__ == "__main__":
    if len(sys.argv) > 0 and sys.argv[1] == 'test':
        os.environ.setdefault(
            "DJANGO_SETTINGS_MODULE", "master_thesis_backend.settings.test"
        )
    else:
        os.environ.setdefault(
            "DJANGO_SETTINGS_MODULE", "master_thesis_backend.settings"
        )

    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
