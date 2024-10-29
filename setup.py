from setuptools import setup, find_packages

setup(
    name = "myModule",
    version= "0.1",
    author="Caleb Okon",
    author_email="<your.email@example.com>",
    description="Learning how to create python packages",
    long_description=open('README.md').read(),  
    long_description_content_type="text/markdown",
    url="https://github.com/<yourusername>/<packages>",  
    packages=find_packages(exclude=["test*"]), 
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License", 
        "Operating System :: OS Independent"
    ],  
    install_requires=["Numpy"]
)