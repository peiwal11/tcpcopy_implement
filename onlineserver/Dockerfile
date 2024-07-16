
FROM registry.inventec/proxy/ubuntu:22.04

# Install dependencies
RUN apt-get update && \
    apt-get install -y git build-essential libpcap-dev 

# Clone tcpcopy repository
RUN git clone https://github.com/session-replay-tools/tcpcopy.git /tcpcopy

# Build tcpcopy
RUN cd /tcpcopy && \
    ./configure && \
    make && \
    make install


RUN chmod +x /usr/local/tcpcopy/sbin/tcpcopy 
COPY entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
