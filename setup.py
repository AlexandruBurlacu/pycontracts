import setuptools

with open("README.md") as f_ptr:
    long_description = f_ptr.read()

setuptools.setup(
    name="pycontracts",
    version="0.1.5rc1",
    author="Alex Burlacu",
    author_email="alexburlacu96@gmail.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: Apache2 License",
        "Operating System :: OS Independent",
    ]
)

