FROM java:7-jdk
MAINTAINER chohan@yelp.com

RUN apt-get update && \
	apt-get install -y \
		git \
		ant \
		make \
		maven \
		python \
		python-setuptools \
		python-pip \
		libsnappy1 \
		libsnappy-dev \
		python-snappy

RUN pip install unittest2

ADD . /code

WORKDIR /code

RUN mvn install -DskipTests

RUN /code/lang/py/setup.py install

RUN cd /code/lang/py && ant build

RUN cd /code/lang/py/ && ant test

RUN mkdir -p /build/interop/data

RUN cd /code/lang/py && ant interop-data-generate

RUN cd /code/lang/py && ant interop-data-test
