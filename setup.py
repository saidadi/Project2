
from distutils.core import setup

setup(
    name='my_packages',
    version='0.2.1',
    description='Data analysis.',
    author='sai',
    author_email='sdadi@mail.yu.edu',
    license='MIT',
    packages=['Web_data_analysis'],
     install_requires=[
        'matplotlib>=3.0.2',
        'numpy>=1.15.2',
        'pandas>=0.23.4',
        'seaborn>=0.11.0',
        'requests>=2.31.0',
        'black>=23.11.0,'
        'lxml>=4.9.3',
        'selenium>=4.15.12',
        'beautifulsoup4>=04.12.2'
    ],
)


