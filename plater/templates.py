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
# templates.py
# -----


def dockerfile(filename='Dockerfile'):
    """
    Returns a simple Python `Dockerfile` template.
    """
    with open(filename, 'w') as f:
        f.write(f"""FROM python:3.7-slim
LABEL maintainer="my@self.com"

COPY
WORKDIR

RUN

CMD""")


def dockerignore(filename='.dockerignore'):
    """
    Returns a simple Python `.dockerignore`
    """
    with open(filename, 'w') as f:
        f.write(r"""__pycache__
*.pyc
*.pyo
*.pyd
.Python
env
pip-log.txt
pip-delete-this-directory.txt
.tox
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*,cover
*.log
.git""")


def readme(filename='README.md'):
    """
    Returns a simple `README.md` template.

    From https://www.makeareadme.com
    """
    with open(filename, 'w') as f:
        f.write("""# Foobar

Foobar is a Python library for dealing with word pluralization.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install foobar
```

## Usage

```python
import foobar

foobar.pluralize('word') # returns 'words'
foobar.pluralize('goose') # returns 'geese'
foobar.singularize('phenomena') # returns 'phenomenon'
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)""")


def actions_python(filename='pythonapp.yml'):
    """
    Returns a Python Github Actions template.
    """
    with open(filename, 'w') as f:
        f.write("""name: Python App

on: [push]

jobs:
  build:

    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v1
    - name: Set up Python 3.7
      uses: actions/setup-python@v1
      with:
        python-version: 3.7
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
    - name: Lint with flake8
      run: |
        # stop the build if there are Python syntax errors or undefined names
        flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
        # exit-zero treats all errors as warnings. The GitHub editor is 127 chars wide
        flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
    - name: Test with pytest
      run: |
        pytest -v --cov""")


def mit_license(filename='LICENSE'):
    """
    Returns a MIT License template.
    """
    with open(filename, 'w') as f:
        f.write("""MIT License

Copyright (c) 2020 Myself

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.""")


def setup(filename='setup.py'):
    """
    Returns a Python package `setup.py` template.
    """
    with open(filename, 'w') as f:
        f.write("""import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Foo",
    version="0.1",
    author="Myself",
    author_email="my@self.com",
    description="Foobar",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/foo/bar",
    packages=setuptools.find_packages(),
    entry_points={
        'console_scripts': ['foo = foo.cli:main']
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3',
)""")


def conda_env(filename='environment.yml'):
    """
    Returns a simple Conda `environment.yml` template.
    """
    with open(filename, 'w') as f:
        f.write("""name: example

dependencies:
  - python=3.7
  - numpy
  - pip:
    - pandas""")


def flask(filename='app.py'):
    """
    Returns a simple Flask template.
    """
    with open(filename, 'w') as f:
        f.write("""from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'""")


def pytorch_mnist(filename='pytorch_mnist.py'):
    """
    Returns a Pytorch MNIST Classifier template.
    """
    with open(filename, 'w') as f:
        f.write("""import torch
import torch.nn as nn
import torch.nn.functional as F
import torchvision
from torchvision import transforms, datasets


def load_mnist():
    train = datasets.MNIST('../../data', train=True, download=True,
                           transform=transforms.Compose([
                           transforms.ToTensor()]))

    test = datasets.MNIST('../../data', train=False, download=True,
                          transform=transforms.Compose([
                          transforms.ToTensor()]))


    trainset = torch.utils.data.DataLoader(train, batch_size=10, shuffle=True)
    testset = torch.utils.data.DataLoader(test, batch_size=10, shuffle=False)

    return trainset, testset


class Net(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(28*28, 64)
        self.fc2 = nn.Linear(64, 64)
        self.fc3 = nn.Linear(64, 64)
        self.fc4 = nn.Linear(64, 10)

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = F.relu(self.fc3(x))
        x = self.fc4(x)

        return F.log_softmax(x, dim=1)


if __name__ == '__main__':

    net = Net()

    X = torch.rand((28, 28))
    X = X.view(-1, 28*28)
    output = net(X)
    print(output)
""")


def tensorflow_mnist(filename='tensorflow_mnist'):
    """
    Returns a Tensorflow MNIST Classifier template.
    """
    with open(filename, 'w') as f:
        f.write("""from __future__ import absolute_import, division, print_function, unicode_literals

import tensorflow as tf


mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28, 28)),
  tf.keras.layers.Dense(128, activation='relu'),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
model.fit(x_train, y_train, epochs=5)
model.evaluate(x_test,  y_test, verbose=2)
""")


def bash(filename='script.sh'):
    """
    Returns a VERY simple bash script template.
    """
    with open(filename, 'w') as f:
        f.write("""#!/bin/bash

echo "Hello!"
""")


def html(filename='index.html'):
    """
    Returns a simple HTML5 template.
    """
    with open(filename, 'w') as f:
        f.write("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>

</body>
</html>""")
