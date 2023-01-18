from struct import pack, unpack
import platform as plt
from models import ICMPReply, ICMPRequest
from utils import *
from time import time
from exceptions import *


class ICMPSocket:

    __slots__ = '_sock', '_address', '_privileged'

    _IP_VERSION = 4
    _ICMP_HEADER_OFFSET = 20
    _ICMP_HEADER_REAL_OFFSET = 20

    _ICMP_CODE_OFFSET = _ICMP_HEADER_OFFSET + 1
    _ICMP_CHECKSUM_OFFSET = _ICMP_HEADER_OFFSET + 2
    _ICMP_ID_OFFSET = _ICMP_HEADER_OFFSET + 4
    _ICMP_SEQUENCE_OFFSET = _ICMP_HEADER_OFFSET + 6
    _ICMP_PAYLOAD_OFFSET = _ICMP_HEADER_OFFSET + 8

    _ICMP_ECHO_REQUEST = 8
    _ICMP_ECHO_REPLY = 0

    def __init__(self, address=None, privileged=True):
        self._sock = None
        self._address = address

        # The Linux kernel allows unprivileged users to use datagram
        # sockets (SOCK_DGRAM) to send ICMP requests. This feature is
        # now supported by the majority of Unix systems.
        # Windows is not compatible.
        self._privileged = privileged or PLATFORM_WINDOWS

        try:
            sys_platform = plt.system().lower()
            if "windows" in sys_platform or "linux" in sys_platform:
                self._sock = self._create_socket(
                    socket.SOCK_RAW)
            else:
                self._sock = self._create_socket(
                    socket.SOCK_DGRAM)

            if address:
                self._sock.bind((address, 0))
        except OSError as err:
            if err.errno in (1, 13, 10013):
                try:
                    self._sock = self._create_socket(
                        socket.SOCK_DGRAM)
                except OSError:
                    raise SocketPermissionError(privileged)
            if err.errno in (-9, 49, 99, 10049, 11001):
                raise SocketAddressError(address)
            raise ICMPSocketError(str(err))

    def _create_socket(self, type):
        '''
        Create and return a new socket.

        '''
        return socket.socket(
            family=socket.AF_INET,
            type=type,
            proto=socket.IPPROTO_ICMP)

    def _set_ttl(self, ttl):
        '''
        Set the time to live of every IP packet originating from this
        socket.

        '''
        self._sock.setsockopt(
            socket.IPPROTO_IP,
            socket.IP_TTL,
            ttl)

    def _checksum(self, data):
        sum = 0

        # TODO:
        # Compute the checksum of an ICMP packet. Checksums are used to
        # verify the integrity of packets.
        #
        # :type data: bytes
        # :param data: The data you are going to send, calculate checksum
        # according to this.
        #
        # :rtype: int
        # :returns: checksum calculated from data
        #
        # Hint: if the length of data is even, add a b'\x00' to the end of data
        # according to RFC
        # let the checksum field in data is "\x00\x00"
        # Please notice that 'str' or 'bytes' object does not support item assignment, so we should do some switch
        data_zero_checksum = data
        length = len(data_zero_checksum)
        # print(length)
        is_even = length % 2
        if is_even == 0 : # The length of data is even
            for i in range(0, length, 1):
                sum += int.from_bytes(data_zero_checksum[i*2 : i*2+2], byteorder='big', signed=False)
        else : # The length of data is odd
            data_zero_checksum = data_zero_checksum + b'\x00'
            for i in range(0, length + 1 ,1):
                sum += int.from_bytes(data_zero_checksum[i*2 : i*2+2], byteorder='big', signed=False)

        while sum >> 16 != 0:
            sum = (sum >> 16) + (sum & 0xffff)

        sum = ~sum & 0xffff
        # print(hex(sum))
        return sum



    def _check_data(self, data, checksum):
        # TODO:
        # Verify the given data with checksum of an ICMP packet. Checksums are used to
        # verify the integrity of packets.
        #
        # :type data: bytes
        # :param data: The data you received, verify its correctness with checksum
        #
        # :type checksum: int
        # :param checksum: The checksum you received, use it to verify data.
        #
        # :rtype: boolean
        # :returns: whether the data matches the checksum
        #
        # Hint: if the length of data is even, add a b'\x00' to the end of data
        # according to RFC
        checksum_get = self._checksum(data)
        # print(checksum_get)
        if checksum_get == checksum:
            return True
        else:
            return False

    def _create_packet(self, request: ICMPRequest):
        id = request.id
        sequence = request.sequence
        payload = request.payload
        checksum = 0
        packet_header : bytes = b''
        packet: bytes = b''
        packet_header = pack('>bbHHH', self._ICMP_ECHO_REQUEST, 0, checksum, id, sequence)
        packet = packet_header + payload
        checksum = self._checksum(packet)
        packet_header = pack('>bbHHH', self._ICMP_ECHO_REQUEST, 0, checksum, id, sequence)
        packet = packet_header + payload

        # 我写的手撸报文代码，出了点问题所以只能用struct.pack来逐个字段地组装报文
        # print(id)
        # print(sequence)
        # print(len(id))
        # print(len(sequence))
        # type = '\x08'
        # code = '\x00'
        # if len(id) != 6 and len(sequence) == 6:
        #     id = id.lstrip('0x').zfill(4)
        #     id = chr(int('0x%s'%id[0:2],16)) + chr(int('0x%s'%id[2:4],16))
        #     sequence =  chr(int('0x%s'%sequence[2:4],16)) + chr(int('0x%s'%sequence[4:6],16))
        # elif len(sequence) != 6 and len(id) == 6:
        #     sequence = sequence.lstrip('0x').zfill(4)
        #     sequence = chr(int('0x%s'%sequence[0:2],16)) + chr(int('0x%s'%sequence[2:4],16))
        #     id =  chr(int('0x%s'%id[2:4],16)) + chr(int('0x%s'%id[4:6],16))
        # elif len(sequence) != 6 and len(id) != 6:
        #     id = id.lstrip('0x').zfill(4)
        #     sequence = sequence.lstrip('0x').zfill(4)
        #     id = chr(int('0x%s'%id[0:2],16)) + chr(int('0x%s'%id[2:4],16))
        #     sequence = chr(int('0x%s'%sequence[0:2],16)) + chr(int('0x%s'%sequence[2:4],16))
        # else : # The length of id and sequence are both 6.
        #     id =  chr(int('0x%s'%id[2:4],16)) + chr(int('0x%s'%id[4:6],16))
        #     sequence =  chr(int('0x%s'%sequence[2:4],16)) + chr(int('0x%s'%sequence[4:6],16))
        # print(id)
        # print(sequence)
        # print(payload)
        # fill the checksum field and it will be processed by the function _checksum
        # checksum_calculated = '\x00\x00'
        # checksum = self._checksum((str(type) + str(code) + str(checksum_calculated) + str(id) + str(sequence) + str(payload)).encode())
        # checksum = str(hex(checksum))
        # if len(checksum) != 6:
        #     checksum = checksum.lstrip('0x').zfill(4)
        #     checksum_packet = chr(int('0x%s'%checksum[0:2],16)) + chr(int('0x%s'%checksum[2:4],16))
        # else:
        #     checksum_packet = chr(int('0x%s'%checksum[2:4],16)) + chr(int('0x%s'%checksum[4:6],16))
        # # Next, we should packet the checksum result into a str object
        # print(checksum_packet)
        # data = (str(type) + str(code) + str(checksum_packet)+ str(id) + str(sequence) + str(payload)).encode()
        # TODO:
        # Build an ICMP packet from an ICMPRequest, you can get a sequence number and
        # a payload.
        #
        # This method returns the newly created ICMP header concatenated
        # to the payload passed in parameters.
        #
		# tips: the 'checksum' in ICMP header needs to be calculated and updated
        # :rtype: bytes
        # :returns: an ICMP header+payload in bytes formatdf
        return packet

    def _parse_reply(self, packet, source, current_time):
        sequence = 0
        type = 0
        code = 0
        id = 0
        checksum = 0
        # TODO:
        # Parse an ICMP reply from bytes.
        #
        # Read sequence, type and code from packet
        #
        # :type packet: bytes
        # :param packet: IP packet with ICMP as its payload
        #
        # :rtype: ICMPReply
        # :returns: an ICMPReply parsed from packet
        data = packet[20:] # get the icmp packet from ip packet
        type, code = unpack('>bb', data[0:2])
        # Firstly we need to check the checksum
        # Firstly we parse the icmp data, so we firstly needs to parse the header field
        # 现在卡到的地方就是这个算校验和，因为接收到的包要算校验和必须先把校验和字段清0再算，好像清0有点麻烦
        data_calculated = pack('>bbH', type, code, 0)
        data_calculated = data_calculated + data[4:]
        checksum = unpack('>H', data[2:4])[0]
        judge = self._check_data(data_calculated,checksum)
        if judge == True: # if the check of the checksum is correct, then parse the data
            if type == 0 or type == 8:
                # convert the id and sequence into dec
                id,sequence = unpack('>HH', data[4:8])
                return ICMPReply(
                    source=source,
                    id=id,
                    sequence=sequence,
                    type=type,
                    code=code,
                    time=current_time)
            else: # if the type is not 0 or 8,it means that it is an error message
                id,sequence = unpack('>HH', data[32:36])
                return ICMPReply(
                        source=source,
                        id=id,
                        sequence=sequence,
                        type=type,
                        code=code,
                        time=current_time)
        else: # if the check of the checksum is wrong, then report the error
            print("The checksum is not correct! Terminate the analysis!")
            pass

    def send(self, request):
        '''
        Send an ICMP request message over the network to a remote host.

        This operation is non-blocking. Use the `receive` method to get
        the reply.

        :type request: ICMPRequest
        :param request: The ICMP request you have created. If the socket
            is used in non-privileged mode on a Linux system, the
            identifier defined in the request will be replaced by the
            kernel.

        :raises SocketBroadcastError: If a broadcast address is used and
            the corresponding option is not enabled on the socket
            (ICMPv4 only).
        :raises SocketUnavailableError: If the socket is closed.
        :raises ICMPSocketError: If another error occurs while sending.

        '''
        if not self._sock:
            raise SocketUnavailableError

        try:
            sock_destination = socket.getaddrinfo(
                host=request.destination,
                port=None,
                family=self._sock.family,
                type=self._sock.type)[0][4]

            packet = self._create_packet(
                request)

            self._set_ttl(request.ttl)
            # self._set_traffic_class(request.traffic_class)

            request._time = time()
            self._sock.sendto(packet, sock_destination)

            # On Linux, the ICMP request identifier is replaced by the
            # kernel with a random port number when a datagram socket is
            # used (SOCK_DGRAM). So, we update the request created by
            # the user to take this new identifier into account.
            if not self._privileged and PLATFORM_LINUX:
                request._id = self._sock.getsockname()[1]

        except PermissionError:
            raise SocketBroadcastError

        except OSError as err:
            raise ICMPSocketError(str(err))

    def receive(self, request=None, timeout=2):
        '''
        Receive an ICMP reply message from the socket.

        This method can be called multiple times if you expect several
        responses as with a broadcast address.

        :type request: ICMPRequest, optional
        :param request: The ICMP request to use to match the response.
            By default, all ICMP packets arriving on the socket are
            returned.

        :type timeout: int or float, optional
        :param timeout: The maximum waiting time for receiving the
            response in seconds. Default to 2.

        :rtype: ICMPReply
        :returns: An `ICMPReply` object representing the response of the
            desired destination or an upstream gateway. See the
            `ICMPReply` class for details.

        :raises TimeoutExceeded: If no response is received before the
            timeout specified in parameters.
        :raises SocketUnavailableError: If the socket is closed.
        :raises ICMPSocketError: If another error occurs while receiving.

        '''
        if not self._sock:
            raise SocketUnavailableError

        self._sock.settimeout(timeout)
        time_limit = time() + timeout

        try:
            while True:
                response = self._sock.recvfrom(1024)
                current_time = time()

                packet = response[0]
                source = response[1][0]

                if current_time > time_limit:
                    raise socket.timeout

                reply = self._parse_reply(
                    packet=packet,
                    source=source,
                    current_time=current_time)

                if (reply and not request or
                    reply and request.id == reply.id and
                    request.sequence == reply.sequence):
                    return reply

        except socket.timeout:
            raise TimeoutExceeded(timeout)

        except OSError as err:
            raise ICMPSocketError(str(err))

    def close(self):
        '''
        Close the socket. It cannot be used after this call.

        '''
        if self._sock:
            self._sock.close()
            self._sock = None



