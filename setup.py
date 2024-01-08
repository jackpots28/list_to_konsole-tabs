from setuptools import setup

setup(
    name='list_to_konsole-tabs',
    version='0.1.0',    
    description='A python package for converting newline files into konsole-tabs',
    url='',
    author='Jack Sims',
    author_email='jack.sims@dillards.com',
    license='BSD 2-clause',
    packages=['list_to_konsole-tabs'],
    install_requires=['argparse',                     
                      ],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',  
        'Operating System :: POSIX :: Linux',        
        'Programming Language :: Python :: 3.8.x',
    ],
)