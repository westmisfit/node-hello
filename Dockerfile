FROM misfit/cloud_nodejs

WORKDIR /work

ENV PORT 8080
EXPOSE 8080

# pre install node modules
RUN npm install -g mocha istanbul
ADD package.json /work/
RUN npm install

# make logs dir
RUN mkdir -p /work/logs

# copy src
ADD . /work

# run web server on $PORT
CMD exec node index.js
