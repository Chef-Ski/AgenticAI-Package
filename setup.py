from setuptools import setup, find_packages

setup(
    name="agentic-core",  # ✅ Ensures we update the correct package on PyPI
    version="0.1.4",  # 🔼 Increment version (important to avoid upload conflicts)
    packages=find_packages(where="agenticai-package"),  # ✅ Correct package directory
    package_dir={"": "agentic-core"},  # ✅ Ensure the package is found correctly
    install_requires=[
        "Flask",
        "Flask-CORS",
        "pyppeteer",
        "openai",
        "requests",
        "python-dotenv",
        "nest-asyncio",
        "asgiref"
    ],
    python_requires=">=3.7",
)
