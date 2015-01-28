import os
from setuptools import setup, find_packages
import uuid

requirements_path = os.path.join(
    os.path.dirname(__file__),
    'requirements.txt',
)
try:
    from pip.req import parse_requirements
    requirements = [
        str(req.req) for req in parse_requirements(
            requirements_path,
            session=uuid.uuid1()
        )
    ]
except ImportError:
    requirements = []
    with open(requirements_path, 'r') as in_:
        requirements = [
            req for req in in_.readlines()
            if not req.startswith('-')
            and not req.startswith('#')
        ]

setup(
    name='taskwarrior-timebook-hook',
    version='0.3',
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
    install_requires=requirements,
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'taskwarrior_timebook_hook = taskwarrior_timebook_hook:cmdline',
            'taskwarrior_timebook_hook_debug = taskwarrior_timebook_hook:cmdline_debug'
        ],
    },
)
