from setuptools import setup, find_packages

setup(
    name="ACIT4420-MorningMessage",
    version="0.1",
    packages=find_packages(),  # Automatically find all packages in your project
    include_package_data=True,  # Include non-Python files specified in MANIFEST.in (if any)
    description="A simple CLI tool to send morning greetings to people",
    author="Carl Petter Mørch-Reiersen",
    author_email="camor2778@oslomet.no",
    install_requires=[
        # List your project's dependencies here, if any
    ],
    entry_points={
        'console_scripts': [
            'morning_greetings=morning_greetings.main:main',  # Points directly to the main function in main.py
        ],
    },
)
