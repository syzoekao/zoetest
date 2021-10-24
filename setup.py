# from distutils.core import setup
from setuptools import setup

setup(
    name='zoetest',
    version='1.0',
    description='Testing install package on GitHub',
    author='Zoe Cow',
    install_requires=['numpy>=1.18',
                      'cython'],
    python_requires='>=3.9',
)
