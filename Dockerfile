FROM sphinxdoc/sphinx-latexpdf

COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt
RUN pip3 install "dask-geomodeling==2.3.0" --no-deps

WORKDIR /code
