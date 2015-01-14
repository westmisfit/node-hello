FROM misfit/cloud_nodejs

# pre install node modules
ADD package.json /work/
RUN cd /work; npm install

# make logs dir
RUN mkdir -p /work/logs
WORKDIR /work

# copy src
ADD . /work

ENV PORT 8080

EXPOSE 8080

# run web server on $PORT
CMD node index.js
