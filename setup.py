from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA example python package', 
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url= 'https://github.com/Abdelrahman-Awad/MYPACKAGE',
    author='Abdelrahman Tarek',
    author_email='abdelrahmantk0@gmail.com'
)