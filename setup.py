from setuptools import find_packages,setup # Imports packaging tools
from typing import List # Imports type hinting for lists

HYPEN_E_DOT='-e .' # Constant used to identify editable mode trigger

def get_requirements(file_path:str)->List[str]: # Function to process requirements
    '''
    this function will return the list of requirements
    '''
    requirements=[] # Initialize empty list
    with open(file_path) as file_obj: # Open the requirements file
        requirements=file_obj.readlines() # Read all lines
        requirements=[req.replace("\n","") for req in requirements] # Remove line breaks

        if HYPEN_E_DOT in requirements: # Check if '-e .' is in the list
            requirements.remove(HYPEN_E_DOT) # Remove it so it isn't installed as a package
    
    return requirements # Return the cleaned list of dependencies

setup(
name='mlproject', # Name of your project
version='0.0.1', # Project version
author='sltan', # Your name
author_email='sltanbrhane50@gmail.com', # Your email
packages=find_packages(), # Automatically finds your project folders
install_requires=get_requirements('requirements.txt') # Loads libraries from your file
)