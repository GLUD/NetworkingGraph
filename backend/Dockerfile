FROM heroku/heroku:16
RUN apt-get update && apt-get install -y \
    python3-pip\
    traceroute\
    && pip3 --version \
<<<<<<< HEAD
    #&& pip3 install --upgrade pip \
    && pip3 --version \
=======
>>>>>>> 78037d6d1fff00b3372f31819125f0b7c7111de4
    && rm -rf /var/lib/apt/lists/*

# Add our code
ADD ./ /opt/webapp/
WORKDIR /opt/webapp

RUN pip3 install -r requirements.txt

CMD ./start.sh

# @link: https://hub.docker.com/r/heroku/heroku/
# docker build -t webscraper .
# docker run -ti -p 8000:8000 -e PORT=8000 webscraper
# docker run -ti webscraper /bin/bash
# @link: https://devcenter.heroku.com/articles/container-registry-and-runtime
# heroku container:push webscraper
# heroku open
# heroku logs
