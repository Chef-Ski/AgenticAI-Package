from setuptools import setup, find_packages

setup(
    name="agentic-core",
    version="0.1.2",  # 🔥 Increment version to avoid conflict
    author="Your Name",
    description="Scrape tweets and generate AI-based tweets.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[
        "Flask",
        "Flask-CORS",
        "pyppeteer",
        "openai",
        "requests",
        "python-dotenv",  # ✅ Fixed from "dotenv"
        "nest-asyncio",
        "asgiref"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
