# with the setup.py i can make the project to py package
# Setup.py will find src.__init__.py
from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)-> List['str']:
    '''
    this function will return the list of requirements
    '''
    e_dot = "-e ."
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","")for req in requirements]
        
        if e_dot in requirements:
            requirements.remove(e_dot)
    return requirements

setup(
    name = 'dsproject',
    version = '0.0.1',
    author = 'Arajo',
    author_email = '0707ara.j@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')
    
)