FROM python:3

COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt
RUN pip3 install "dask-geomodeling==2.2.2" --no-deps

WORKDIR /code
VOLUME /code