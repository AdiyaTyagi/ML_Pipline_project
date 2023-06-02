from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = "-e ."

def get_requirements(filepath: str) ->List[str]:
    requirements = []

    with open(filepath) as filr_obj:
        requirements = filr_obj.readlines()
        requirements = [i.replace("\n", "") for i in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)


setup(name='ML_Pipeline_project',
      version= '0.0.1',
      description='Machine Learning Pipeline Project',
      author='Shivan Kumar',
      author_email="adiya.trivedi.10@gmail.com",
      url='https://github.com/AdiyaTyagi',
      packages=find_packages(),
      install_requirements= get_requirements('requirements.txt')
      )
