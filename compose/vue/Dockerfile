FROM node

COPY ./compose/vue/copy.sh /copy.sh
RUN sed -i 's/\r//' /copy.sh
RUN chmod +x /copy.sh

COPY ./frontend /app

WORKDIR /app

RUN npm install && npm run build

CMD /copy.sh

