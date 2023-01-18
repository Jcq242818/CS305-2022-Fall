<h1 align = "center"><font size='6'>CS305 Course Project: Research on IPv6 Network Protocol</h1>

<h1 align = "center"><font size='4'>Name: 吉辰卿（50%） &nbsp&nbsp张旭东（50%） &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp ID: 11911303&nbsp &nbsp 12011923</h1>



## Part 1: Basic Information about IPv6

### 1.1 Motivation of development of IPv6

​	As new subnets and IP nodes connect to the Internet at an alarming rate and are assigned unique IP addresses, the address  space represented by 32 bits is running out. To satisfy the requirement for a larger IP addresses space, a new IP protocol was developed, which was named IPv6. This was also an opportunity to improve and strengthen other aspects of IPv4 based on the operational experience accumulated in IPv4.

​	Additional motivation is that header format helps speed processing and forwarding and facilitate quality of service.

### 1.2 Characteristics of IPv6

#### 1.2.1 Larger address space

​	Different from IPv4, whose length of an IP address is only 32 bits, IPv6 increases the length of an IP address from 32 bits to 128 bits, which makes sure the world doesn't run out of IP addresses. What's more, IPv6 has introduced a new type of address called the anycast address,which can deliver datagrams to any one of a set of hosts.

#### 1.2.2 Simplified and efficient packet structure

​	The header length of IPv4 is not fixed, which is caused by the $option$ header field whose length is indefinite. The header length of IPv6 is fixed, which is 40 bytes. The 40-byte fixed-length header allows the routers to process IP packets faster, which can improve the quality of service.

#### 1.2.3 Better scalability

​		As discussed above, IPv6 fixes the header length and transfers the functionality of the option field and fragment field to its extended header, which allows more flexible processing of options to do. More functionality can be achieved by adding different extended headers.

#### 1.2.4 Flow label

​	The IPv6 packet format has a flow label field whose length is 20 bits. It is used to identify the flow of a packet and can give priority to some datagrams in a flow, or it can be used to give higher priority to some applications' datagrams over those from other applications.

#### 1.2.5 Implementation of automatic configuration and prefix re - addressing

​	On an IPv6 network, a router advertises its interface prefix to end system. End system generates an available IPv6 address for itself by using this prefix and calculating the generated interface ID, and also considers the route as its default gateway. Even if the end system that has obtained an IPv6 address is moved to another network segment, the end system can automatically change its IPv6 address through the above process.

#### 1.2.6 Support for hierarchical network structure

​		IPv6 addresses are assigned in order from IANA to RIR and then to ISP. IANA is the International Assigned Numbers Authority,  RIR is the Regional Internet Registry, and ISP is Internet Service Provider. IANA will reasonably assign IPv6 addresses to the five RIRs. Then, the RIR allocates addresses to the countries in the region reasonably. The addresses assigned to each country are then handed over to ISPs. Last, ISPs allocate IPv6 addresses to users reasonably. 

​	In this assignment process, the case that the network addresses of subnets are discontinuous can be avoided as much as possible, which can better aggregate routes and reduce the number of route entries on the backbone network.

#### 1.2.7 Better support for quality of service

​	IPv6 protocol supports quality of service better in two aspects. One is that  the priority field of IPv6 protocol has 6 bits that can be used as a priority representation and can represent 64 different priorities. The other is that the flow label field in IPv6 protocol defines a data flow based on the source and destination addresses.

​	In the early stage, a flow classifier defines a data flow only through the quintuple of source IP address, destination IP address, source port, destination port, and protocol. This definition process can be defined only after being unpackaged at the transport layer. With the flow label field, flow classification can be realized directly through the information of the network layer, which greatly improves the efficiency of flow classification.

#### 1.2.8 Native support for end-to-end security

​	The extended header of IPv6 protocol includes an authentication header and an encapsulation security clean-load header, which are defined by IPsec protocol. The network layer can implement end-to-end security through these two headers without assistances from other protocols, as is the case for IPv4 protocol.

#### 1.2.9 Support for mobile features

​	IPv6 protocol supports the mobile of end system. It means that communication can also be quickly recovered when the end system is moved to another network environment. However,it's just a concept, not in use yet.

#### 1.2.10 Other differences between IPv4 and IPv6

- ​	Fragmentation and Reassembly

  IPv4 protocol allows fragmentation in the router. However, IPv6 protocol doesn't allow this operation happened in the router. For IPv6 protocol, fragmentation is allowed only at source and destination. If the size of received IPv6 datagrams is too large, the router discards the datagram and sends back an ICMP error datagram.  Fragmentation and reassembly is a time-consuming operation, and removing this function from the router and placing it on the end system greatly speeds up IP datagram forwarding through the network.

-    Checksum in the header

  For IPv4 protocol, checksum in the header needs to be recalculated on each router. However, this will never happen for IPv6 protocol. Removing this operation will speed up the processing of IP packets.

- Option

  For IPv4 protocol, the option field is a part of the standard IP header. However, for IPv6 protocol, it is no longer a part of standard IP header. It may appear  at the location indicated by the "next header" field in the IPv6 datagram.

### 1.3 Development of IPv6

#### 1.3.1 Status of development of IPv6

- Countries actively reserve IPv6 address resources

  More than 220 countries and regional organizations in the world have applied for IPv6 addresses, which has reached more than 180,000 times of the current Internet address space, and 25.4% of the address blocks have been notified for use.

- Steady progress in building network infrastructure

  Among the 13 root DNS servers in the world, 11 of them support IPv6 protocol. Among the 1346 top-level DNS servers, 1318 of them support IPv6 protocol, which accounts for 97.9 percent of the total . The upgrade of DNS servers has laid a solid foundation for the full commercial deployment of IPv6 protocol.

- Rapidly growing commercial network scale

  At present, there are more than 29,000 active route entries of IPv6 protocol in the world, more than 11,800 autonomous regions that support IPv6 protocol, and more than 248 ISPs providing permanent access services to IPv6 protocol, basically forming an network of IPv6 protocol covering major ISPs, content service providers and economic regions.

- The content that can be accessed by IPv6 protocol becomes more and more abundant

  More than 195 million website domain names have been registered worldwide, of which 7.63 million domain names support the type  "AAAA " of record of IPv6 protocol, accounting for 3.90% of the total. Meanwhile, a growing number of mobile apps are also providing support for IPv6 protocol.

- Growing user scale

  At present, more than 94 countries have developed users of IPv6 protocol, and the total number of users is more than 250 million.

- Mobile traffic is the main growth point

  The growth of users, the expansion of network coverage and the richness of content have contributed to the significant growth of global data traffic of TPv6 protocol. The average traffic of IPv4 protocol reached 45.4 gigabytes, accounting for more than 34% of the global traffic.

- Mobile end operating systems have further improved their support for IPv6

  The latest Android and Windows Phone systems include a component  named 464xlatCLAT, which encapsulates packets of IPv4 through an tunnel of IPv6 and sends them to the gateway named NAT64 to access sources of IPv4.

#### 1.3.2 Resistance to the development of IPv6 

1. The exhaustion process of IPv4 addresses slows down

   The widespread use of classless interdomain routing and NAT has slowed the process of exhaustion of IPv4 addresses. What's more, it is difficult for the smooth evolution of the technology due to the incompatibility of IPv6 protocol and IPv4 protocol. 

2. The lack of a reasonable business model

   In the short term, it is difficult for deployers to gain benefits from technology upgrade. Moreover, technology upgrade is a complex system engineering, which requires multiple links from end to end and training of relevant technical persons.

3. The disadvantages of IPv6 protocol

   - Low efficiency

   - Security algorithms are controlled in the United States

   - The digital button can't be used to access the Internet

   - The IP addresses can't be directly represented and must be translated by DNS

   - The algorithm used to connect the network is complex

   - There is no fundamental solution to the image and sound protocol

#### 1.3.3 Status of migration from IPv4 to IPv6

​	There are three main ways to migrate from IPv4 to IPv6, which are double stack technique, tunneling technique and protocol translation technique.

- double stack technique

  <img src=".\double stack.png" style="zoom:50%;" />

  IPv6 protocol and IPv4  protocol are network layer protocols with similar functions. Both are based on the same physical platform, and there is no difference between the transport layer protocols loaded on them, which are TCP and UDP. Therefore, a host that supports both IPv6 protocol and IPv4 protocol can communicate with hosts that support IPv4 protocol and hosts that support IPv6 protocol.

- tunneling technique

  <img src=".\tunneling.png" style="zoom:50%;" />

  When an IPv6 datagram enters an IPv4 network, the IPv6 datagram is encapsulated into an IPv4 datagram. When the encapsulated IPv4 datagram leaves the IPv4 network, the data portion (IPv6 datagram) is taken out and forwarded to the destination node. The router encapsulates the IPv6 datagram into an IPv4 datagram. The source and destination addresses of the IPv4 datagram are the IPv6 addresses of the tunnel entrance and exit, respectively.

  The tunnel technique can connect the local IPv6 network through the existing Internet backbone network running IPv4 protocol, so it is the easiest technology to adopt in the early stage of the transition from IPv4 to IPv6.

- protocol translation technique

  By combining SIIT protocol translation with traditional IPv4 dynamic address translation and appropriate application layer gateway , it enables the communication for most applications between hosts that only support IPv6 and hosts that only support IPv4. 

#### 1.3.4 Difficulties in the migration process from IPv4 to IPv6

- double stack technique

  This technique has high requirements for sites,and may involve upgrade of servers and network equipment. It is a long-term evolution technology with large investment and long transformation period. In the short term, it is suitable for the upgrade of websites of IPv6 with relatively simple architecture and services. Because the codes of IPv4 and IPv6 are not exactly the same, the codes of double stacks of website applications need to be rewritten. 

- tunneling technique

  This technology requires users to install corresponding tunnel software of IPv6, which has limitations in universality and convenience. It is mainly applicable to the application environment of the C/S model or the scenario where users can install end system, but is not suitable for large-scale deployment.

### 1.4 Outside attitudes towards IPv6

- Strong support from domestic policies

  In November 2017, the General Office of the CPC Central Committee and The General Office of the State Council jointly issued the Action Plan for Promoting the Large-scale Deployment of Internet Protocol Version 6. The Action Plan calls for the formation of an independent technology system and industrial ecosystem of the next generation of Internet, the world's largest IPv6 commercial application network, and the deep integration of the next generation of Internet in various economic and social fields in 5 to 10 years.

  In October 2018, the Yunnan Provincial government issued the Implementation Opinions on Promoting the Deployment Plan of IPv6 . Through government guidance and enterprise leadership, by the end of 2020, the active users of IPv6 will exceed 20 million, accounting for more than 50% of the Internet users. By the end of 2025, networks, applications, and end system will fully support IPv6.

