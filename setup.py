from setuptools import setup

setup(
    name="project",
    version="0.0.1",
    packages=["project"],
    package_dir={"": "src"},
    install_requires=[
        "ipykernel==6.15.2",    
        "black==22.8.0",
    ],
)
