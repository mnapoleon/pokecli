from setuptools import setup

setup(
    name='pokecli',
    version='0.1.0',
    py_modules=['pokecli'],
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts' : [
            'pokecli = pokecli:pokecli',
        ],
    },
)