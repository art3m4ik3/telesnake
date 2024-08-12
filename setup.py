from setuptools import setup, find_packages

setup(
    name="Telesnake",
    version="0.1",
    packages=find_packages(),
    install_requires=["aiohttp"],
    description="Telegram API wrapper",
    author="art3m4ik3",
    author_email="art3m4ik3@gmail.com",
    url="https://github.com/yourusername/yourrepository",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
