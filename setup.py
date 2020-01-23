import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="plater",
    version="0.3",
    author="William Jacques",
    author_email="williamjcqs8@gmail.com",
    description="Easily create a starter file template for different project",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/aquadzn/plater",
    packages=setuptools.find_packages(),
    entry_points={
        'console_scripts': ['plater = plater.plater:main']
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
