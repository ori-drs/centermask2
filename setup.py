# ## ! DO NOT MANUALLY INVOKE THIS setup.py, USE CATKIN INSTEAD

# from distutils.core import setup
# from catkin_pkg.python_setup import generate_distutils_setup

# # fetch values from package.xml
# setup_args = generate_distutils_setup(
#     packages=['centermask',
#     ],
#     package_dir={'': ''})

# setup(**setup_args)


from setuptools import setup

setup(
    name='centermask',
    version='0.1.0',    
    description='A example Python package',
    # url='https://github.com/shuds13/pyexample',
    author='Mark Finean',
    author_email='shudson@anl.gov',
    license='BSD 2-clause',
    packages=['pyexample'],
    install_requires=['torch',
                      'detectron2',
                      'fvcore'                     
                      ],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',  
        'Operating System :: POSIX :: Linux',        
        # 'Programming Language :: Python :: 2',
        # 'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)