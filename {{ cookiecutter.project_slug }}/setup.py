from setuptools import find_packages, setup

setup(
    name='src',
    packages=find_packages(),
    version='0.1.0',
    description='{{ cookiecutter.project_description }}',
    author='{{ cookiecutter.project_author_name }}',
    license='{% if cookiecutter.project_open_source_license == 'MIT' %}MIT{% elif cookiecutter.project_open_source_license == 'BSD-3-Clause' %}BSD-3{% endif %}',
)