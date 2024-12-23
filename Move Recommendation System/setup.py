from setuptools import setup

with open("README.md","r",encoding = 'utf-8') as fh:
    long_description = fh.read()

AUTHOR = 'Rishabh Upadhyay'
SRC_REPO = 'src'
LIST_OF_REQUIREMENTS = ['streamlit']

setup(
    name = SRC_REPO,
    version = '0.0.1',
    author = 'Rishabh Upadhyay',
    author_email = 'rishabh.292002@gmail.com',
    description = 'It is a tool that suggests movies to users based on their preferences and interests. It uses algorithms to analyze data like user ratings, reviews, watch history, and movie attributes',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    package = [SRC_REPO],
    python_requires = '>=3.7',
    install_requires = LIST_OF_REQUIREMENTS,
)