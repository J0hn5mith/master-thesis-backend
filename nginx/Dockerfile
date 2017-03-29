FROM tutum/nginx
RUN rm /etc/nginx/sites-enabled/default
ADD sites-enabled/ /etc/nginx/sites-enabled
#TODO don't user them from here, because insecure
COPY nginx.crt /etc/nginx/
COPY nginx.key /etc/nginx/
