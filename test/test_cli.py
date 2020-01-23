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
# test_cli.py
# -----

import os
import argparse

from plater import plater


def test_one_template():
    args = argparse.Namespace(template='readme', filename=None)
    plater.generate_template(args)

    assert os.path.isfile('README.md')


def test_three_templates():
    args = argparse.Namespace(template=['dockerfile', 'dockerignore', 'mit_license'], filename=None)
    plater.generate_template(args)

    assert os.path.isfile('Dockerfile')
    assert os.path.isfile('.dockerignore')
    assert os.path.isfile('LICENSE')


def test_modified_two_templates():
    args = argparse.Namespace(template=['bash', 'html'], filename=['hello.sh', 'home.html'])
    plater.generate_template(args)

    assert os.path.isfile('hello.sh')
    assert not os.path.isfile('script.sh')

    assert os.path.isfile('home.html')
    assert not os.path.isfile('index.html')
