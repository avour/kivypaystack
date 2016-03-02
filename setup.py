from setuptools import setup

setup(name='pypaystack',
      version='0.11',
      description='Python wrapper for Paystack API',
      url='https://github.com/edwardpopoola/pypaystack',
      author='Edward Popoola',
      author_email='edwardpopoola@gmail.com',
      license='MIT',
      install_requires=['requests', 'json'],
      packages=['pypaystack'],
      zip_safe=False)

