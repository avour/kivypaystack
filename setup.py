from setuptools import setup
from pypaystack import version

setup(name='pypaystack',
    version=version.__version__,
    description='Python wrapper for Paystack API',
    url='https://github.com/edwardpopoola/pypaystack',
    author=version.__author__,
    author_email='edwardpopoola@gmail.com',
    license=version.__license__,
    test_suite='nose.collector',
    tests_require=['nose'],
    install_requires=['requests'],
    packages=['pypaystack'],
    zip_safe=False
    )

