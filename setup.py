from setuptools import setup, find_packages

setup(
    name="job_crawler",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests>=2.31.0",
        "beautifulsoup4>=4.12.2",
        "pandas>=2.1.4",
    ],
    python_requires=">=3.8",
) 