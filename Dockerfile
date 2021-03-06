FROM tnir/mysqlclient

RUN pip install flask \
  && pip install flask-mysql \
  && pip install flask_table

WORKDIR /stuff
COPY . .  
# VOLUME /stuff

EXPOSE 5000

CMD ["python","main.py"]
