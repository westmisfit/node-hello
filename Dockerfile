FROM misfit/cloud_nodejs

RUN mkdir -p /work/logs

ADD . /work

EXPOSE 8080

WORKDIR /work

RUN npm install

CMD PORT=8080 node index.js
