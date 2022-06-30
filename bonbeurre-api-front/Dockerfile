FROM node:8-alpine

WORKDIR  /bonbeurreApiFront

ADD package.json /bonbeurreApiFront/package.json

RUN npm config set registry http://registry.npmjs.org

RUN npm install

ADD . /bonbeurreApiFront

EXPOSE 3000

CMD ["npm","run","start"]
