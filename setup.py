from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.3'
DESCRIPTION = 'PyTextBin is a versatile Python library facilitating seamless conversion between text, binary, JSON, base64, xml and CSV formats with ease.'

# Setting up
setup(
    name="PyTextBin",
    version=VERSION,
    author="Collins O. Odhiambo",
    author_email="<comon928@gmail.com>",
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[''],
    keywords=['PyTextBin', 'csv', 'xmml', 'base64', 'text', 'json', 'binary'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)

