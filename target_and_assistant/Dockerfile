FROM registry.inventec/proxy/ubuntu:latest


#install dependencies

RUN apt-get update && \
    apt-get install -y git build-essential libpcap-dev

# Clone intercept repository
RUN git clone https://github.com/session-replay-tools/intercept.git /intercept

# Build intercept
RUN cd /intercept && \
    ./configure && \
    make && \
    make install



# Set entrypoint to intercept

ENTRYPOINT ["/usr/local/intercept/sbin/intercept"]
