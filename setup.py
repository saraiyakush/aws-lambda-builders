#!/usr/bin/env python
import io
import re
import os
from setuptools import setup, find_packages


def read(*filenames, **kwargs):
    encoding = kwargs.get("encoding", "utf-8")
    sep = kwargs.get("sep", os.linesep)
    buf = []
    for filename in filenames:
        with io.open(filename, encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)


def read_requirements(req="base.txt"):
    content = read(os.path.join("requirements", req))
    return [line for line in content.split(os.linesep) if not line.strip().startswith("#")]


def read_version():
    content = read(os.path.join(os.path.dirname(__file__), "aws_lambda_builders", "__init__.py"))
    return re.search(r"__version__ = \"([^'\"]+)", content).group(1)


cmd_name = "lambda-builders"
if os.getenv("LAMBDA_BUILDERS_DEV"):
    # We are installing in a dev environment
    cmd_name = "lambda-builders-dev"

setup(
    name="aws_lambda_builders",
    version=read_version(),
    description=(
        "Python library to compile, build & package AWS Lambda functions for " "several runtimes & frameworks."
    ),
    long_description=read("README.md"),
    author="Amazon Web Services",
    author_email="aws-sam-developers@amazon.com",
    url="https://github.com/awslabs/aws-lambda-builders",
    license="Apache License 2.0",
    packages=find_packages(exclude=["tests.*", "tests"]),
    keywords="AWS Lambda Functions Building",
    # Support 3.8 or greater
    python_requires=(">=3.8"),
    entry_points={"console_scripts": ["{}=aws_lambda_builders.__main__:main".format(cmd_name)]},
    install_requires=read_requirements("base.txt") + read_requirements("python_pip.txt"),
    extras_require={"dev": read_requirements("dev.txt")},
    include_package_data=True,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Environment :: Other Environment",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Topic :: Internet",
        "Topic :: Software Development :: Build Tools",
        "Topic :: Utilities",
    ],
)
