FROM centos:7
ENV LANG=en_US.UTF-8 \
    TZ=Asia/Shanghai
RUN ln -fs /usr/share/zoneinfo/${TZ} /etc/localtime \
    && echo ${TZ} > /etc/timezone

RUN yum install -y python3 python3-pip freeradius freeradius-utils freeradius-sqlite crontabs && \
    yum clean all

ADD https://github.com/just-containers/s6-overlay/releases/download/v2.2.0.1/s6-overlay-amd64-installer /tmp/
RUN chmod +x /tmp/s6-overlay-amd64-installer && /tmp/s6-overlay-amd64-installer /

COPY . /root/
COPY s6/ /
RUN pip3 install -r /root/requirements.txt

WORKDIR /root
RUN mv clients.conf /etc/raddb/ && \
    mv default /etc/raddb/sites-available/ && \
    mv radiusd.conf /etc/raddb/ && \
    mv eap /etc/raddb/mods-enabled/ && \
    mv schema.sql /etc/raddb/mods-config/sql/main/sqlite/ && \
    mv sql /etc/raddb/mods-enabled/
EXPOSE 5000/tcp 1812/udp


ENTRYPOINT ["/init"]
CMD ["flask", "run", "--host", "0.0.0.0", "--port", "5000"]
