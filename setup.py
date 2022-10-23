# new version to pypi (pip install twine):
# rm -rf dist && python setup.py sdist && python -m twine upload dist/*
import os
import setuptools

readme = os.path.join(os.path.dirname(__file__), "README.md")
with open(readme, "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mintapi",
    description="a screen-scraping API for Mint.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    version="2.9",
    packages=["mintapi"],
    license="The MIT License",
    author="Michael Rooney",
    author_email="mrooney.mintapi@rowk.com",
    url="https://github.com/mintapi/mintapi",
    install_requires=[
        "configargparse>=1.5.0",
        "oathtool>=2.3.0",
        "pandas>=1.0.0",
        "requests>=2.28.0",
        "selenium>=4.3.0,<5.0.0",
        "selenium-requests>=2.0.0",
        "xmltodict>=0.13.0",
        "keyring>=23.7.0",
    ],
    python_requires=">=3.6",
    entry_points=dict(
        console_scripts=[
            "mintapi = mintapi.cli:main",
        ],
    ),
)
