import argparse
import sys

from models import *
from time import sleep
from sockets import *

PING_COUNT = 3  #the number of ICMP echo packet tobe sent whose initial TTL value are same
PING_INTERVAL = 0.05
PING_TIMEOUT = 2
MAX_HOP = 30


def tracert(address, id=None):
    if is_hostname(address):
        address = resolve(address)[0]

    sock = ICMPSocket()

    id = id or unique_identifier()
    ttl = 1
    host_reached = False
    hops = []
    pack_num = 3
    sequence_num = 1
    # start_time = []
    # receive_time = []
    # construct the payload in Windows Operating System
    payload = b'\x00' * 64
    while not host_reached and ttl <= MAX_HOP:
        reply = None
        packets_sent = 0
        rtts = []
        start_time = []
        receive_time = []
        ###############################
        # TODO:
        # Create ICMPRequest and send through socket,
        # then receive and parse reply,
        # remember to modify ttl when creating ICMPRequest
        #
        #
        # :type id: int
        # :param id: The identifier of ICMP Request
        #
        # :rtype: Host[]
        # :returns: ping result
        #
        # Hint: use ICMPSocket.send() to send packet and use ICMPSocket.receive() to receive
        #
        ################################
        # send three packet in one loop to test each hop

        for i in range(0,pack_num,1):
            Icmp_Request = ICMPRequest(address,id,sequence = sequence_num ,payload = payload, payload_size= 64, ttl= ttl)
            sock.send(Icmp_Request)
            start_time.append(time())
            packets_sent = packets_sent + 1
            sequence_num = sequence_num + 1
            try:
                reply = sock.receive()
                receive_time.append(reply.time)
                rtts.append((receive_time[i] - start_time[i])*1000)
            except Exception:
                pass
        if reply:
            hop = Hop(
                    address=reply.source,
                    packets_sent=packets_sent,
                    rtts=rtts,
                    distance=ttl)
            hops.append(hop)
            if reply.source == address:
                host_reached = True
                break
        else:
            pass
        ttl += 1
    return hops


if __name__ == "__main__":
    target = sys.argv[1]
    parser = argparse.ArgumentParser(description="tracert")
    parser.add_argument('--i', type=int, default=None)
    args = parser.parse_args(sys.argv[2:])
    hops = tracert(target,args.i)
    for hop in hops:
        print(hop.__str__())