- Strong promotion from international policy

  1. IPv6 in American

     The US government is one of the most important users of the applications of IPv6 in the US. It has publicly declared many times that IPv6 plays a key role in the sustainable development of the Internet economy in the US, and has forced the implementation of upgrade of IPv6. The U.S. government has already issued a deadline for the military to transition to IPv6, as well as a deadline for all levels of the federal government to fully complete the support of IPv6.

  2. IPv6 in Europe

     The governments of European countries have adopted a unified policy to provide tax breaks and market information support for products that support IPv6. Europe's Third Generation Partnership has defined IPv6 as the standard addressing scheme for mobile multimedia

  3. IPv6 in other country

     The Japanese government attaches great importance to the development of IPv6, and even regards the development of IPv6 technology as a basic policy of the government's "ultra-high speed network construction and competition". In March 2001, the "E-Japan Key Plan" put forward the goal of completing the transition of the Internet to IPv6.

- Strong push from various industries

  The latest Android and Windows Phone systems include a component  named 464xlatCLAT, which encapsulates packets of IPv4 through an tunnel of IPv6 and sends them to the gateway named NAT64 to access sources of IPv4.

  IOS9 system provides applications with a "Bump in the API" programming interface to encapsulate IPv4 packets through an IPv6 tunnel and access IPv4 information sources.
  
  AT&T Wireless, Sprint, and Verizon Wireless LTE networks support IPv4/IPv6 dual stacks, while T-Mobile USA LTE networks support ipv6-only single stack. On the broadband front, AT&T, Comcast, and Google Fiber already support IPv6.

### 1.5 Application of IPv6

​	IPv6 is widely used in various fields and scenarios.

- Applications in websites and apps

  1. In the past, the server could only see the user's home gateway or 4G gateway, which lost a lot of big data. However, using IPv6 allows servers to bypass NAT and see the end user directly, which enables accurate analysis and service.

  2. The live broadcast using IPv6 eliminates the NAT process and smoother P2P sharing technique, making the user's viewing experience more smooth. Meanwhile, accurate address positioning is not only conducive to more effective traffic guidance, but also conducive to the precise delivery of personalized advertisements, and improve the security of copyright procurement and copyright protection.

     <img src=".\application in websites and apps.png" style="zoom:50%;" />

- Applications in end-to-end communication

  1. It can optimize the export of education network, ensure that the special channel of high-quality education resources is smooth, resources are delivered nearby, and improve the visiting experience of teachers and students. It can also effectively screen and classify high-quality educational resources and eliminate bad applications.

     <img src=".\application in end-end communication.png" style="zoom:50%;" />

  2. At present, due to the lack of fixed IP for home cameras, people usually need to use the cloud platform to penetrate the Intranet and realize the access to the camera from the outside network, which increases the risk of the disclosure of user privacy. IPv6 provides a separate fixed IP address for home cameras, which simplifies the network structure. People can access the camera directly from their phones, reducing the risk of third-party intervention.

     <img src=".\appication in home camera.png" style="zoom:50%;" />

- Applications in the field of IoT

  IPv6 integrates cutting-edge technologies such as artificial intelligence, big data and the Internet of Things, giving birth to new business forms, applications and scenarios such as smart city, smart transportation and ubiquitous electric Internet of Things.

  1. Smart transportation

     Due to the massive IPv6 address resources, the smart lock of shared bikes does not need to be connected for a long time. This saves power for the smart lock and helps reduce maintenance costs.

     <img src=".\application in smart transportion.png" style="zoom:50%;" />

  2. Smart lighting

     Smart lighting based on IPv6 realizes the monitor of lighting status, which can monitor the running status of all kinds of equipment and discover the faulty equipment in time. It also realizes the analysis of operation status and energy consumption to achieve the optimization of intelligent evaluation and control of lighting effect.

     <img src=".\application in smart lighting.png" style="zoom:50%;" />

  3. ubiquitous electric IoT

     Currently, more than 500 million end devices are connected to the national grid system. By 2030, it is expected to exceed 2 billion. IPv6 provides massive address resources to connect all end devices.

     <img src=".\appication in electric IoT .png" style="zoom:50%;" />

## Part 2: Advanced Topic of IPv6 -- IPSec Protocol

In this part, we will choose the<font color="#dd0000"> **Topic 3: IPSec Protocol.**</font>

#### **1. Introduction**

   IPSec is a protocol cluster proposed by the Internet Engineering Task Force (IETF) to protect the IP layer communication security architecture using the password. It provides a set of IP extensions for implementing security in the network layer for both IPv4 and IPv6. IPSec Protocol supports the following functions: 

- **Data Confidentiality:** The IPSec sender encrypts the packets before sending them over the network. 
- **Data Integrity:** IPSec verifies the packets sent by the IPSec sender to ensure that the data is not changed during transmission.  
- **Data Authentication:** The IPSec recipient can identify the origin of IPsec packets. This service depends on the integrity of the data. 
- **Reverse Replay:** The IPSec receiver can check and reject the replay packet.

​	With the rapid development of Internet, IPSec Protocol is applied in more and more fields. At the same time, the problem of Internet security is becoming more and more serious. The data on the network is very easy to be wiretapped and tampered by others. IPSec is a standard network security protocol and an open standard network architecture. It ensures secure network communication through encryption. IPSec ensures IP data security and defends against network attacks.

​	Now, IPv6 is a new Internet standard developed by the IETF for packet communication over IP. IPSec was required until RFC 6434, but its use in IPv4 has been optional. The purpose of doing so is that **IPSec can be more widely used as IPv6 becomes more popular.**The first edition of IPSec was defined in RFC2401-2409. In 2005, the second edition of the standard document was published and the new document was defined in RFC 4301 and RFC 4309.

​	Therefore, in this part, I will introduce and analyze several key aspects of IPSec protocol in detail and analyze the application of IPSec in IPv6 networks by analyzing the relevant data packets.

#### **2. Two modes of operation of IPSec**

**IPSec supports two working modes, that is Tunnel mode and Transmission mode.**

- **Tunnel mode**

   ​	Tunnel mode encrypts data between tunnel points or gateways, ensuring the security of transmittal from gateway to gateway. When data is transmitted between the client and the server, it is encrypted **only when it reaches the gateway and the remaining paths are not protected.** The entire IP packet of the client is used to calculate the AH or ESP header and is encrypted. The AH or ESP header and encrypted user data are encapsulated in a new IP packet.   

   ​	Tunnel mode uses a new packet header to encapsulate messages in order to protect the messages of a network. Based on that, tunnel mode is applicable to the communication between two gateways, shown in the Figure 9 below.

![IPSec1](.\IPSec10.png)

<div align = 'center'><b>Fig.9 The Working diagram of tunnel mode</div>

- **Transmission mode**

     ​	In the transmission mode, **IPSec provides end-to-end transmission security from the source to the destination**. In transmission mode, only the transport layer data is used to calculate the AH or ESP header. The AH or ESP header and the encrypted transport layer data are placed behind the original IP packet header. 

     ​	The transmission mode **does not change the packet header. **The source and destination IP addresses of the tunnel are the source and destination IP addresses of the final communication parties. The communication peers can only protect the messages sent by themselves, but cannot protect the messages of a network. Therefore, this mode applies only to the communication between two hosts, not to the communication between two gateways, shown in the Figure 10 below.

![IPSec2](.\IPSec11.png)
<div align = 'center'><b>Fig.10 The Working diagram of transmission mode </div>

#### **3. Three key Protocols in IPSec: AH, ESP and IKE**

   **Firstly, Let's take a look at AH and ESP, the two protocols that protect provide security protection for data packets in the IPSec protocol cluster. **

   IPSec borrows the clever feature of facsimilation. Before a user transmits a message, it uses the encryption algorithm and encryption key to transform the message. This process is called encryption. After receiving the message, the other user uses the same encryption algorithm and encryption key to restore the message to its true appearance in reverse. This process is called decryption. And the information is never presented as it is, leaving the stealer with nothing to gain. The whole process for packet sending and receiving is shown below. **In the IPSec protocol, the ESP protocol can encrypt and decrypt the datagram.**

![](.\IPSec3.png)

<div align = 'center'><b>Fig.11 The process of encrypting and decrypting data packets in IPSec </div>

​	In addition to encrypting and decrypting messages, IPSec also supports message integrity verification to prove that messages have not been tampered with. Before a user transmits a message, it processes the message using an authentication algorithm and authentication key to obtain a signature. The signature is then sent with the message. After receiving a message, the other user uses the same authentication algorithm and key to process the message and obtain a signature. Then, the signatures on both ends are compared. If the signatures on both ends are the same, it will proof that the message is not tampered during the transmission. **In the IPSec protocol, both AH and ESP protocol can verify the integrity of the datagram.**

<img src=".\IPSec4.png" alt="20221220155310" style="zoom:67%;" />

<div align = 'center'><b>Fig.12 The process of verifying the integrity of the data packets in IPSec </div>

​	**The following is a detailed description of AH and ESP protocols:**

- **Authentication Header Protocol: AH**

   ​	**AH is a security protocol at the network layer,** which provides the connectionless integrity and data source authentication for the IP datagram, and provides protection against replay situations. AH can be used independently, or in conjunction with IP encapsulation security payload **(ESP,we will mention soon)**, or by using a nested tunnel mode. In these way, security services can be provided between communication host and communication host, between communication security gateway and communication security gateway, or between security gateway and host.

   ​	AH protocol uses the authentication algorithm with the key to calculate the protected data. **Currently, it provides two authentication algorithms: MD5 (Message Digest) and SHA1(Secure Hash Algorithm)**. The key lengths of the two algorithms are 128bit and 160bit respectively. By using data integrity checks, we can determine whether a packet has been modified during transmission; Through the use of authentication mechanisms, terminal systems or network devices can authenticate users or applications and filter traffic; Authentication mechanisms also protect against address fraud and replay attacks.

   ​	However, we should know that AH protocol provides source authentication and data integrity services but does not provide confidentiality services. **Therefore, when authentication is required without confidentiality, using the AH protocol is the best option.**
   
