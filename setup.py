from setuptools import setup

setup(
    name="task-cli",
    version="0.1",
    py_modules=["main"],
    entry_points={
        "console_scripts": [
            "task-cli = main:main",
        ],
    },
)
