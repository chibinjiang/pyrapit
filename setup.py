from setuptools import setup, find_packages
from os import path
from rapit import __version__
DIR = path.dirname(path.abspath(__file__))
INSTALL_PACKAGES = open(path.join(DIR, 'requirements.txt')).read().splitlines()

with open(path.join(DIR, 'README.md')) as f:
    README = f.read()

setup(
    name='rapit',
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    description="RESTful API Integration Testing",
    long_description=README,
    long_description_content_type='text/markdown',
    install_requires=INSTALL_PACKAGES,
    version=__version__,
    url='https://github.com/chibinjiang/rapit',
    author='zhibin.jiang',
    author_email='jiangzhibin2014.xujie@gmail.com',
    keywords=['restful-api', 'continuous-integration', 'requests', 'integration-testing'],
    # tests_require=[
    #     'pytest',
    #     'pytest-cov',
    #     'pytest-sugar'
    # ],
    package_data={
        # include json and pkl files
        '': ['*.json', 'models/*.pkl', 'models/*.json'],
    },
    include_package_data=True,
    python_requires='>=3'
)
