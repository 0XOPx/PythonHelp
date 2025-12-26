from setuptools import setup, find_packages

# These variables match your requested format
__version__ = "1.0.0"  # Supports (number) or (number)a(alphanumber)
__author__ = "Your Name"

setup(
    name="Your-Package-Name",
    version=__version__,
    author=__author__,
    author_email="your.email@example.com",
    description="A short description of your project",
    long_description=open("README.md").read() if open("README.md") else "Project description here",
    long_description_content_type="text/markdown",
    url="https://github.com/YourUsername/YourRepo",
    packages=find_packages(), 
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    install_requires=[], # Add external dependencies here
)
