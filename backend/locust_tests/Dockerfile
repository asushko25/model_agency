FROM locustio/locust

WORKDIR /mnt/locust_tests

ENV PYTHONPATH /mnt

# install small requirements for locust testing
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copy locust tests files into the container
COPY . .
