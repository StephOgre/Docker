FROM python:3.12

COPY requirements.txt /tmp/

RUN pip install -r /tmp/requirements.txt

WORKDIR /app

COPY . . 

CMD ["streamlit", "run", "st.py","--server.port", "3838"]