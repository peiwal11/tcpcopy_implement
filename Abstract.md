# TCPCOPY

## Reference:[https://github.com/session-replay-tools/tcpcopy](https://github.com/session-replay-tools/tcpcopy)     

## Objection
To evaluate the performance and behavior of `tcpcopy` and `intercept` when containerized under different configurations, ensuring they function correctly and handle network traffic as expected.

## Experiment Process

### Configurations Implemented

1. **Online server on Server A, Target server on Server B, Assistant server on Server C:**
   - (1) Each server running on the host.
   - Each server running in a Docker container:
     - (2) With PostgreSQL service
     - (3) With Python service

2. **Online server on Server A, Target server, and Assistant server on Server B:**
   - (4) Target and Assistant servers are assigned new static IPs. Both servers are placed on the same bridge network. Ports are mapped out on the Server B host to facilitate communication with the Online server.

### Experiment Details

#### Configuration (4) Observations

- On the target server, packets captured indicate that it can no longer establish a standard three-way handshake with the client.
- On the assistant server, the sequence numbers do not start from 1, differing from previous observations when these servers were separated.

### Important Considerations for TCPCOPY Containerize

**Set Network Mode to Host:**
- **Reason:** If the network mode is not set to host, there could be issues with IP mapping, preventing `tcpcopy` and `intercept` from correctly capturing and handling traffic.
- **Action:** Configure the containers to use the host network mode, allowing `tcpcopy` and `intercept` to access network traffic as if they were running directly on the host.

**Add Capability to Container to Have Necessary Permission:**   
    - online server   port 9999 provide service  
    - target server service on 10.191.7.16:10231   
    - assistant server on 10.191.7.16    
- Online server:
  ```   
   docker run --rm --net="host" --cap-add=NET_RAW --cap-add=NET_ADMIN newtcpcopy -x 9999-10.191.7.16:10231 -s 10.191.7.16     
  ```   
-  Assistant server:
   ```   
    docker run --rm --net="host" --cap-add=NET_RAW --cap-add=NET_ADMIN intercept -i eth0 -F 'tcp and src port 10231'
   ```   

Reason for --cap-add=NET_RAW:   
Packet capture occurs at the datalink layer. This capability allows the capture of raw packets, not just TCP packets.

### Experiment Results for Different Configurations      
#### PG Scenario Observations   
- Online Server: Packets captured from the online server's network interface show communication with the client and assistant server, and fakes client traffic to the target server.    
- Target Server: Packets captured from the target server's network interface are purportedly sent from clients but actually originate from the online server.      
- Assistant Server: Packets captured from the assistant server's network interface show continuous communication with the online server.    

#### Python Scenario Observations 
- Online Server: Packets captured from the online server's network interface show communication with the client and assistant server, and fakes client traffic to the target server.   
- Target Server: Packets captured from the target server's network interface show that it believes it is directly communicating with the client, but the source MAC address is from the online server.      
- Assistant Server: Packets captured from the assistant server's network interface show packets routed through it from the target to the client, with the source MAC address from the target server.    

## Conclusion   
When running each server in separate containers on different servers, as in configurations (1), (2), and (3), the functionality remains intact. However, in configuration (4), placing both the target and assistant servers in different containers on the same server but under different conditions leads to unexpected behavior:         

- The target server fails to establish a standard three-way handshake with the client.   
- The assistant server exhibits sequence numbers that do not start from 1, differing from previous observations when these servers were separated.   
- To ensure correct functionality of tcpcopy and intercept when containerized, it is crucial to set the network mode to host and add the necessary permissions to the containers.
 
## Tips   
- The assistant server uses port 36524 to communicate with the online server.   
- The online server does not establish a TCP connection with the assistant server, even though they communicate with each other constantly.   
- The online server communicates with the assistant server before sending fake traffic to the target server.  
- The online server does not establish a TCP connection with the target server.   
- The target server believes it has a normal connection with the client.   
