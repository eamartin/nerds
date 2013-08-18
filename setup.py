from distutils.core import setup
from pip.req import parse_requirements

reqs = parse_requirements("requirements.txt")
reqs = [str(ir.req) for ir in reqs]

setup(
    name="Nerds4Life",
    version="1.0",
    packages=["nerds"],
    install_requires=reqs
)
