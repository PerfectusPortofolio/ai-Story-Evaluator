from setuptools import setup, find_packages

setup(
    name="narrative-ai-cli",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "openai",
        "click"
    ],
    entry_points={
        "console_scripts": [
            "narrative-ai=narrative_ai.cli:main",
        ],
    },
    author="Perfctus David",
    description="CLI tool that analyzes storytelling structure, tone, humor, and creativity using AI",
    python_requires=">=3.8",
)
