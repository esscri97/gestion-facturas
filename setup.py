from setuptools import setup, find_packages

setup(
    name="juegos_azar",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "colorama==0.4.6",
        "iniconfig==2.1.0",
        "numpy==2.2.6",
        "packaging==25.0",
        "pluggy==1.6.0",
        "Pygments==2.19.1",
        "pytest==8.4.0",
        "setuptools==80.9.0"
        ],
    author="David Escrivá",
    author_email="david97escriva@gmail.com",
    description="Una librería con juegos de azar escritos en Python",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/esscri97/juegos_azar",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
)