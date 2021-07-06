import setuptools
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="P_CombiningPValuesFinal",
    version="0.1.3.2",
    author="Breya McGlown",
    author_email="bswlker2@memphis.edu",
    description="Six fundamental statistics and combination p value functionality",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/StatsGirl/Master2021/tree/main/Python",
    project_urls={
        "Bug Tracker": "https://github.com/StatsGirl/Master2021/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)