# 0x0F. Load balancer
A load balancer is mechanism that helps to distribute web load/traffic from an enterprise app or website to different servers in order to enhance performance and prevent service failure. There are two major categories of load balancers, namely hardware load balancers and software load balancers.
## Hardware load balancers
These comprise of devices (such as switches and routers) or specially dedicated computer hardware which are used to distribute client load into the server infrastructure. They are often used in conjuction with software load balancers.
## Software load balancers
They run either on dedicated hardware load balancer machines or on the server infrastructure itself and serve as the interface between the client and the servers, in order to distribute the load across the servers. They are powered by three major algorithms; Weight Scheduling, Rouding Robin and Least Connection First Scheduling.
* Weight Scheduling: assigns weight to each server according to hardware specification and distributes load according to weights.
* Rounding Robin: In an infrastructure where the hardware specs are fairly uniform, distributes load in a sequential order to each server.
* Least Connection First: Distributes load according to persistent connections on each server, so at any given time the least loaded server is prioritized for load distribution.
## Task details to be updated
