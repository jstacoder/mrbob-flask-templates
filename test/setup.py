from setuptools import setup, find_packages

def get_long_description():
    return open('README.rst','r').read()

config = {
    'name':new,
    'version':'0.0.1',
    'author':'Kyle Roux',
    'author_email':'kyle@level2designs.com',
    'packages': find_packages(),
    'include_package_data': True,
    'description': '',
    'long_description': get_long_description(),
    'install_requires': [
            'Flask',
    ]
    # uncomment to add scripts to install
    #'entry_points': {
    #'console_scripts': [
    #'script_name = foo.bar:function',]}
}

setup(**config)
