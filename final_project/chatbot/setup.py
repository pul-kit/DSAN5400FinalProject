from setuptools import setup, find_packages

setup(
    name='chatbot',  # Replace with your package's name
    version='0.1',  # Your package's version
    author='Group',  # Your name
    description='Chatbot for instructions',  # A brief description of your package
    long_description=open('README.md').read(),  # A long description, usually from README
    long_description_content_type='text/markdown',  # Type of the long description
    packages=find_packages(exclude=('tests', 'docs')),  # Automatically find package modules
    install_requires=[
        # List of dependencies required by your package
        # For example: 'numpy>=1.18.1', 'pandas>=1.0.3'
    ],
    classifiers=[
        # Classifiers help users find your project by categorizing it.
        # For a list of valid classifiers, see: https://pypi.org/classifiers/
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.9',  # Minimum version requirement of Python
)