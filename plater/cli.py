#!/usr/bin/env python3

# Plater
# -----
# Easily create a starter file template for different project
# -----
# https://github.com/aquadzn/plater
# William Jacques
# -----
# Licensed under MIT License
# -----
# cli.py
# -----

import sys

from . import plater


def main():
    """
    Main function.
    """
    # https://github.com/twintproject/twint/blob/master/twint/cli.py#L293
    version = ".".join(str(v) for v in sys.version_info[:2])
    if float(version) < 3.6:
        print("Plater requires Python version 3.6+")
        sys.exit(0)

    plater.generate_template(plater.get_args())
