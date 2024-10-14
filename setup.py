from setuptools import setup, find_packages

setup(
    name='ryena',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'ryena=ryena.cli:main',  # Entry point for the ryena command
        ],
    },
    install_requires=[],
    author='Your Name',
    author_email='your.email@example.com',
    description='A command-line interface for various services.',
)