- **Encapsulation Security Payload Protocol: ESP**

   ​	**ESP is also a security protocol at the network layer,** which is designed to provide a hybrid application of security services in both IPv4 and IPv6. ESPs in IPSec Protocol stack provide confidentiality and integrity by encrypting the data to be protected and placing this encrypted data in the data portion of the IPsec ESP. **ESP encryption adopts symmetric key encryption algorithm such as DES (Data Encryption Standard), 3DES (Triple Data Encryption Standard) and AES (Advanced Encryption Standard) to provide connectionless data integrity authentication, data source authentication, and anti-replay attack services. **Based on user security requirements, this mechanism can be used to encrypt both a transport layer segment (such as TCP, UDP, ICMP, and IGMP) and an entire IP datagram. Encapsulating the protected data is necessary to provide confidentiality for the entire raw datagram.

   ​	The ESP header can be placed after the IP header (transmission mode), or before the encapsulated IP header (tunnel mode). IANA assigns a protocol value of 50 to ESP. The protocol header that precedes the ESP header always contains this value in the next head field (IPv6) or Protocol (IPv4) field. ESP contains a non-encrypted protocol header followed by encrypted data. The encrypted data contains both the protected ESP header field and the protected user data. The user data can be the entire IP datagram or the upper-layer protocol frame of IP (such as TCP or UDP).

   ​	One of the obvious difference between the AH and ESP is that **the ESP protocol provides not only source authentication, data integrity, but also provides confidentiality services.** Because confidentiality is usually important to VPNS and other IPsec applications, so the ESP protocol is used much more widely than AH. However, the ESP can also be used independently or in combination with AH.

**Then, Let's take a look at the Key manager in IPSec protocol -- Internet Key Exchange (IKE).**

​	When a VPN has a small number of endpoints, the network administrator can manually type the security association information (encryption/authentication algorithm and key and SPI) in the SAD of that endpoint. Such a "human key method" is obviously impractical for a large VPN, which may consist of hundreds or even thousands of IPSec routers and hosts. Large, geographically dispersed deployments require an automated mechanism to generate security alliance information.**IPSec uses the Internet Key Exchange (IKE) protocol to do this work. **IKE is defined by RFC 5996.

​	Based on the Internet Security Association and Key Management Protocol (ISAKMP) framework, **IKE is a UDP-based application layer protocol that provides automatic key negotiation and IPSec SA establishment services. Moreover, IKE is a composite protocol that consists of three subprotocols: Internet Security Association and Key Management Protocol (ISAKMP), Oakley, and SKEME. **ISAKMP defines the establishment process of IKE partnerships (similar to IPSec sas). The core of the Oakley and SKEME protocols is the Diffie-Hellman (DH) algorithm, which is used to securely distribute keys and authenticate identities on the Internet to ensure data transmission security. The functions of these three subprotocols are summarized as follows.

![](.\IPSec5.png)

<div align = 'center'><b>Fig.13 Summary of functions of the three subprotocols in IKE </div>

​	So, what is the relationship between IKE and IPSec?  As IKE is an application layer protocol, its data needs to be transmitted through ISAKMP protocol to establish an IKE SA between two peers to complete identity authentication and key information exchange. Then, under the protection of the IKE SA, a pair of IPSec sas are negotiated according to the configured security protocol parameters. **After that, the data between the two peers is encrypted and transmitted through the IPSec tunnel through the ESP or AH protocol mentioned above.** The following Figure illustrates the relationship between IKE and IPSec.

![](.\IPSec6.png)

<div align = 'center'><b>Fig.14 The Relationship between IKE and IPSec </div>

​	Therefore, the ultimate goal of IKE is to dynamically establish IPSec SA between gateways through negotiation and maintain IPSec SA in real time. By using the IKE in IPSec VPN, we can reduce the number of manually configured and modified IPSec Keys and improve the management and maintenance efficiency of IPSec VPN.

#### **4. The two phases of IKE Protocol**

​	**IKE is composed of two phases: In phase 1, an IKE SA is established. In phase 2, an IPSec SA is established through the IKE SA.** 

- **Phase 1: Establishing the IKE SA**

  ​	In this phase, the two gateways negotiate to establish theIKE SA in active mode or aggressive mode, Let's first look at how this process works in the main mode. **In the main mode, IKE (Version 1) protocol uses three steps and six ISAKMP messages to establish an IKE SA,** the concrete implementation of these three steps is as follows:

  ​	**1. Negotiate the IKE safety proposal **
  
  ​	When the initiator sends a local IKE safety proposal to the corresponding peer, the responder searches for the IKE proposal that matches the initiator. If no matching IKE proposal exists, the negotiation fails. The matching principle of the IKE Peer security proposal is that the two peers have the same encryption algorithm, authentication algorithm, identity authentication method, and DH group identifier (excluding the IKE SA lifetime).
  
  ​	**2. Use the DH algorithm to exchange key materials and generate keys**
  
  ​	The two peers exchange each other's Key material using the Key Exchange and the nonce payload of the ISAKMP messages. The Key Exchange is used to exchange DH public values, and the nonce is used to transmit temporary random numbers. In the DH algorithm, IKE peers only exchange key materials but do not exchange real shared keys. **Therefore, even if a hacker steals DH value and temporary value, the shared key cannot be calculated. This is the essence of the DH algorithm.**
  
  ​	After the exchange of key materials is complete, the IKE peers start the complex key calculation process by combining the self-configured authentication methods. (Pre-shared key or digital certificate participate in the key calculation process) Then, three keys are generated:
  
  - **SKEYID_a: **The integrity authentication key for ISAKMP Message.
  - **SKEYID_e:** The encryption key for ISAKMP Message.
  - **SKEYID_d:** Used to derive the keys for IPSec packet encryption and authentication. **(This key ensures the security of the data packets encapsulated by IPSec).**
  
  ​	**3. Identity authentication**
  
  ​	The IKE peers exchange identity information through two ISAKMP messages for identity authentication. **(These identities are encrypted by SKEYID_e)**There are two authentication technologies that are commonly used:
  
  - **Pre-shared key: **The identity information of the device is an IP address or name.
  - **Digital certificate:** The identity information of the device is the certificate and Hash values of some messages encrypted using the certificate private key (commonly known as signatures).
  
  The complete process of this phase can be clearly shown as follows:

<img src=".\IPSec7.png" alt="20221220200239" style="zoom:67%;" />

<div align = 'center'><b>Fig.15 The whole process of the Phase 1 in IKE protocol(In main mode)</div>

- **Phase 2: Establishing the IPSec SA through the IKE SA**

  ​	**In Phase 2, IKE (Version 1) uses the fast exchange mode to establish an IPSec SA through three ISAKMP messages. **The specific meanings of these three messages are as follows:

  ​	**1. The initiator sends the IPSec proposal, protected data flow (ACL), and the key material to the responder.**

  ​	**2. The responder responds to the matched IPSec proposal and protected data flow, and generates the key for the IPSec SA.**

  ​	IPSec peers exchange key materials (such as the parameters of SKEYID_d, AH/ESP protocol and nonce), and then calculate their own keys to generate the keys for IPSec SA authentication. In this way, each IPSec SA has its own unique key. IPSec SA keys are derived from SKEYID_d. If SKEYID_d leaks, IPSec VPN may be violated. To improve the security of key management, IKE provides the PFS (perfect forward security) function. After PFS is enabled, an additional DH exchange is performed during IPSec SA negotiation, and a new IPSec SA key is generated to improve IPSec SA security.

  ​	**3. The initiator sends the confirmation result and starts to send IPSec (ESP) packets.**

  The complete process of this phase can be clearly shown as follows:

![IPSec8](.\IPSec8.png)

<div align = 'center'><b>Fig.16 The whole process of the Phase 2 in IKE protocol</div>

​	**Finally, it is noticed that the aggressive mode can also be selected to establish IKE SA in Phase 1.** Moreover, aggressive mode completes the Phase 1 negotiation process with only three ISAKMP messages, the whole process is shown below:

![IPSec9](.\IPSec9.png)

<div align = 'center'><b>Fig.17 The whole process of the Phase 1 in IKE protocol (In aggressive mode)</div>

​	In this mode, the initiator and responder send the IKE proposal, key information, and identity information to each other in an ISAKMP message, which improves the IKE negotiation efficiency. However, the identity information is transmitted in plain text without encryption and integrity verification. Therefore, the security of IKE SA decreases accordingly.

#### **5. The working process of AH and ESP in the two modes of IPSec in IPv6 network**

​	From above analysis, IPSec has two working modes: tunnel mode and transmission mode. So, I'll briefly discuss how AH and ESP protocols work in each of these modes.

- **Tunnel mode**

​	In tunnel mode, the original data packet to be protected is encapsulated with a new data packet, that is, the original data packet is used as the load of the new data packet. The new data packet is called tunnel data packet. In this data packet, AH authentication only confirms the source and integrity of data packets but does not provide security services for transmitted data and ESP provides confidentiality services. In addition, ESP authenticates the information behind the ESP header. Meanwhile, tunnel mode encapsulates the entire IP datagram and generates a new IP header in front of it. Therefore, the packets of AH and ESP tunnel mode in the IPv6 architecture are as follows:

<img src=".\IPSec12.png" style="zoom:150%;" />

<img src=".\IPSec13.png" style="zoom:150%;" />

<div align = 'center'><b>Fig.18 The packet structure of AH and ESP protocol separately in tunnel mode of IPSec in ipv6 <br> Above: AH packet &nbsp&nbsp&nbsp Below: ESP packet</div>

​	Of course, as mentioned in the previous section, the AH and ESP protocols can work either alone or together. Therefore, in tunnel mode, the original IP datagrams can also be encapsulated by AH and ESP protocol to form AH-ESP packets. The encapsulation process is as follows:

![](.\IPSec14.png)

<div align = 'center'><b>Fig.19 The whole process of encapsulating the original IP packet when AH and ESP are used together in tunnel mode</div>

​	After understanding the basic structure of the IPSec datagram of AH, ESP, and AH-ESP, we can briefly analyze the working process of AH and ESP through textbooks and actual packet capture. First of all, let's take a look at the description of the process of encapsulating IP datagram by these two protocols in the textbook. **(ESP provides not only the services provided by AH but also the data encryption service. Therefore, I will analyze the encapsulation process of IPSec packets encapsulated by ESP and the encapsulation process of ESP under IPv6 is similar to that of IPv4)** . We can look at a VPN network in the following scenario:

![](.\IPSec18.png)

<div align = 'center'><b>Fig.20 A scenario where the ESP protocol in is used in tunnel mode to encrypt and encapsulate IP datagrams</div>

