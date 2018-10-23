from setuptools import setup

setup(
    name='data_delivery_cli',
    version='0.0',
    py_modules=['data_delivery'],
    install_requires=[
        'Click'
    ],
    entry_points='''
        [console_scripts]
        data_delivery=cli:data_delivery
    '''
)