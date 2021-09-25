from setuptools import setup, find_packages
from os.path import join, dirname

setup(
    name='UnlockingGame',
    version='1.0',
    packages=find_packages(),
    long_description=open(join(dirname(__file__), 'README.md')).read(),
    author="Usyapyj",
    author_email='novoselovvlad04@gmail.com',
    install_requires=['Xlib', 'pygame', 'threading'],
    python_requires='>=3.6',
    entry_points={
        'console_scripts':
            ['UnlockingGame = UnlockingGame.main:main'],
    },
    package_data={"": ["*.png"]}
)
