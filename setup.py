from setuptools import setup

setup(name='pypaystack',
    version='0.1',
    description='Python wrapper for Paystack API',
    url='https://github.com/edwardpopoola/pypaystack',
    author='Edward Popoola',
    author_email='edwardpopoola@gmail.com',
    license='MIT',
    test_suite='nose.collector',
    tests_require=['nose'],
    install_requires=['requests[security]'],
    packages=['pypaystack'],
    zip_safe=False
    )

