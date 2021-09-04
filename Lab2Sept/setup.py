from setuptools import find_packages, setup

setup(
    name="Lab2",
    version="1.0",
    packages=find_packages(include=['modules_serializer', 'modules_serializer.*']),
    entry_points={
        'console_scripts': [
            'myParser=modules_serializer.entrypoint:main',
        ],
    },
    install_requires=[
        "appdirs==1.4.4",
        "attrs==21.2.0",
        "coverage==5.5",
        "distlib==0.3.2",
        "entrypoints==0.3",
        "filelock==3.0.12",
        "iniconfig==1.1.1",
        "packaging==21.0",
        "pluggy==0.13.1",
        "py==1.10.0",
        "pyparsing==2.4.7",
        "pytest==6.2.3",
        "pytest-cov==2.11.1",
        "pytomlpp==1.0.3",
        "PyYAML==5.4.1",
        "simplejson==3.16.0",
        "six==1.16.0",
        "toml==0.10.2",
        "virtualenv==20.0.17",
    ]
)