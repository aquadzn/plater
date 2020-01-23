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
# plater.py
# -----

import argparse
import inspect

from . import templates


DICT = {
    "dockerfile": templates.dockerfile,
    "dockerignore": templates.dockerignore,
    "readme": templates.readme,
    "actions_python": templates.actions_python,
    "mit_license": templates.mit_license,
    "setup": templates.setup,
    "conda_env": templates.conda_env,
    "flask": templates.flask,
    "pytorch_mnist": templates.pytorch_mnist,
    "tensorflow_mnist": templates.tensorflow_mnist,
    "bash": templates.bash,
    "html": templates.html,
}


def generate_template(args):
    """
    Creates file of chosen template.
    """
    if len(args.template) == 1:
        print(f"Creating {''.join(args.template)} template ...")
        if args.filename is not None:
            DICT.get(
                ''.join(args.template),
                lambda: 'Invalid function!'
            )(args.filename)
        else:
            DICT.get(''.join(args.template), lambda: 'Invalid function!')()

    else:
        print(f"Creating {' - '.join(args.template)} template ...")
        for i in args.template:
            if args.filename is not None:
                for j in args.filename:
                    DICT.get(i, lambda: 'Invalid function!')(j)
            else:
                DICT.get(i, lambda: 'Invalid function!')()


def get_args():
    """
    Returns the CLI arguments.
    """
    functions_list = [x.__name__ for x in templates.__dict__.values()
                      if inspect.isfunction(x)]

    parser = argparse.ArgumentParser(
        description="If you use both flags,\
                    number of args for each flag must be the same."
    )
    parser.add_argument(
        '-t',
        '--template',
        nargs='+',
        metavar='Name of template',
        help=f"Select one or more template in {functions_list}.",
        required=True,
        choices=functions_list
    )
    parser.add_argument(
        '-f',
        '--filename',
        nargs='+',
        metavar='Output filename',
        help="Select custom filename. Must be as long as template argument."
    )

    return parser.parse_args()
