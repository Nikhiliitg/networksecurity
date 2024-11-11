'''
The setup.py file is essential part of packaging and distributing Python projects.
It is used by setuptools and distutils to build and install Python packages.
'''

from setuptools import setup,find_packages
from typing import List

def get_requirements()->List[str]:
    '''
    This function will return the list of requirements
    '''
    requirement_list:List[str]=[]
    try:
        with open('requirement.txt') as file:
            lines=file.readlines()
            for line in lines:
                requirement=line.strip()
                
                if requirement and requirement!='-e .':
                    requirement_list.append(requirement)
                    
    except FileNotFoundError:
        print(f"requirement.txt file not found")
    return requirement_list
print(get_requirements())

setup(
    name='NetworkSecurity',
    version='0.0.1',
    author='Nikhil',
    author_email='d.nikhil@op.iitg.aac.in',
    packages=find_packages(),
    install_requires=get_requirements(),
)
