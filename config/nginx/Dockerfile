FROM nginx
LABEL MAINTAINER="Ryan | ryan.abolfazl@gmail.com"

COPY nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]