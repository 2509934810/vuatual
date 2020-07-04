from setuptools import setup, find_packages


setup(
    name="vuatual",
    version="1.0.0",
    install_requires=["pytest==5.4.3", "click==7.1.2"],
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        "pytest11": ["Vuatual = vuatual.plugin"],
        "console_scripts": ["vuatual = vuatual.run:entrypoint"],
    },
    classifiers=["Framework :: Pytest"],
)