​	We suppose router R1 receives a normal IPv4 datagram from host 172.16.1.17 (in the headquarters network), and the packet's destination is host 172.16.2.48 (in the branch office network). Router R1 converts this "plain IPv4 datagram" into an IPsec datagram using the following method:

- **Append an "ESP tail" field to the tail of the initial IPv4 datagram.** (which includes the initial header field) 
- **Encrypt the result above by using the algorithm and the key specified by SA.** (Security Association, which include the encryption and authentication algorithms and corresponding keys used by both peers).
- **Append a field called "ESP header" to the encryption quantity obtained by above process, **and the resulting package is called "enchi-lada".
- **Generate an authenticated MAC covering the entire "enchilada" using the algorithm and the key specified by the SA.**
- **Attach the MAC obtained above to the tail of the "enchilada" to form the entire payload.**
- **Finally, generate a new IP header with all the classic IPv4 header fields (usually 20 bytes in total), the new head is attached before the entire payload, shown in the figure below.**

![](.\IPSec19.png)

<div align = 'center'><b>Fig.21 The format of IPSec datagram encapsulated by ESP protocol in tunnel mode</div>

​	After examining the steps to construct an IPsec datagram through the ESP protocol, we now take a closer look at the composition of "enchilada". We see in Figure 21 that the ESP tail consists of three fields: the fill, the fill length, and the next header. Because the block password requires that the encrypted packet must be an integer multiple of the block length. By Using the padding (consisting of meaningless bytes) so that the "message" formed when it is added to the initial datagram (along with the padding length field and the next header field) is an integer multiple of the block. The fill length field indicates how much padding the receiving entity inserted (and needs to be removed). The next header field indicates the type of data (for example, UDP) contained in the payload data field. The payload data (typically the initial IP datagram) and the ESP tail are cascaded and encrypted.

​	Then, attached to this encryption unit is the ESP header, which is sent in clear text and consists of two fields: SPI field and sequence number field. The SPI field indicates to the receiving entity which SA the datagram belongs to; The receiving peer can then index its SAD with the SPI to determine the appropriate authentication/decryption algorithm and key. The sequence number field defends against replay attacks.

​	The sending entity also attaches an authentication MAC (ESP MAC field in Figure 21) to allow the receiver to verify the integrity of the sent data (that is, whether the sent data has been tampered with by a third party). As mentioned earlier, the sending entity computes a MAC across the entire "enchilada" (consisting of the ESP header, the initial IP datagram, and the ESP tail, that is, the datagram and tail with encryption). To calculate a MAC, the sender appends a secret MAC key to this "enchilada", calculates a fixed-length hash of the result and populates the ESP MAC field shown in Figure 21.

​	Note that the resulting IPSec datagram is a genuine IPv4 datagram with a traditional IPv4 header. The segment is followed by a load. But in this case, the payload consists of an ESP header, initial IP datagram, an ESP tail and an ESP authentication field (with encrypted initial datagram and ESP tail). The initial IP datagram has source IP Address 172.16.1.17 and destination IP Address 172.16.2.48. The IPSec datagram contains the initial IP address but these addresses are contained and encrypted as part of the IPSec packet load. **But in the new IP header the source and the destination IP address are the two router interfaces at the two endpoints of the tunnel, that is 200.168.1.100 and 193.68.2.23. Also, the protocol number in this new IPv4 header field is set not to TCP, UDP, or SMTP, but to 50,Indicates that this is an IPSec datagram using ESP.**

​	Finally, let's look at how the entire IPSec datagram encapsulated by ESP is received by the destination. After R1 sends the IPSec datagram into the public Internet, it passes through a number of routers before reaching the R2. **Each of these routers will process the datagram as if it were a normal datagram.** For these public Internet routers, because the destination IP address in the outer header is R2, so the final destination of this datagram is R2.

​	When receiving an IPSec packet, R2 sees that the destination IP address of the packet is R2 itself. So, R2 manage the datagram. Because the protocol field (at the far left of the IP header) is 50, R2 knows that IPSec ESP processing should be applied to the datagram. First, for enchilada, R2 uses SPI to determine which SA the datagram belongs to. Second, it calculates the MAC of the enchilada and verifies that the MAC is the same as the value in the ESP MAC field. If the two are same, R2 knows that the enchilada is from R1 and has not been tampered with. Third, it checks the ordinal field to verify that the datagram is new (and not a replayed datagram). Fourth, it decrypts the encryption unit using the decryption algorithm and key associated with the SA. Fifth, it deletes and extracts the initial ordinary IP message. Finally, it forwards the initial datagram into the branch office network toward its final destination (The IP address is 172.16.2.48).

​	Because it is difficult to analyze AH or ESP packets due to our device faults. Therefore, we can analyze related messages through a typical case by referring to the information on the Internet. The network structure of this case is as follows, which is a typical VPN network structure: **(Note that the Internet protocol used in this example is IPv4, but the IPSec protocol encapsulates IPv4 and IPv6 packets in the same way. Therefore, we only pay attention to the details of encapsulation in IPSec protocol, not to the Internet protocol IPv4 or IPv6)**

![](.\IPSec20.png)

<div align = 'center'><b>Fig.22 A typical network structure using ESP and AH protocol under the tunnel mode</div>

​	In the above network structure, the user network on the left (IP address 192.168.0.1) sends a "Ping" request and expects to receive an "Ping echo reply" from the user network on the right (IP address 172.16.0.1). Users on one side are connected to users on the other side through a VPN private line. The external gateways of users on the two sides are 1.1.1.1/24 and 2.2.2.2/24 respectively.

​	Firstly, **if the left external gateway uses ESP protocol to encapsulate the initial IP datagram to obtain IPSec packets**, then if we set up a card on the wide area network between users at both ends for packet capture detection, the captured packets will be as follows:

![](.\IPSec21.png)

<div align = 'center'><b>Fig.23 The IPSec datagram encapsulated by ESP protocol in the WAN network captured by Wireshark </div>

​	After analyzing the packet content, **it is found that the "Ping" message is encrypted and not unrecognizable, which proves that the IPSec packet has been encrypted through ESP.** Moreover, the source and destination addresses of the new IP header have changed to 1.1.1.1 and 2.2.2.2, **which makes the third party on the WAN network think that the datagram is just the message traffic between two external gateways, which hides the real IP information of the users on both sides very well.**

​	Next, **in order to compare the similarities and differences between AH and ESP protocol, we simulate that the left external gateway 1.1.1.1/24 uses the AH protocol to encapsulate the IP datagrams under tunnel mode.** Similarly, if we set up a card on the wide area network between users at both ends for packet capture detection, the captured packets will be as follows:

![](.\IPSec22.png)

<div align = 'center'><b>Fig.24 The IPSec datagram encapsulated by AH protocol in the WAN network captured by Wireshark </div>

​	After analyzing the packet content, **the AH protocol does not encrypt the data in the original IP packet. Instead, the AH protocol only adds a new IP packet header and AH header before the original IP packet header. **If a third party captures a datagram on a WAN, the ICMP message content can still be correctly analyzed. **Therefore, the AH protocol cannot encrypt the datagram and it can only verify the integrity of the received datagram.**

- **Transmission mode**

​	In transmission mode, the router does not check or process the AH in IPv6. Therefore, in the transmission mode of IPv6, the AH header is placed behind the IP header and extended headers such as "Hop by Hop", "Route", and "Segment". Meanwhile, in this mode the ESP header is inserted behind the original IP header. Therefore, the ESP header only provides security services for upper-layer protocols and does not protect the IP header. The packets of AH and ESP transmission mode in the IPv6 architecture are as follows:

![](.\IPSec15.png)

<img src=".\IPSec16.png" style="zoom:150%;" />

<div align = 'center'><b>Fig.25 The packet structure of AH and ESP protocol separately in transmission mode of IPSec in ipv6 <br> Above: AH packet &nbsp&nbsp&nbsp Below: ESP packet</div>

​	Same as tunnel mode, the AH and ESP protocols can work either alone or together. Therefore, in transmission mode, both the AH header and ESP header can be directly inserted between the IP header and the transport layer header to form AH-ESP encapsulated packets. The encapsulation process is as follows:

![](.\IPSec17.png)

<div align = 'center'><b>Fig.26 The whole process of encapsulating the original IP packet when AH and ESP are used together in transmission mode</div>

​	Based on the analysis of the packet structure of AH and ESP protocol in transmission mode, **we can see that the packet header does not change in the transmission mode, and the source and destination IP addresses of the tunnel are the source and destination IP addresses of the final communication peers. The communication peers can only protect the messages sent by themselves, but cannot protect the messages of a network.** Therefore, this mode applies only to the communication between two hosts, not between two external gateways.

## Part 3: Design and Implementation
### 3.1 Overall Network Topology

![](.\p3-1.png)

<div align = 'center'><b>Fig.27 Our whole network topology</div>

### 3.2 Composition and Configuration

​	Our network topology simulates a **simple campus network**. The whole network structure is mainly divided into the following parts (LAN): **library network, computer room network, dormitory network, information center (server) network, a VPN network and an IPV6 tunnel network.** The composition and configuration of each part are as follows:

- **The library network**

<img src=".\p3-2.png" style="zoom: 67%;" />

<div align = 'center'><b>Fig.28 library network topology</div>

​	As shown in the picture above, our library network uses a **wireless link** to simulate a scenario where different students' laptops and mobile phones are **connected to a same WiFi router**. We used the WRT300N wireless router in the Cisco simulator, which has a built-in DHCP service, so we didn't need to configure static IP addresses for the laptops and phones. Therefore, we configure the wireless router as follows:

```python
## Internet configuration(WAN):
Internet IP address: 221.0.0.2
Subnet mask: 255.255.255.0
Dafault Gateway: 221.0.0.3 
#The default gateway is the next-hop router connected to the wireless router, which is represented by Router0 in our topology

## Network Setup(LAN):
IP address: 192.168.1.1
Subnet mask: 255.255.255.0

## DHCP Server
Start IP Address: 192.168.1.100
IP Address Range: 192.168.1.100-149
Static DNS Server: 192.168.137.4 # This is the DNS Server in the information center (server) network

#Wireless information:
Network: Mixed
Network Name(SSID): ZXD
Standard Channel: 4-2.427GHz
Security Mode: WEP ## WEP Key: 0123456789
```

