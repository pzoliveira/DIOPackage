from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="calculadora",
    version="0.0.1",
    author="Pericles Zapata de Oliveira",
    author_email="pzoliveira@outlook.com",
    description="Simple calculator",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pzoliveira/DIOPackage.git",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)