from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="desafio-projeto",
    version="0.0.1",
    author="Thamyres Magalhães",
    author_email="thamyres-alves.14@hotmail.com",
    description="Desafio de projeto criação de pacotes em Python",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Thamyresarm/dio-formacao-Python/tree/master/DesafiosdeProjetos/DesafioDescomplicandoCriacaoPacotes",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)