​	After configuring the router, we can successfully configure the network information of each mobile phone and laptop through the DHCP protocol, as shown in the figure below **(taking Laptop 1 as an example)**:

<img src=".\p3-3.png" style="zoom:67%;" />

<div align = 'center'><b>Fig.29 The network configuration of Labtop1 </div>

​	When configuring the library network, the most interesting part is how to connect the laptop to the wireless network. We need to do the following：

**1. Install a wireless card on the laptop.**

​	As shown in the figure below, we need to remove the fast Ethernet card firstly, and then drag the wireless card in the lower right corner to the appropriate slot on the Laptop.

<img src=".\p3-4.png" style="zoom: 67%;" />

<div align = 'center'><b>Fig.30 The configuration of Wireless card on the Laptop </div>

**2. Connect to the corresponding wireless network through the graphical user interface**

​	As shown below, we can find "Connect" option in the "PC Wireless" option under the desktop of the laptop. By clicking the "Refresh" button, we can view the surrounding WiFi network. Then, we click the "Connect" button to connect to the corresponding wireless network by inputting the WEP Key.

<img src=".\p3-5.png" style="zoom: 67%;" />

<div align = 'center'><b>Fig.31 The configuration of Wireless connection on the Laptop </div>

- **The computer room network**

<img src=".\p3-6.png" style="zoom:67%;" />

<div align = 'center'><b>Fig.32 computer room network topology</div>

​	As shown in the figure above, our computer room network **uses wired Ethernet**, in which four PC hosts (PC0-PC3) and a DHCP server are connected to a Ethernet switch, the other end of the switch is connected to the default gateway router **(Router 9)**, and above the gateway router is connected to a series of IPV4 routers. **(It is not shown in this figure, but is covered in the topology of the router in the following sections).**The IP addresses of the four PC hosts will be dynamically configured through the DHCP server. The corresponding configurations of the DHCP server are as follows:

```python
## The configuration of the DHCP server
Default Gateway: 192.168.4.1
DNS Server: 192.168.137.4 # This is the DNS Server in the information center (server) network
Start IP address: 192.168.4.100
Subnet Mask: 255.255.255.0
Maximum Number of Users: 50
```

​	After the DHCP server is configured, the network information of the four PC hosts can be dynamically configured, as shown in the following figure **(using PC0 as an example)** :

<img src=".\p3-7.png" style="zoom:67%;" />

<div align = 'center'><b>Fig.33 The network configuration of PC0 </div>

- **The dormitory network**

<img src=".\p3-8.png" style="zoom:67%;" />

<div align = 'center'><b>Fig.34 dormitory network topology</div>

​	As shown in the figure above, we designed a dormitory network topology on the right side of the entire network. As you can see in the figure, we still **used a wireless router WRT300N(which also supports wired Ethernet)**to connect a PC host, an IOT server **(has static IP address 192.168.25.108)**, a smartphone (which connects to the IOT server to control all IOT devices in the dormitory network), and six IOT home devices. All devices are connected to the wireless router via wired Ethernet or WiFi. Similar to the library network, the wireless router is configured as follows:

```python
## Internet configuration(WAN):
Internet IP address: 192.168.3.100
Subnet mask: 255.255.255.0
Dafault Gateway: 192.168.3.1 
#The default gateway is the next-hop router connected to the wireless router, which is represented by Router0 in our topology

## Network Setup(LAN):
IP address: 192.168.25.1
Subnet mask: 255.255.255.0

## DHCP Server
Start IP Address: 192.168.25.100
IP Address Range: 192.168.25.100-149
Static DNS Server: 192.168.137.4 # This is the DNS Server in the information center (server) network

#Wireless information:
Network: Mixed
Network Name(SSID): JCQ
Standard Channel: 10-2.457GHz
Security Mode: WEP ## WEP Key: 0123456789
```

​	Similarly, because the wireless router has a DHCP server, we no longer need to manually configure a static IP address for each device connected to the router, as shown in the figure below **(taking "摆烂王的电脑"as an example)**:

<img src=".\p3-9.png" style="zoom:67%;" />

<div align = 'center'><b>Fig.35 The network configuration of "摆烂王的电脑" </div>

​	Then, we need to be aware of the fact that since the IOT server is a **well-known end system in this LAN**, we cannot use DHCP server to configure its dynamic IP. (This is because the IP of the server cannot be changed every time the server is accessed. Otherwise, the IOT server cannot be accessed every time the IOT device is initialized). Therefore, **this IOT server has a static IP address of 192.168.25.108.**

​	In order for the mobile phone to control all the IOT devices in the dormitory by accessing the IOT server, we need to register a control user name and password for the smartphone and store it in the IOT server. The registration method is to open the desktop in the mobile phone, select "IOT Monitor". Then, we click the "sign up" button to register a new account, as shown in the figure below:

<img src=".\p3-10.png" style="zoom: 67%;" />

<div align = 'center'><b>Fig.36 Register the account and password for the smartphone to control the IOT device </div>

​		After registration, we can see the corresponding user information in the IOT server background, as shown in the figure below:

<img src=".\p3-11.png" style="zoom:67%;" />

<div align = 'center'><b>Fig.37 The information of the account and password on the IOT server </div>

​	Finally, we need to configure the corresponding control user information and the IOT server IP address information in the corresponding IOT controlled equipment, as shown below **(taking the fan as an example)**:

<img src=".\p3-12.png" style="zoom:67%;" />

<div align = 'center'><b>Fig.38 Configure the corresponding IOT server IP address and control account information on the controlled device </div>

​	In this dormitory network, we also need to pay attention to **the way these IOT devices connect to the Wireless network**. Since these IOT devices don't have a graphical user interface, we can't connect to the wireless router through the "PC Wireless" graphical window like the laptops in the library. Therefore, we need to configure the WiFi SSID and WEP Key of the corresponding wireless router **in the Wireless0 interface of IOT devices** to connect the corresponding WiFi, as shown in the figure below **(taking the fan as an example)**:

<img src=".\p3-13.png" style="zoom:67%;" />

<div align = 'center'><b>Fig.39 The way IOT devices connect to the wireless WiFi network </div>

- **The information center (server) network**

<img src=".\p3-14.png" style="zoom:67%;" />

<div align = 'center'><b>Fig.40 information center (server) network topology</div>

​	As the name implies, the information center of the school **provides various Internet services (Web server, DNS domain name resolution, Web server and FTP server) to all the computers in the subnets of the school** (excluding some IPv6 subnets, because we only do tunnel experiments on these subnets). As shown in the figure above, our information center contains four servers: Web server, FTP server, DNS server, and Email server. **Since almost all end systems can access these servers, the IP addresses of these servers must be statically configured (the figure above shows the IP address configurations of these servers).**Then I will show the configuration method of the corresponding service for each server **(see section 3.3 for the specific implementation of the corresponding service).**

​	**1. Web Server**

​	Since other end systems need a domain name to access our Web page on this Web server for convenience of memory, we need to register the domain name corresponding to this Web server on the DNS server. Of course, in order to simulate the real scenario, the domain name of the Web server we get may be an alias of it. So, we firstly need to find the canonical host name corresponding to the alias through the CNAME resource record, and then find the IP address corresponding to the canonical host name through the A resource record. These domain name resolution information of the Web server in our DNS server resource records as shown below:

```python
## resource record (RR) about the Web Server (192.168.137.2) in the DNS server (192.168.137.4)
(kesi.com, www.cisco.com, CNAME)
(www.cisco.com, 192.168.137.2, A)
```

​	After inserting these two resource records in the DNS server, other hosts in the campus network can access this Web server through the domain name of this Web server.

​	**2. FTP Server**

​	When configure the FTP server, we need to register the user name and password on the server and the user's permission to operate related files after logging in to the FTP server, as shown in the figure below **(we created a new user called jcqzxd) :**

<img src=".\p3-15.png" style="zoom: 45%;" />

<div align = 'center'><b>Fig.41 The configuration information of FTP Server</div>

​	Then, if a host in the campus network wants to access the FTP server, you only need to output the following command in the terminal **(We also will need to enter the correct user name and password to successfully log in, as shown in the section 3.3):**

```python
ftp 192.168.137.3
```

​    **3. DNS Server**

​	When configuring the DNS server, we need to insert the resource records **(Web Server and Email Server)** related to domain name resolution, as shown below **(I will explain the resource record of the Email server when explaining the configuration of the mail server):**

```python
## resource record (RR) about the Web Server (192.168.137.2) in the DNS server (192.168.137.4)
(kesi.com, www.cisco.com, CNAME)
(www.cisco.com, 192.168.137.2, A)

## resource record (RR) about the Email Server (192.168.137.5) in the DNS server (192.168.137.4)
(inmail.sustech.edu.cn, 192.168.137.5, A)
(outmail.sustech.edu.cn, 192.168.137.5, A)
(mail.sustech.edu.cn, 192.168.137.5, A)
```

​    **4. Email Server**

​	When configuring the mail server, we firstly need to fill in the domain name of the mail server, and then we need to register the corresponding user name and password for each host in the campus network (except the IPv6 tunnel host) on the Email server, as shown in the figure below:

<img src=".\p3-16.png" style="zoom:67%;" />

<div align = 'center'><b>Fig.42 The configuration information of Email Server</div>

​	After that, we also configure the  information of the user and Email server on the each host in our campus network, as shown below **(Configure mail in the Email option on the desktop, using PC0 as an example) :**

<img src=".\p3-17.png" style="zoom:67%;" />

<div align = 'center'><b>Fig.43 The configuration information of Email on PC0</div>

​	In this configuration, we found that the corresponding Incoming Mail Server information and Outgoing Mail Server information need to be configured. The two servers represent the corresponding mail server information of the receiving mail and the senting mail **(both refer to the same Email server -- mail.sustech.edu.cn, but their domain name is different. We can see the resource records in the DNS servers below).**

​	After that, we need to insert the corresponding resource record into the DNS server so that the host can successfully resolve the corresponding mail server information, as shown below:

```python
## resource record (RR) about the Email Server (192.168.137.5) in the DNS server (192.168.137.4)
(inmail.sustech.edu.cn, 192.168.137.5, A)
(outmail.sustech.edu.cn, 192.168.137.5, A)
(mail.sustech.edu.cn, 192.168.137.5, A)
```

​	As we can see, the server used to send mail and the server used to receive mail point to **the same Email server -192.168.137.5 (its domain name is mail.sustech.edu.cn).**

- **The VPN Network**

![](.\p3-18.png)

<div align = 'center'><b>Fig.44 VPN network topology</div>

