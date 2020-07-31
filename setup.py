import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="solima",
    version="0.1.0",
    author="",
    author_email="",
    description="sample package'",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/smasui-0302/python-sample-package
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points = {
        'console_scripts': ['sample_command = sample_command.sample_command:main']
    },
    python_requires='>=3.7',
)