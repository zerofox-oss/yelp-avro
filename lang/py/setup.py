#! /usr/bin/env python

# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
# 
# http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from setuptools import setup
from setuptools import find_packages
from sys import version_info
import os

install_requires = ['six']
if version_info[:2] <= (2, 5):
    install_requires.append('simplejson >= 2.0.9')

# Required since this python package is not in root dir of repo
os.chdir(os.path.dirname(os.path.abspath(__file__)))

setup(
  name = 'yelp-avro',
  version = '1.10.0',
  packages=find_packages('src', exclude=('tests*',)),
  package_dir = {'avro': 'src/avro'},
  scripts = ["scripts/avro"],

  #include_package_data=True,
  package_data={'avro': ['LICENSE', 'NOTICE']},

  # Project uses simplejson, so ensure that it gets installed or upgraded
  # on the target machine
  install_requires = install_requires,

  # we support python 2 and 3 in one package:
  options={'bdist_wheel': {'universal': 1}},

  # metadata for upload to PyPI
  author = 'Apache Avro',
  author_email = 'dev@avro.apache.org',
  description = 'Avro is a serialization and RPC framework.',
  license = 'Apache License 2.0',
  keywords = 'avro serialization rpc',
  url = 'http://avro.apache.org/',
  classifiers=[
      'License :: OSI Approved :: Apache Software License',
      'Programming Language :: Python :: 2',
      'Programming Language :: Python :: 2.7',
      'Programming Language :: Python :: 3',
      'Programming Language :: Python :: 3.5',
      'Programming Language :: Python :: Implementation :: CPython',
  ],
  extras_require = {
    'snappy': ['python-snappy'],
  },
)
