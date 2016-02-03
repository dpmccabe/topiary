# Copyright (c) 2014. Mount Sinai School of Medicine
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import print_function
import os
import sys

from setuptools import setup, find_packages

readme_dir = os.path.dirname(__file__)
readme_filename = os.path.join(readme_dir, 'README.md')

try:
    with open(readme_filename, 'r') as f:
        readme = f.read()
except:
    readme = ""

try:
    import pypandoc
    readme = pypandoc.convert(readme, to='rst', format='md')
except:
    print(
        "Conversion of long_description from MD to reStructuredText failed...")


building_docs_on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

if building_docs_on_rtd:
    # we're going to use mock objects for all modules
    # which come with Python versions 3.3+ but require
    # a separate package before that
    major_version, minor_version = sys.version_info[:2]
    if major_version < 3 or minor_version < 3:
        required_packages = ["mock"]
    else:
        required_packages = []
else:
    required_packages = [
        'numpy >=1.7',
        'pandas >=0.13.1',
        'mhctools >=0.1.8',
        'varcode >=0.3.17',
        'nose >=1.3.6',
        'gtfparse >=0.0.4'
    ]

if __name__ == '__main__':
    setup(
        name='topiary',
        version="0.0.15",
        description="Predict cancer epitopes from cancer sequence data",
        author="Alex Rubinsteyn, Tavi Nathanson",
        author_email="alex {dot} rubinsteyn {at} gmail {dot} com",
        url="https://github.com/hammerlab/topiary",
        license="http://www.apache.org/licenses/LICENSE-2.0.html",
        classifiers=[
            'Development Status :: 3 - Alpha',
            'Environment :: Console',
            'Operating System :: OS Independent',
            'Intended Audience :: Science/Research',
            'License :: OSI Approved :: Apache Software License',
            'Programming Language :: Python',
            'Topic :: Scientific/Engineering :: Bio-Informatics',
        ],
        install_requires=required_packages,
        long_description=readme,
        packages=find_packages(exclude="test"),
        scripts=[
            'scripts/topiary'
        ],
    )
