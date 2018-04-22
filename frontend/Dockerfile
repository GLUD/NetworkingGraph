FROM heroku/heroku:16
RUN curl -sL https://deb.nodesource.com/setup_7.x | bash -
RUN apt-get update && apt-get install -y \
    nodejs \
    && nodejs -v \
    && npm --version  \
    && rm -rf /var/lib/apt/lists/*

# Add our code
ADD ./ /opt/webapp/
WORKDIR /opt/webapp

RUN npm install \
    && npm run build \
    && rm -rf node_modules
RUN npm install express

CMD node serverexpress.js

# @link: https://hub.docker.com/r/heroku/heroku/
# docker build -t networkinggraph .
# docker run -ti -p 8003:8003 -e PORT=8003 networkinggraph
# docker run -ti networkinggraph /bin/bash
# @link: https://devcenter.heroku.com/articles/container-registry-and-runtime
# heroku container:push web
# heroku open
# heroku logs
