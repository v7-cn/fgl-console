from setuptools import find_packages, setup

setup(
    name="engine",
    packages=find_packages(exclude=["engine_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud"
    ],
    extras_require={"dev": ["dagit", "pytest"]},
)
