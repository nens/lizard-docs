FROM sphinxdoc/sphinx-latexpdf:8.0.2
# Pin the docker tag to use Python 3.12 to work
# around PyPi sub-dependencies with no 3.13 wheels

COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt
RUN pip3 install "dask-geomodeling==2.3.0" --no-deps

WORKDIR /code
