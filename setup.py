import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="welkin-python", # Replace with your own username
    version="0.0.1",
    author="Sonu George",
    author_email="sonu.g@spericorn.com",
    description="Welkin Python package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sonugspericorn/welkin-python",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    install_requires=[
        'arrow',
        'PyJWT',
        'requests'
        ],
    python_requires='>=3.6',
)
