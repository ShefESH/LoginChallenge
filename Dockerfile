FROM python:latest
RUN apt update

RUN apt install -y bash nano iproute2
COPY . /var/www/LoginChallenge/
RUN chmod +x /var/www/LoginChallenge/start.sh
WORKDIR /var/www/LoginChallenge/web
RUN pip install -r /var/www/LoginChallenge/requirements.txt

ENV FLASK_APP="app.py"
EXPOSE 5000
ENTRYPOINT ["/var/www/LoginChallenge/start.sh"]
