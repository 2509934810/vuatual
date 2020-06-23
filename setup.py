from setuptools import setup, find_packages


setup(
    name= "vuatual",
    version="1.0.0",
    install_requires=[
        "pytest==5.4.3",
        "click==7.1.2",
        ""
    ],
    packages=[
        "src",
        "src.cases",
        "src.core",
        "src.utils"
    ],
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "vuatual=src.run:main"
        ]
    }
)