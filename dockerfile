FROM python:3.7-slim
RUN pip install flask
RUN pip install flask-mysql
RUN pip install flask-cors
RUN mkdir templates
RUN mkdir static
COPY app.py /app.py
COPY templates/*  /templates/
RUN chmod -R a+rwx templates
CMD ["python","app.py"]