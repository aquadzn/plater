import os
from unittest.mock import patch

import plater


def test_cli():
    with patch('argparse._sys.argv', ['plater', '-t', 'readme dockerfile flask']):
        assert os.path.isfile('README.md') == True
        assert os.path.isfile('Dockerfile') == True
        assert os.path.isfile('app.py') == True
