from setuptools import setup, find_packages

setup(name='greenaddress-recovery',
      version='0.1',
      description='GreenAddress recovery tool',
      url='https://github.com/greenaddress/garecovery',
      author='GreenAddress',
      author_email='info@greenaddress.it',
      license='MIT',
      packages=find_packages(),
      tests_require=['pytest', 'pytest-cov', 'mock', 'pep8', ],
      setup_requires=['pytest-runner', ],
      scripts=['garecovery/bin/garecovery-cli', ],
      include_package_data=True,
      zip_safe=False)