​	As shown above, our VPN network will be built using the IPSec protocol stack we mentioned in Part 2. In this network, the two hosts (192.168.200.2/24 and 192.168.201.2/24) want to set up a private VPN tunnel to each other. The gateway routers on the two hosts are Router 6 and Router 10 respectively. Then, to open an IPSec tunnel, we need to perform the following configurations on the two routers. Before the configuration **(This is because the SA negotiation process is bidirectional)**, we should notice that once the IPSec tunnel between the two routers is configured, if nothing else is configured, the hosts on both sides of the tunnel will not be able to access other LANs on the campus network. **Therefore, we also need to use port multiplexing NAT technology on the two gateway routers to enable hosts on both sides to access other LAN of the campus network. The configurations of router 6 and router 10 are as follows (IPSec tunnel mode and AH and ESP protocols are used at the same time) :**

​	**1. Router 6 configuration**

```bash
#以下是配置ISAKMP策略（也就是管理连接的配置）'
R6(config)#crypto isakmp policy 1 #策略序列号为“1”，范围是1~10000，数值越小，优先级越高
R6(config-isakmp)#encryption aes #配置加密算法
R6(config-isakmp)#hash  sha  #hash命令指定验证过程中采用的散列算法
R6(config-isakmp)#authentication pre-share #声明设备认证方式为“预先共享密钥”
R6(config-isakmp)#group 2#采用DH算法的强度为group2
R6(config-isakmp)#lifetime 10000  #可选，管理连接生存周期，默认为86400s（24小时）
R6(config-isakmp)#exit
R6(config)#crypto isakmp key 6 address 1.1.1.2 #配置“预先共享密钥”
#'下面是数据连接配置'
#定义虚拟专用网保护的流量 
R6(config)#access-list 101 permit ip 192.168.200.0 0.0.0.255 192.168.201.0 0.0.0.255   
R6(config)#crypto ipsec transform-set test-set ah-sha-hmac esp-aes #数据连接协商参数，“test-set”是自定义的名称
R6(config)#crypto map test-map 1 ipsec-isakmp  #将数据连接相关配置设定为MAP，“test-map”是自定义的名字
% NOTE: This new crypto map will remain disabled until a peer
        and a valid access list have been configured.
R6(config-crypto-map)#set peer 1.1.1.2  #虚拟专用网对端地址
R6(config-crypto-map)#set transform-set test-set #将数据连接关联刚才创建的传输集
R6(config-crypto-map)#match address 101 #匹配的ACL
R6(config-crypto-map)#int gi0/0/1  #进入外部接口
R6(config-if)#crypto map test-map  #应用在外网接口
#'下面是要解决内部主机访问互联网问题'
R6(config-if)#access-list 102 deny ip 192.168.200.0 0.0.0.255 192.168.201.0 0.0.0.255 #拒绝虚拟专用网的流量
R6(config)#access-list 102 permit ip any any #放行其他任何流量
R6(config)#ip nat inside source list 102 int gi0/0/1 overload #采用端口复用的PAT方式，解决内网访问互联网的问题
#'下面是进入相关接口启用NAT功能。
R6(config)#int gi0/0/1
R6(config-if)#ip nat outside 
R6(config-if)#in gi0/0/0
R6(config-if)#ip nat inside 
```

​	**Important Note: When NAT and virtual private network (VPN) traffic both exist, NAT is matched first, and then the router match the virtual private network (VPN). Therefore, when NAT is performed on the virtual private network, the virtual private network traffic is needed to be denied.**

​	**2. Router 10 configuration**

```bash
R10(config)#crypto isakmp policy 1
R10(config-isakmp)#encryption aes
R10(config-isakmp)#hash  sha
R10(config-isakmp)#authentication pre-share
R10(config-isakmp)#group 2
R10(config-isakmp)#lifetime 10000
R10(config-isakmp)#exit
R10(config)#crypto isakmp key 6 address 100.0.0.1
R10(config)#access-list 101 permit ip 192.168.201.0 0.0.0.255 192.168.200.0 0.0.0.255       
R10(config)#crypto ipsec transform-set test-set ah-sha-hmac esp-aes
R10(config)#crypto map test-map 1 ipsec-isakmp
% NOTE: This new crypto map will remain disabled until a peer
        and a valid access list have been configured.
R10(config-crypto-map)#set peer 100.0.0.1
R10(config-crypto-map)#set transform-set test-set
R10(config-crypto-map)#match address 101
R10(config-crypto-map)#int gi0/0/0
R10(config-if)#crypto map test-map
R10(config-if)#
*Mar  1 00:51:55.511: %CRYPTO-6-ISAKMP_ON_OFF: ISAKMP is ON
R10(config-if)#access-list 102 deny ip 192.168.201.0 0.0.0.255 192.168.200.0 0.0.0.255    
R10(config)#access-list 102 permit ip any any
R10(config)#ip nat inside source list 102 int f0/0 overload
R10(config)#int gi0/0/0
R10(config-if)#ip nat outside
R10(config-if)#in gi0/0/1
R10(config-if)#ip nat inside 
```

​	After the IPSec configurations of the two routers are configured, the IPSec tunnel between the left and right hosts is established. We can observe the operation process of the IPSec stack in more detail by "Ping" each other in the simulation mode to observe the packet encapsulation and decapsulation **(See in section 3.3 for the discussion of these details).**

-  **The IPv6 tunnel network**

![](.\p3-19.png)

<div align = 'center'><b>Fig.45 IPv6 tunnel network topology</div>

​	In this LAN, we achieved that two IPv6 hosts could Ping each other successfully through several IPv4 routers (IPv4 LAN). **The key to this is to build the tunnel that allow IPv6 packets to be encapsulated into IPv4 packets as they pass through IPv4 routers, which will treat the datagrams as normal IPv4 packets.** When the datagrams arrive at the end of the tunnel, the IPv6 router unpacks the IPv4 datagrams into an IPv6 datagrams **(an IPv6 router can realize this fact by checking the upper-layer protocol number)** and sends the datagrams to the target IPv6 host.

​	In the network shown above, two laptops (JCQ's PC and ZXD's PC) are both **IPv6 hosts**. The middle routers (Router 27, Router 29 and Router 25) have IPv4 interfaces. **Therefore, an IPv6 to IPv4 tunnel needs to be set up between Router 27 and Router 25. **So, corresponding tunnel information needs to be configured on the two routers. **(The tunnel is bidirectional, so the tunnel information needs to be configured on both routers).** The configuration information is shown below:

​	**1. Router 27**

```bash
Router27#conf
Router27(config)#int tunnel 1
Router27(config-if)#ipv6 addr 5001::1/64
Router27(config-if)#tunnel source gi0/0/1
Router27(config-if)#tunnel destination 20.0.0.2
Router27(config-if)#tunnel mode ipv6ip
Router27(config-if)#exit
Router27(config)#ipv6 route 4000::/64 5000::2 #配置ipv6隧道抵达右侧主机的静态路由
Router27(config)#ipv6 route 3000::/64 5000::2 #配置ipv6隧道抵达隧道右侧路由器的静态路由
```
​	**2. Router 25**

```bash
Router25#conf
Router25(config)#int tunnel 1
Router25(config-if)#ipv6 addr 5001::2/64
Router25(config-if)#tunnel source gi0/0/0
Router25(config-if)#tunnel destination 10.0.0.1
Router25(config-if)#tunnel mode ipv6ip
Router25(config-if)#exit
Router25(config)#ipv6 route 2000::/64 5000::1 #配置ipv6隧道抵达左侧主机的静态路由
```

