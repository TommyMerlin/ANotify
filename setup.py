from setuptools import setup, find_packages

setup(
    name='anotify',
    version='0.1.9',
    packages=find_packages(),
    install_requires=[
        'requests>=2.15.1',
    ],
    author='7ommy',
    author_email='tommymerlin0920@gmail.com',
    description='Send notifications by multiple channels',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/TommyMerlin/ANotify',
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
    python_requires='>=3.6',
)
