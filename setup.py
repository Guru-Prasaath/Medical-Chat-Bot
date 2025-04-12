from setuptools import find_packages, setup

setup(
    name='Generative AI Project',
    version='0.0.0',
    author='Guru Prasaath',
    author_email='guruprasaath.dilli@gmail.com',
    packages=find_packages(),  # This automatically finds packages in the current directory
    install_requires=[
    'sentence-transformers==2.2.2',
    'flask',
    'pypdf',
    'python-dotenv',
    'pinecone[grpc]',
    'langchain',
    'langchain-pinecone',
    'langchain_community',
    'langchain_openai',
    'langchain_experimental',  # Fixed typo here
],
)

