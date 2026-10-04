from __future__ import annotations

from setuptools import find_packages, setup


setup(
    name="chatbot-ai",
    version="0.2.0",
    description="Professional chatbot starter with NLP, intent routing, memory, and extensible architecture",
    packages=find_packages(),
    include_package_data=True,
    python_requires=">=3.10",
    entry_points={
        "console_scripts": [
            "chatbot-ai=chatbot.app:main",
        ]
    },
)
