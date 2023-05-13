from setuptools import setup

setup(
    name='dailyPic',
    version='0.1.0',
    description='A python library to obtain daily images from Unplash',
    author='Wingware',
    author_email='wingwaresoftware@gmail.com',
    url='https://github.com/Wingwaresoftware/dailypic/',
    packages=['dailypic'],
    install_requires=[
        'requests',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
