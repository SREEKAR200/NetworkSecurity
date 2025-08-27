from setuptools import find_packages,setup
from typing import List

def get_requirements() -> List[str]:
    requirements_lst:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            lines=file.readlines()
            for line in lines:
                requirements=line.strip()
                if requirements and requirements!='-e .':
                    requirements_lst.append(requirements)
    except FileNotFoundError:
        print("requirements.txt not found")
    return requirements_lst

print(get_requirements())

setup(
    name='NetworkSecurity',
    version="0.0.1",
    author="Sreekar Kannepalli",
    packages=find_packages(),
    install_requires=get_requirements()
)