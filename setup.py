from githubstats.__init__ import __version__
try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

setup(
    description=("Interactive Vizualizations and Stats of GitHub's Newest, "
                 "Most Popular Repos."),
    author='Donne Martin',
    url='https://github.com/donnemartin/viz',
    download_url='https://github.com/donnemartin/viz',
    author_email='donne.martin@gmail.com',
    version=__version__,
    license='Apache 2.0',
    install_requires=[
        'click>=5.1',
        'colorama>=0.3.3',
        'docopt>=0.6.2',
        'geocoder>=1.7.1',
        'github3.py==1.0.0a2',
        'pillow>=3.0.0',
    ],
    extras_require={
        'testing': [
            'mock>=1.0.1',
            'tox>=1.9.2'
        ],
    },
    entry_points={
        'console_scripts':
            'gh = githubstats.github_stats_cli:GitHubStatsCli.cli'
    },
    packages=find_packages(),
    scripts=[],
    name='githubstats',
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)