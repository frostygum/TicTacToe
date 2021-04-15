from setuptools import setup, find_packages
from pip.req import parse_requirements
from pip.exceptions import InstallationError

try:
    requirements = parse_requirements("requirements.txt")
    install_requires = [str(r.req) for r in requirements]
except InstallationError:
    install_requires = []

try:
    long_description = open("README.rst").read()
except IOError:
    long_description = ""

setup(
    name="TicTacToe",
    version="0.1.0",
    description="A Multiplayer TicTacToe Game using TCP",
    license="MIT",
    author="Author name",
    packages=find_packages(),
    install_requires=install_requires,
    long_description=long_description
)
