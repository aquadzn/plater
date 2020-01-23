# Plater
![](https://github.com/aquadzn/plater/workflows/Python%20package/badge.svg)

📋 Easily create a starter file template for different project

# Installation
Requires **Python 3.6+** 🤗

```bash
pip install plater
```

# Usage

```python
plater -t readme  # one template

plater -t dockerfile dockerignore  # two templates

plater -t pytorch_mnist tensorflow_mnist -f pytorch.py tf.py  # two templates and rename both files
```

# Contributing
Feel free contribute to this project by forking this repository and add your template on the following files:

* [templates.py](https://github.com/aquadzn/plater/edit/master/plater/templates.py)
* [plater.py](https://github.com/aquadzn/plater/edit/master/plater/plater.py)

# To-do

* Do a more complete template finder by using GitHun API or a Python wrapper in order to make requests and return repository as result. Allow user to specify a repository and clone it (or just download files needed).