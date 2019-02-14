from setuptools import setup
from pypaystack import version

setup(name='kivypaystack',
    version=version.__version__,
    description='Python wrapper for Paystack API',
    url='https://github.com/avour/kivypaystack',
    author=version.__author__,
    author_email='avour123@gmail.com',
    license=version.__license__,
    test_suite='nose.collector',
    tests_require=['nose'],
    install_requires=['requests'],
    packages=['kivypaystack'],
    zip_safe=False
    )

