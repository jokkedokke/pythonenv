from setuptools import setup

setup(
    name='cmd_example',
    version='0.0.1a',
    py_modules=['cmd_example'],
    install_requires=[
        'Click',
        'boto3',
    ],
    entry_points='''
        [console_scripts]
        cmdExample=cmdExample:doStuff
    '''
)
