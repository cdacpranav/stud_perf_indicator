from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    """This function will return the list of requirements"""
    try:
        with open(file_path, 'r') as file_obj:
            requirements = [req.strip() for req in file_obj.readlines()]
            if HYPEN_E_DOT in requirements:
                requirements.remove(HYPEN_E_DOT)
            
            print("Requirements Installed Successfully...")
            return requirements
    except FileNotFoundError:
        raise FileNotFoundError(f"{file_path} not found. Please ensure the file exists.")
    except Exception as e:
        raise Exception(f"An error occurred while reading {file_path}: {e}")


setup(
    name = 'StudentPerformanceIndicator',
    version = '1.0.0',
    author = 'PRASANNA',
    author_email = 'harkep20@outlook.com',
    packages = find_packages(),
    install_requires = get_requirements("requirements.txt")
    
)
