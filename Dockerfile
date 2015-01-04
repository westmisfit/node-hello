FROM misfit/cloud_nodejs

RUN mkdir -p /work/logs
WORKDIR /work

ENV PORT=8080
EXPOSE 8080

ADD . /work
RUN cd /work; npm install

CMD node index.js
