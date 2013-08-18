from distutils.core import setup
from pip.req import parse_requirements

reqs = map(str, parse_requirements("requirements.txt"))

setup(
    name="Nerds4Life",
    version="1.0",
    packages=["nerds"],
    install_requires=reqs
)
