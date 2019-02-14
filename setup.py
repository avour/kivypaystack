from setuptools import setup
from kivypaystack import version

setup(name='kivypaystack',
    version=version.__version__,
    description='A port of pypaystack to support the kivy framework',
    url='https://github.com/avour/kivypaystack',
    author=version.__author__,
    author_email='avour123@gmail.com',
    license=version.__license__,
    install_requires=['kivy'],
    packages=['kivypaystack'],
    zip_safe=False
    )
