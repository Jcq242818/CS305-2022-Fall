<h1 align = "center"><font size='6'>CS305 Lab 14 Practice</h1>

<h1 align = "center"><font size='4'>Name: 吉辰卿  &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp ID: 11911303</h1>



## Practice 13.2 -1: (ARP & Switch)

### Build the network as below topology, do the following test on **simulation mode** of Packet-Tracer

![20221220111126](D:\Data\Tencent Files\3329500177\Image\SharePic\20221220111126.png)

- **Clear the arp table on PC0, then invoke“ping”on PC0 to reach PC1.**

<img src="D:\Data\Tencent Files\3329500177\Image\SharePic\20221220111309.png" alt="20221220111309" style="zoom:150%;" />

<img src="D:\Data\Tencent Files\3329500177\Image\SharePic\20221220111513.png" alt="20221220111513" style="zoom:150%;" />

- **Describe the transmission path of arp request and arp reply.**

**Firstly**, If PC0 wants to ping PC1, he needs to send an ICMP packet to PC1. However, the link layer part of the packet requires the MAC address of PC1. Therefore, PC0 searches its arp table but finds that there is no entry corresponding to PC1(we use arp -d to delete any arp entries). Therefore, he will send an arp request from Fa0, his only outbound link. After receiving the arp request, the switch checks that the destination address is the broadcast address (FF-FF-FF-FF-FF-FF). So it forwards the frame to all other outgoing ports. ![20221220113317](D:\Data\Tencent Files\3329500177\Image\SharePic\20221220113317.png)

**Then**, the arp request packet is then received by arp modules in all network devices on the LAN. Each of these ARP modules checks whether its IP address matches the destination IP address in the ARP packet. The matching one sends back to the query host a response ARP packet with the desired mapping **(PC1 sends an arp reply to PC0)**.

![20221220113842](D:\Data\Tencent Files\3329500177\Image\SharePic\20221220113842.png)

![20221220113953](D:\Data\Tencent Files\3329500177\Image\SharePic\20221220113953.png)

**Finally**, the query host PC0 is able to update its ARP table and send its ICMP request data packet encapsulated in a link layer frame whose destination MAC is the MAC address of the host PC1 that responded to the previous ARP request.

- **What does switch do after receive the arp request or arp reply: send back, forward or drop ? **

  The arp request is broadcast to all the outbound links except the interface from which the request is sent.

  **Answer: send forward**

- **What does router do after receive the arp request or arp reply: send back, forward or drop ?**

  Because it finds that the ip address corresponding to the arp request does not match its own ip address, it discards the request. 

  **Answer: drop**

