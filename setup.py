from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf8") as fh:
    long_description = fh.read()

setup(
    name="qtstylish",
    version="0.1.1",
    description="Modern styles for PyQt5.",
    author="Adam Rose",
    author_email="adam.e.rose@hotmail.com",
    url="https://github.com/adamerose/qtstylish",
    packages=find_packages(),
    include_package_data=True,
    long_description=long_description,
    long_description_content_type="text/markdown",
    exclude_package_data={'': ['.gitignore']},
    # Using this instead of MANIFEST.in - https://pypi.org/project/setuptools-git/
    setup_requires=['setuptools-git'],
    install_requires=[
        "PyQt5",
    ],
)
