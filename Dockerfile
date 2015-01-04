FROM misfit/cloud_nodejs

RUN mkdir /work

ADD . /work

EXPOSE 8080

CMD PORT=8080 node index.js
