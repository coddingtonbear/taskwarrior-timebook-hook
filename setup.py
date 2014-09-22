from setuptools import setup, find_packages

setup(
    name='taskwarrior-timebook-hook',
    version='0.2',
    url='https://github.com/coddingtonbear/taskwarrior-timebook-hook',
    description=(
        'Track your tasks as Timebook entries',
    ),
    author='Adam Coddington',
    author_email='me@adamcoddington.net',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'taskwarrior_timebook_hook = taskwarrior_timebook_hook:cmdline'
        ],
    },
)
