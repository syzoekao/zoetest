# from distutils.core import setup
from setuptools import setup

setup(
    name='zoetest',
    version='1.0',
    description='Testing install package on GitHub',
    author='Zoe Cow',
    install_requires=[# 'cython',
                      'numpy>=1.18'],
    python_requires='>=3.9',
)
