
FROM registry.inventec/proxy/ubuntu:22.04

# Install dependencies
RUN apt-get update && \
    apt-get install -y git build-essential libpcap-dev 

# Build tcpcopy
RUN git clone https://github.com/session-replay-tools/tcpcopy.git /tcpcopy && \
    cd /tcpcopy && \
    ./configure && \
    make && \
    make install && \
    chmod +x /usr/local/tcpcopy/sbin/tcpcopy 
    
COPY entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
