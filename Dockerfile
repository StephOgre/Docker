FROM python:3.12

COPY requirements.txt /tmp/

RUN pip install -r /tmp/requirements.txt

WORKDIR /app

COPY . . 

RUN curl -SL https://minio.lab.sspcloud.fr/ogrestephane225/diffusion/drop00.tar.gz -o drop00.tar.gz && tar -xzvf drop00.tar.gz && rm -rf drop00.tar.gz

CMD ["streamlit", "run", "st.py","--server.port", "3838"]