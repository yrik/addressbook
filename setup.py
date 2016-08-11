from setuptools import setup

setup(
    name='addressbook',
    version='0.01',
    description='A package that provides API to manage addressbook records',
    url='http://github.com/yrik/addressbook',
    author='Yuri Kriachko',
    author_email='iurii.kriachko@gmail.com',
    license='MIT',
    packages=['addressbook'],
    test_suite='nose.collector',
    tests_require=['nose'],
    zip_safe=False,
)
