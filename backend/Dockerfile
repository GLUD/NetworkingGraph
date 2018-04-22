FROM heroku/heroku:16
RUN apt-get update && apt-get install -y \
    python3-pip \
    && pip3 --version \
    && rm -rf /var/lib/apt/lists/*

# Add our code
ADD ./ /opt/webapp/
WORKDIR /opt/webapp

CMD pip3 install -r requirements.txt
CMD ./start.sh

# @link: https://hub.docker.com/r/heroku/heroku/
# docker build -t webscraper .
# docker run -ti -p 8080:8080 -e PORT=8080 webscraper
# docker run -ti webscraper /bin/bash
# @link: https://devcenter.heroku.com/articles/container-registry-and-runtime
# heroku container:push webscraper
# heroku open
# heroku logs
