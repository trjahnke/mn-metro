import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mn-metro", # Replace with your own username
    version="0.0.1",
    author="Tristan Jahnke",
    author_email="trjahnke@gmail.com",
    description="A wrapper for the Minnesota Metro API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/trjahnke/mn-metro",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)