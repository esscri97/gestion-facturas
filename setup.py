from setuptools import setup, find_packages

setup(
    name='gestion-facturas',
    version='1.0.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        "colorama==0.4.6",
        "iniconfig==2.1.0",
        "packaging==25.0",
        "pluggy==1.6.0",
        "Pygments==2.19.2",
        "pytest==8.4.1",
        "setuptools==80.9.0"
        ],
    author="David Escrivá",
    author_email="david97escriva@gmail.com",
    description='Herramienta CLI para administrar usuarios y facturas con base de datos PostgreSQL y soporte Docker',
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/esscri97/gestion-facturas",
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10',
)