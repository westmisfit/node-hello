FROM misfit/cloud_nodejs

RUN mkdir -p /work/logs

ADD . /work

RUN cd /work; npm install

EXPOSE 8080

WORKDIR /work

CMD PORT=8080 node index.js
