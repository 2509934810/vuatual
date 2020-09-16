from setuptools import setup, find_packages


setup(
    name="vuatual",
    version="1.0.0",
    install_requires=[
        "pytest==5.4.1",
        "click==7.1.2",
        "selenium==3.141.0",
        "PyMySQL==0.10.0",
        "requests==2.24.0",
        "ruamel.yaml==0.16.12",
    ],
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        "pytest11": ["Vuatual = vuatual.plugin"],
        "console_scripts": ["vuatual = vuatual.run:entrypoint"],
    },
    classifiers=["Framework :: Pytest"],
)
