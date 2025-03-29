import setuptools
with open("README.md", "r", encoding="utf=-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "Text-Summarizer"
AUTHOR_USER_NAME = "Laaksh1205"
SRC_REPO = "textsummarizer"
AUTHOR_EMAIL = "23je0516@iitism.ac.in"

#this below code look for the local package setup,
#it will look for this constructor file in every folder & will install it as my local package

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A simpe python package for NLP app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/Laaksh1205/Text-Summarizer",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
)


# packages=setuptools.find_packages(where="src"),
#     classifiers=[
#         "Programming Language :: Python :: 3",
#         "License :: OSI Approved :: MIT License",
#         "Operating System :: OS Independent",
#     ],
#     python_requires=">=3.6",
#     include_package_data=True,
#     install_requires=[
#         "transformers",
#         "nltk",
#         "tqdm",
#         "click",
#         "beautifulsoup4",
#     ],