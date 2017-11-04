FROM node

COPY ./compose/vue/build_and_wait.sh /build_and_wait.sh
RUN sed -i 's/\r//' /build_and_wait.sh
RUN chmod +x /build_and_wait.sh

COPY ./frontend /app

WORKDIR /app

CMD /build_and_wait.sh
