from setuptools import setup, find_packages

# Read the contents of your README file
with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='CSV-splitter',
    version='0.1.0',
    description='Splits large csv files into smaller csv files.',
    # long_description=open('README.md').read(),
    long_description='''this is a long description....''',
    long_description_content_type='text/x-rst',
    url='https://github.com/ginomcfino/CSV-splitter.git',
    author='Weiqi Ji',
    author_email='ycyberpunk2k@gmail.com',
    license='license',
    packages=find_packages(),
    classifiers=[
        'Topic :: Text Processing',
    ],
)
