from setuptools import setup, find_packages

setup(
    name="Telesnake",
    version="0.2",
    packages=find_packages(),
    install_requires=["aiohttp"],
    description="Telegram API wrapper",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    license="MIT",
    author="art3m4ik3",
    author_email="art3m4ik3@gmail.com",
    url="https://github.com/art3m4ik3/telesnake",
    project_urls={
        "Website": "https://ll-u.ru",
        "Source code": "https://github.com/art3m4ik3/telesnake",
        "Issues": "https://github.com/art3m4ik3/telesnake/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