​	Of course, if we now “Ping” the hosts at both ends of the tunnel, we will find that the two hosts cannot “Ping” each other. **This is because the router at the right end of the tunnel is not the default gateway for the laptop on the right (ZXD's PC). **Therefore, **we need to configure the static routes for Router 26 and Router 25 as shown below：**

​	**1. Router 26**

```python
Router26#conf
Router26(config)#ipv6 route 2000::/64 3000::2
```

​	**2. Router 25**

```python
Router25#conf
Router25(config)#ipv6 route 4000::/64 3000::1
```

​	After the two static IPv6 routes are configured, the laptops on both sides of the tunnel can **"Ping"** each other. **For details about the Ping test, see Section 3.3.**

- **Route Configuration of the trunk router**

​	In this part, the configuration of **the static route and dynamic route** of trunk router will be  briefly demonstrated.

​	**1.Router 9**

<img src=".\RIP of router9.png" style="zoom: 80%;" />

<div align = 'center'><b>Fig.46 RIP of router9</div>

**2.Router 14**

<img src=".\RIP of router14.png" style="zoom:80%;" />

<div align = 'center'><b>Fig.47 RIP of router14</div>

**3.Router 13**

<img src=".\RIP of router13.png" style="zoom:80%;" />

<div align = 'center'><b>Fig.48 RIP of router13</div>

**4.Router4**

<center class="half">    
    <img src=".\Static router of router4.png"  alt="image-20221225130536907" style="zoom:120%;" width="250"/>    
    <img src=".\RIP of router4.png" alt="image-20221225130611296" style="zoom:120%;" width="300"/> 
</cente


<div align = 'center'><b>Fig.49 static and RIP of router13</div>

**5.Router0**

<center class="half">    
    <img src=".\RIP of router0.png"  alt="image-20221225130536907" style="zoom:120%;" width="300"/>    
    <img src=".\static router of 0.png" alt="image-20221225130611296" style="zoom:110%;" width="300"/> 
</center>
<div align = 'center'><b>Fig.50 RIP and static of router0</div>

**6.Router5**

<center class="half">    
    <img src=".\RIP of router5 .png"  alt="image-20221225130536907" style="zoom:120%;" width="280"/>    
    <img src=".\static of router5.png" alt="image-20221225130611296" style="zoom:120%;" width="280"/> 
</center>
<div align = 'center'><b>Fig.51 RIP and static of router5</div>

**7.Router29**

<img src=".\RIP of router29.png" style="zoom: 67%;" />

<div align = 'center'><b>Fig.52 RIP of router5</div>

**8.Router3**

<center class="half">    
    <img src=".\RIP of router3.png"  alt="image-20221225130536907" style="zoom:120%;" width="280"/>    
    <img src=".\static router of router3.png" alt="image-20221225130611296" style="zoom:110%;" width="280"/> 
</center>
<div align = 'center'><b>Fig.53 RIP and static of router3</div>


**9.Router7**

<center class="half">    
    <img src=".\RIP of router7.png"  alt="image-20221225130536907" style="zoom:120%;" width="280"/>    
    <img src=".\static of router7.png" alt="image-20221225130611296" style="zoom:110%;" width="280"/> 
</center>
<div align = 'center'><b>Fig.54 RIP and static of router7</div>

**10.Router8**

<center class="half">    
    <img src=".\RIP of router8.png"  alt="image-20221225130536907" style="zoom:120%;" width="280"/>    
    <img src=".\static router of router8.png" alt="image-20221225130611296" style="zoom:110%;" width="280"/> 
</center>
<div align = 'center'><b>Fig.55 RIP and static of router8</div>


### 3.3 Test of performance

​	This section is divided into three parts: test of connectivity, test of isolation and test of  network function.

#### 3.3.1 Test of connectivity

​	After all configurations are complete, test the connectivity between all local area networks.

**1.connectivity between library network and computer room network**

​	The laptop in the library network ping one PC in the computer room network, the result is shown below: 

<img src=".\connectivity betwwen library network and computer room network.png" style="zoom: 50%;" />

<div align = 'center'><b>Fig.56 laptop in library ping PC in computer room</div>

​	The result shows that the library network can connect to the computer room network.

**2.connectivity between library network and information center network**

​		The laptop in the library network ping one server in the information center network, the result is shown below: 

<img src=".\connectivity between library network and information center network.png" style="zoom: 50%;" />

<div align = 'center'><b>Fig.57 laptop in library ping server in information center</div>

​	The result shows that the library network can connect to the information center network.

**3.connectivity between computer room network and JCQ's laptop**

​	The PC in the computer room network ping JCQ's laptop and JCQ's laptop ping The PC in the computer room , the results are shown below: 

<center class="half">    
    <img src=".\The PC in the computer room network ping JCQ's laptop.png"  alt="image-20221225130536907" style="zoom:120%;" width="280"/>    
    <img src=".\JCQ's laptop ping The PC in the computer room .png" alt="image-20221225130611296" style="zoom:110%;" width="280"/> 
</center>
<div align = 'center'><b>Fig.58 ping test between computer room network and JCQ's laptop</div>


​	The results show that the connectivity between computer room network and JCQ's laptop is perfect.

**4.connectivity between computer room network and ZXD's laptop**

​	The PC in the computer room network ping ZXD's laptop and ZXD's laptop ping The PC in the computer room , the results are shown below: 

<center class="half">    
    <img src=".\The PC in the computer room network ping ZXD's laptop.png"  alt="image-20221225130536907" style="zoom:100%;" width="280"/>    
    <img src=".\ZXD's laptop ping The PC in the computer room.png" alt="image-20221225130611296" style="zoom:110%;" width="280"/> 
</center>
<div align = 'center'><b>Fig.59 ping test between computer room network and ZXD's laptop</div>


​	The results show that the connectivity between computer room network and ZXD's laptop is perfect.

**5.connectivity between computer room network and information center network**

​	The PC in the computer room network ping DNS server in information center network and the DNS server in information center network ping the PC in the computer room , the results are shown below:

<center class="half">    
    <img src=".\The PC in the computer room network ping DNS server in information center network  .png"  alt="image-20221225130536907" style="zoom:110%;" width="280"/>    
    <img src=".\the DNS server in information center network ping the PC in the computer room.png" alt="image-20221225130611296" style="zoom:110%;" width="280"/> 
</center>
<div align = 'center'><b>Fig.60 ping test between computer room network and DNS server in information center network</div>


​	The results show that the connectivity between computer room network and  information center network is perfect.

**6.connectivity between JCQ's laptop and ZXD's laptop**

​	JCQ's laptop ping ZXD's laptop and ZXD's laptop ping JCQ's laptop, the results are shown below:

<center class="half">    
    <img src=".\JCQ's laptop ping ZXD's laptop.png"  alt="image-20221225130536907" style="zoom:110%;" width="280"/>    
    <img src=".\ZXD's laptop ping JCQ's laptop.png" alt="image-20221225130611296" style="zoom:110%;" width="280"/> 
</center>
<div align = 'center'><b>Fig.61 ping test between JCQ's laptop and ZXD's laptop</div>


​	The results show that the connectivity between JCQ's laptop and ZXD's laptop is perfect.

**7.connectivity between JCQ's laptop and information center network**

​	JCQ's laptop ping DNS server in information center network and the DNS server in information center network ping JCQ's laptop, the results are shown below:

<center class="half">    
    <img src=".\JCQ's laptop ping DNS server in information center network.png"  alt="image-20221225130536907" style="zoom:100%;" width="280"/>    
    <img src=".\DNS server in information center network ping JCQ's laptop.png" alt="image-20221225130611296" style="zoom:100%;" width="280"/> 
</center>
<div align = 'center'><b>Fig.62 ping test between JCQ's laptop and information center network</div>


​	The results show that the connectivity between JCQ's laptop and information center network is perfect.

**8.connectivity between ZXD's laptop and information center network**

​	ZXD's laptop ping DNS server in information center network and the DNS server in information center network ping ZXD's laptop, the results are shown below:

<center class="half">    
    <img src=".\ZXD's laptop ping DNS server in information center network.png"  alt="image-20221225130536907" style="zoom:110%;" width="280"/>    
    <img src=".\the DNS server in information center network ping ZXD's laptop.png" alt="image-20221225130611296" style="zoom:110%;" width="280"/> 
</center>
<div align = 'center'><b>Fig.63 ping test between ZXD's laptop and information center network</div>


​	The results show that the connectivity between ZXD's laptop and information center network is perfect.

**9.connectivity between IoT and information center network**

​	The PC in the IoT network ping DNS server in the information center network, the result is shown below: 

<img src=".\The PC in the IoT network ping DNS server in the information center network.png" style="zoom: 67%;" />

<div align = 'center'><b>Fig.64 The PC in the IoT network ping DNS server in the information center network</div>

​	The result shows that the IoT network can connect to the information center network.

**10.connectivity between IoT and computer room network**

​	The PC in the IoT network ping one PC in the computer room network, the result is shown below: 

<img src=".\The PC in the IoT network ping one PC in the computer room network.png" style="zoom: 50%;" />

<div align = 'center'><b>Fig.65 The PC in the IoT network ping one PC in the computer room network</div>

​	The result shows that the IoT network can connect to the computer room network.

**11.connectivity between JCQ's PC and ZXD's PC**

​	JCQ's PC ping ZXD's PC and ZXD's PC ping JCQ's PC, the results are shown below:

<center class="half">    
    <img src=".\JCQ's PC ping ZXD's PC.png"  alt="image-20221225130536907" style="zoom:110%;" width="280"/>    
    <img src=".\ZXD's PC ping JCQ's PC.png" alt="image-20221225130611296" style="zoom:110%;" width="280"/> 
</center>
<div align = 'center'><b>Fig.66 ping test between JCQ's PC and ZXD's PC</div>


The results show that the connectivity between JCQ's PC and ZXD's PC is perfect.

#### 3.3.2 Test of isolation

**1.Isolation from external network to wireless local area network**

​	In **3.3.1**, it is obvious that the devices in the two wireless local area network can access the computer room network and the information center network. However, the devices in the computer room network and the information network can't access the two wireless local area network.

 <center class="half">    
    <img src=".\computer room network ping library network.png"  alt="image-20221225130536907" style="zoom:110%;" width="280"/>    
    <img src=".\computer room network ping IoT.png" alt="image-20221225130611296" style="zoom:100%;" width="280"/> 
</center>
<div align = 'center'><b>Fig.67 ping test from computer room network and two wireless local area network</div>


​	The reason behind this is the firewall in the wireless router has worked. When a packet access external network from the internal through the firewall, the firewall generates session status and records the source IP address, destination IP address, the port number, source MAC address, destination MAC address, and so on. When packets are sent back from the external network, the firewall checks the status firstly to check whether the information in the packet returned is consistent with that in the session state. If yes, the packet returned from the external network to the internal network is allowed. If the information is inconsistent with the session state, the firewall checks whether the **ACL** policy allows the packets from the external network to enter. If not, the packets aren't allowed to enter the internal network.

​	Access control lists are referred to as **ACL**. The ACL uses the packet filtering technology to read the information in the Layer 3 and Layer 4 packet headers on the router, such as the source address, destination address, source port, and destination port, and filters the packets according to predefined rules to achieve the purpose of access control.

​	When the devices in wireless local area network ping the devices in the computer room network, the firewall on the wireless router generate session status and record corresponding information. When the packets return from the computer room network to the wireless local area network, the information in the packets is consistent with that in the session state, which means them can enter the wireless local area network. When the devices in computer room network ping the devices in the wireless local area network, the firewall on the wireless router doesn't contain any information about the packets. Besides, the ACL on the wireless router doesn't be configured to let the packets from the external network enter. So the devices in the computer room network and the information network can't access the two wireless local area network.

**2.Isolation between VPN network and wireless local area network**

​	When the devices in VPN network ping the devices in the wireless local area network, the access isn't allowed because of  firewall and ACL. What's more, when the devices in the wireless local area network ping the devices in VPN network, the access isn't also allowed.

 <center class="half">    
    <img src=".\the wireless local area network ping VPN network.png"  alt="image-20221225130536907" style="zoom:110%;" width="280"/>    
    <img src=".\VPN network ping the wireless local area network.png" alt="image-20221225130611296" style="zoom:110%;" width="280"/> 
</center>
<div align = 'center'><b>Fig.68 ping test between wireless local area network and VPN network</div>


​	Router 6 and router 10 are both configured with **NAT** mode and **IPSec** mode. By default, **NAT** mode takes precedence. (The detail of IPSec will be demonstrated in **3.3.3**). When the the devices in the wireless local area network ping JCQ's laptop whose IP address is $192.168.200.2$, the corresponding information of packet whose direction is from wireless area network to VPN network in and out the wireless router is shown below:

<img src=".\from wireless area network to VPN network .png" style="zoom: 50%;" />

  <div align = 'center'><b>Fig.69 corresponding information of packet from wireless area network to VPN network</div>

​	The firewall in the wireless router record the destination IP address which is $192.168.200.2$. When the packet returned  , the corresponding information of returned packet in and out router6 is shown below:

<img src=".\from VPN network to wireless network.png" style="zoom: 50%;" />

<div align = 'center'><b>Fig.70 corresponding information of returned packet from VPN network to wireless local area network</div>

​	Source IP address of returned packet in router6 is $192.168.200.2$ while Source IP address of returned packet in router6 is $100.0.0.1$. This is because of NAT in router6. When the wireless router receives returned packet, the firewall in it check source IP address of returned packet which is $100.0.0.1$, which is inconsistent with the source IP address recorded. So, the firewall blocks returned packet. That is why the access isn't also allowed when the devices in the wireless local area network ping the devices in VPN network.

**3.Isolation between IPv6 network and IPv4 network**

​	When the devices in IPv6 network ping the devices in IPv4 network, the access isn't allowed. And vice versa. 

 <center class="half">    
    <img src=".\computer network ping v6.png"  alt="image-20221225130536907" style="zoom:100%;" width="260"/>    
    <img src=".\v6 ping computer network.png" alt="image-20221225130611296" style="zoom:110%;" width="260"/> 
</center>
<div align = 'center'><b>Fig.71 ping test between IPv4 network and IPv6 network</div>


​	All the end systems in our network topology are single stack hosts, which support only one protocol, IPv4 or IPv6. When a packet of one protocol type is sent to a host that supports another protocol type, the host cannot identify the packet of this protocol type. So a host that supports only IPv6 cannot communicate with a host that supports only IPv4.

#### 3.3.3 test of  network function

**1.HTTP service and DNS service**

​	Firstly, the IP address of DNS server need to be configured on the PC. Then resource  record need to be configured on DNS server.

<center class="half">    
    <img src=".\IP address of DNS server.png"  alt="image-20221225130536907" style="zoom:100%;" width="280"/>    
    <img src=".\resource record.png" alt="image-20221225130611296" style="zoom:110%;" width="280"/> 
</center>
<div align = 'center'><b>Fig.72 configuration of DNS IP and resource record</div>


​	Visit the web Page **www.cisco.com** to test HTTP service and DNS service. The result and trace of packet is shown below:

<img src=".\HTTP server.png" style="zoom: 80%;" />

<div align = 'center'><b>Fig.73 result of ping www.cisco.com</div>

<center class="half">    
    <img src=".\DNS server 1.png"  alt="image-20221225130536907" style="zoom:100%;" width="300"/>    
    <img src=".\DNS server2.png" alt="image-20221225130611296" style="zoom:110%;" width="300"/> 
</center>
<div align = 'center'><b>Fig.74 trace of packet</div>


​	The figures above means HTTP service and DNS service are perfect. PC0 first sends packets to DNS server to ask IP address of **www.cisco.com**. Then DNS server reply a packet to tell PC0 that IP address of **www.cisco.com** is $192.168.137.2$. After knowing the IP address of **www.cisco.com**, PC0 sends HTTP require message to do the first step of three-way handshaking  and HTTP server sends HTTP reply message to do the second step of three-way handshaking.

**2.DHCP service**

​	The configuration of DHCP service on DHCP server is shown below: 

<img src=".\DHCP configuration.png" style="zoom:67%;" />

<div align = 'center'><b>Fig.75 configuration of DHCP service on DHCP server</div>

​	The result of DHCP service is shown below:

<center class="half">    
    <img src=".\DHCP of PC0.png"  alt="image-20221225130536907" style="zoom:110%;" width="300"/>    
    <img src=".\DHCP of PC1.png" alt="image-20221225130611296" style="zoom:100%;" width="300"/> 
</center>
<div align = 'center'><b>Fig.76 DHCP service</div>


**3.FTP service**

​	FTP server is used to transfer files between two computers. It is one of the most widely used services in Internet. It can set the permission of each user according to the actual needs, but also has the characteristics of cross-platform, cross-platform file transmission between each other. The configuration of FTP service on FTP server is shown below:

<img src=".\configuration of FTP service.png" style="zoom: 50%;" />

<div align = 'center'><b>Fig.77 configuration of FTP service on FTP server</div>

​	Then PC0 is used to access FTP server. The result is shown below:

<img src=".\FTP service.png" style="zoom:67%;" />

<div align = 'center'><b>Fig.78  FTP service </div>

**4.Email server**

​	The configuration of Email service on Email server is shown below:

 <center class="half">    
    <img src=".\email of email server.png"  alt="image-20221225130536907" style="zoom:110%;" width="300"/>    
    <img src=".\DNS of email server.png" alt="image-20221225130611296" style="zoom:100%;" width="290"/> 
</center>
<div align = 'center'><b>Fig.79   configuration of Email service on Email server </div>


​	 Now PC0 send email to juanlao3. The result is shown below: 

<center class="half">    
    <img src=".\send email.png"  alt="image-20221225130536907" style="zoom:100%;" width="300"/>    
    <img src=".\receive email.png" alt="image-20221225130611296" style="zoom:100%;" width="300"/> 
</center>
<div align = 'center'><b>Fig.80   send email and receive email </div>


​	When PC0 send a email to juanlao3, user agent of PC0 send the email to email server of PC0 using HTTP. Then DNS server resolve **outmail.sustech.edu.cn** and then the email is pulled to email server of juanlao3 using SMTP. Email server of juanlao3 receive the email and put it into mailbox of juanlao3. The juanlao3 run user agent to read the email using POP3. 

**5.IOT service**

​	In the dormitory network, smartphone logins control accounts to control IoT devices indirectly through servers. The information of control account is shown below:

<img src=".\information of account.png" style="zoom:67%;" />

<div align = 'center'><b>Fig.81   information of account </div>

​	Then smartphone login control account to control IoT devices.

<img src=".\台灯 off.png" style="zoom:67%;" />

<div align = 'center'><b>Fig.82   smartphone control Table lamp to turn off </div>

<img src=".\台灯 on.png" style="zoom:67%;" />

<div align = 'center'><b>Fig.83   smartphone control Table lamp to turn on </div>

**6. VPN service-IPSec**

​	The VPN service in IPSec tunnel mode can effectively protect the communication between hosts in the VPN Internet. To the outside world, it's just two gateway servers communicating with each other to hide the information of the hosts on the VPN Internet. The following process will prove the point. Let JCQ's laptop ping ZXD's laptop. 

​	Source IP address and destination IP address of the packet in router6 are $192.168.200.2$ and $192.168.201.2$ while that of the packet out router6 are $100.0.0.1$ and $1.1.1.2$. When the packet go through router6, the original packet whose source IP address and destination IP address are $192.168.200.2$ and $192.168.201.2$ is encapsulated into a new packet whose source IP address and destination IP address are  $100.0.0.1$ and $1.1.1.2$. Besides, the new packet adds AH and ESP headers.  

<img src=".\packet in and out router6.png" style="zoom: 50%;" />

<div align = 'center'><b>Fig.84   corresponding information of packets in and out router6 </div>

<center class="half">    
    <img src=".\message format in router6.png"  alt="image-20221225130536907" style="zoom:100%;" width="300"/>    
    <img src=".\message format out router6.png" alt="image-20221225130611296" style="zoom:100%;" width="300"/> 
</center>
<div align = 'center'><b>Fig.85   message format of packets in and out router6   </div>


​	Then the new packet transmit from router6 to router10. At the router10, the new packet whose source IP address and destination IP address are $100.0.0.1$ and $1.1.1.2$ is unpacked and the original packet whose source IP address and destination IP address are $192.168.200.2$ and $192.168.201.2$ is extracted from the new packet. Then, the original packet is transmitted to PC4.

<img src=".\packet in and out router10.png" style="zoom:67%;" />

<div align = 'center'><b>Fig.86   corresponding information of packets in and out router10 </div>

<center class="half">    
    <img src=".\message format in router10.png"  alt="image-20221225130536907" style="zoom:100%;" width="300"/>    
    <img src=".\message format out router10.png" alt="image-20221225130611296" style="zoom:100%;" width="300"/> 
</center>
<div align = 'center'><b>Fig.87   message format of packets in and out router10   </div>

**7. IPv6 tunnel service**

​	In this subsection, I show that the IPv6 hosts **(JCQ's PC and ZXD's PC)** at both ends of an IPv6 tunnel can **"Ping"** through each other.

<center class="half">    
    <img src=".\JCQ's PC ping ZXD's PC.png"  alt="image-20221225130536907" style="zoom:110%;" width="280"/>    
    <img src=".\ZXD's PC ping JCQ's PC.png" alt="image-20221225130611296" style="zoom:110%;" width="280"/> 
</center

<div align = 'center'><b>Fig.88 IPv6 tunnel service</div>

​	The more detail about IPv6 tunnel and the related static and dynamic routing configuration can can be seen in **Section 3.2**.

​	It is also interesting to note that the IPv6 hosts at either end of the tunnel cannot access the IPv4 subnets on the campus network but these hosts at both ends of the tunnel can "Ping" each other through a series of IPv4 LAN routers because the two computers are IPv6 single-stack hosts. However, the default gateway Router of the left host **(JCQ's PC) **has an IPv4 interface, so it can access the IPv4 subnet outside the campus network, as shown below **(Taking Router 27 "Ping" the Web server 192.168.137.2 as an example) :**

<img src=".\IPv6 tunnel.png" style="zoom:67%;" />

<div align = 'center'><b>Fig.89 The connectivity test of IPv4 router in the middle of IPv6 tunnel </div>
## Part 4: Conclusion

​	In this course project, we looked at everything about IPv6 networks. This section describes the background, core technologies, application scenarios, and advanced technologies of IPv6. In the part 3, we simulate the addressing and interworking of IPv4 and IPv6 networks by building a campus network. In this section we also implemented many common services such as Web service, DNS service, FTP service, and Email service and verified them well through practical tests. In addition, we have implemented some extended-play components such as IOT services, IPv6 tunneling and IPSec virtual private network services. In building these extended services, we had a lot of problems at first. But after consulting the relevant information and intense discussion and analysis, we can finally use the relevant knowledge of computer network to solve them well.

​	Our biggest impression in this project is that when we encounter problems in the network topology simulation in the part 3, we can try to carry out packet capture analysis in the simulation mode. For example, **Why can't the hosts in the wireless LAN "Ping" through the hosts on both sides of the IPSec tunnel? This is a nice problem we meet**. Through packet capture analysis, we can clearly see that the reason is that **the firewall in the wireless router does not record the session state after the IP address modification due to NAT of the IPSec gateway router. As a result, the firewall of the wireless router thinks that the packet is a datagram sent from the Internet instead of the packet returned to the hosts in this wireless LAN, and then discards it.**

​	All in all, this course project provided us with a good opportunity to expand our learning outside the classroom and let us have a deeper understanding of IPv6 technology and its relationship with IPv4.
