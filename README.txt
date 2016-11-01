Apache Avro™ is a data serialization system.

Learn more about Avro, please visit our website at:

  http://avro.apache.org/

To contribute to Avro, please read:

  https://cwiki.apache.org/confluence/display/AVRO/How+To+Contribute

=================================================================
For Yelp usage, we use python version and added some data type support, which can be used in data pipeline project. All changes are in lang/py/.  

Promote to Yelp pypi: 
(Waiting for promote_to_pypi job upgrade, here is the temporary solution)
1. Git clone this repo to your dev box.
2. Update @AVRO_VERSION@ in lang/py/setup.py
3. In the repo directory, run cmd (will build tarball and wheel):
	python lang/py/setup.py bdist_wheel
	python lang/py/setup.py sdist
4. Run cmd to promote to Yelp pypi:
	upload-to-pypi dist/avro-[version-number].tar.gz dist/avro-[version-number]-py26-none-any.whl
