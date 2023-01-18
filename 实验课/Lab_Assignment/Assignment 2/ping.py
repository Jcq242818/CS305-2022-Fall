import sys

from models import *
from time import *
from sockets import *
import argparse

PING_INTERVAL = 0.05
PING_TIMEOUT = 3


def ping(address,n=4, payload=None,id=None):
	if is_hostname(address):
		address = resolve(address)[0]

	sock = ICMPSocket()
	id = id or unique_identifier()
	payload = payload or random_byte_message(56)
	reply = None
	# count the packet that have been sent
	packets_sent = 0
	# save the rtt time in each packet
	rtts = []
	start_time = []
	receive_time = []
	###############################
	# TODO:
	# Create ICMPRequest and send through socket,
	# then receive and parse reply
	#
	# :type n: int
	# :param n: The number of ICMP request
	#
	# :type payload: bytes
	# :param payload: The payload in ICMP Request
	#
	# :type id: int
	# :param id: The identifier of ICMP Request
	#
	# :rtype: Host
	# :returns: ping result
	#
	# Hint: use ICMPSocket.send() to send packet and use ICMPSocket.receive() to receive
	################################
	# send and receive ICMP packet in one loop
	for i in range(0, n, 1):
		Icmp_Request = ICMPRequest(address,id,sequence=(i+1),payload=payload)
		sock.send(Icmp_Request)
		start_time.append(time())
		packets_sent = packets_sent + 1
		try:
			reply = sock.receive()
			receive_time.append(reply.time)
			rtts.append((receive_time[i] - start_time[i])*1000)
		except Exception:
			pass
	if reply: # If receive the icmp packet
		return Host(
			address=reply.source,
			packets_sent=packets_sent,
			rtts=rtts)
	else:
		pass
	return None


if __name__ == "__main__":
	target = sys.argv[1]
	parser = argparse.ArgumentParser(description="ping")
	# generate the packet number to send, the default value is 4
	parser.add_argument('--n', type=int, default=4)
	# generate the payload of the ICMP packet
	parser.add_argument('--p', type=str, default=None)
	# generate the id of the ICMP packet
	parser.add_argument('--i', type=int, default=None)
	args = parser.parse_args(sys.argv[2:])
	n = args.n
	i = args.i
	p = None
	if args.p:
		p = args.p.encode()
	host = ping(target, n, p, i)
	print(host.__str__())
