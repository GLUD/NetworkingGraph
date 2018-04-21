FROM heroku/heroku:16
RUN curl -sL https://deb.nodesource.com/setup_7.x | bash -
RUN apt-get install -y \
    nodejs python3-pip && nodejs -v && npm --version
RUN pip3 install --upgrade pip

# Add our code
ADD ./ /opt/webapp/
WORKDIR /opt/webapp

CMD npm start

# @link: https://hub.docker.com/r/heroku/heroku/
# docker build -t networkinggraph .
# docker run -ti -p 8080:8080 -e PORT=8080 networkinggraph
# docker run -ti networkinggraph /bin/bash
# @link: https://devcenter.heroku.com/articles/container-registry-and-runtime
# heroku container:push web
# heroku open
