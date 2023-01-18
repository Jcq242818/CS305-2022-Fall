from time import sleep

import unittest

from scapy.layers.inet import ICMP, IP

from utils import unique_identifier
from models import ICMPRequest
from sockets import ICMPSocket
from ping import ping
from tracert import tracert
from scapy.all import *

host = None
local_target = '10.25.3.230'
iface = "Intel(R) Wireless-AC 9560 160MHz"


class BasicTest(unittest.TestCase):
    socket = None

    @classmethod
    def setUpClass(cls):
        cls.socket = ICMPSocket()

    @classmethod
    def tearDownClass(cls):
        cls.socket.close()

    def testCheckSum_basic(self):
        ans = self.socket._checksum(b'\x08\x00\x00\x00\x04\x00\x00\x01abcd')
        self.assertEqual(12088, ans)

    def testCheckSum_with_random_param(self):
        ans = self.socket._checksum(
            b'\x08\x00\x00\x00\x03\x81\x00\x01kdzqdOFsgHIK60OuuSEwNo7ps7v7P78mRCLjg5dVw3IzPu58PD25ADtL')
        self.assertEqual(37455, ans)

    def testCheckData_true(self):
        ans = self.socket._check_data(
            b'\x08\x00\x00\x00E9\x00\x01zIFGqgWafHAmyLx4q7370PGW4S6633gAKMJWzqW1H9JA5w0E1FiGZdD3', 54909)
        self.assertTrue(ans)

    def testCheckData_false(self):
        ans = self.socket._check_data(
            b'\x08\x00\x00\x00E9\x00\x01zIFGqgWafHAmyLx4q7370PGW4S661H9JA5w0E1asfasfgdsasFiGZdD3', 54909)
        self.assertFalse(ans)

    def testCreatePacket_1(self):
        request = ICMPRequest(
            destination='223.5.5.5',
            id=13009,
            sequence=1,
            payload=b'AAAA'
        )
        ans = self.socket._create_packet(request)
        self.assertEqual(b'\x08\x00B\xab2\xd1\x00\x01AAAA', ans)

    def testCreatePacket_2(self):
        request = ICMPRequest(
            destination=local_target,
            id=1165488,
            sequence=5,
            payload=b'zIFGqgWafHAmyLx4q7370PGW4S661H9JA5w0E1asfasfgdsasFiGZdD3'
        )
        ans = self.socket._create_packet(request)
        self.assertEqual(b'\x08\x00\x8c\xca\xc8\xb0\x00\x05zIFGqgWafHAmyLx4q7370PGW4S661H9JA5w0E1asfasfgdsasFiGZdD3',
                         ans)

    def testParsePacket_normal(self):
        reply = self.socket._parse_reply(
            b'E\x00\x00T.d\x00\x00/\x01\xad\xdd\xb2\x9d:\xbb\xc0\xa8\x01g\x00\x00\xdcKJ\x95\x00\x00GoQOrJrWZA5V82mrPkOtQrjXf07EZeNdYZkwNZ7ReHx7kwzlowcfArbf',
            '223.5.5.5', 1669111491.8911805)
        self.assertEqual(19093, reply.id)
        self.assertEqual(0, reply.sequence)
        self.assertEqual(0, reply.type)
        self.assertEqual(0, reply.code)

    def testParsePacket_error(self):
        reply = self.socket._parse_reply(
            b'E\x00\x00p\x00\x05\x00\x00\x80\x01\x00\x00\xc0\xa8\x01g\xc0\xa8\x01g\x03\x01%\xaa\x00\x00\x00\x00E\x00\x00T\xcd\x8a\x00\x00@\x01\x00\x00\xc0\xa8\x01g\xc0\xa8\x01\xbc\x08\x00T\xd5\x0eU\x00\x001h3fn0ueYjgR06TdC5yGzZwegKtJDWazgVHqsVi4frLZ0jVz2MXENk8t',
            '223.5.5.5', 1669111491.8911805)
        self.assertEqual(3669, reply.id)
        self.assertEqual(0, reply.sequence)
        self.assertEqual(3, reply.type)
        self.assertEqual(1, reply.code)

    def testPing_basic(self):
        self.socket.close()
        host = ping('223.5.5.5', 5)
        self.assertIsNotNone(host)

    # @timeout_decorator.timeout(2)
    def testTracert(self):
        hosts = tracert(local_target)
        self.assertGreater(len(hosts), 0)


class PingTest(unittest.TestCase):
    def testN_1(self):
        host = ping(local_target, 1)
        self.assertEqual(len(host.rtts), 1)

    def testN_2(self):
        host = ping(local_target, 3)
        self.assertEqual(len(host.rtts), 3)

    def testAddress_1(self):
        host = ping('223.5.5.5', 3)
        self.assertEqual(len(host.rtts), 3)

    def testAddress_2(self):
        host = ping('www.baidu.com', 3)
        self.assertEqual(len(host.rtts), 3)


class TracertTest(unittest.TestCase):
    def testAddress_1(self):
        host = tracert('223.5.5.5')
        self.assertGreater(len(host), 3)

    def testAddress_2(self):
        host = tracert('www.baidu.com')
        self.assertGreater(len(host), 3)


class PysharkTest(unittest.TestCase):
    def testPingID(self):
        testID = unique_identifier()

        def lateLunch():
            sleep(1)
            ping(address=local_target, id=testID)

        threading.Thread(target=lateLunch).start()
        pkt = sniff(filter="icmp", timeout=5, iface=iface)
        for p in pkt:
            if p[ICMP].id == testID:
                self.assertTrue(expr=True)
                return
        self.assertFalse(expr=True)

    def testPingSequence(self):
        testID = unique_identifier()

        def lateLunch():
            sleep(1)
            ping(address=local_target, id=testID, n=3)

        sequence = -1
        threading.Thread(target=lateLunch).start()
        pkt = sniff(filter="icmp", timeout=5, iface=iface)
        for p in pkt:
            if p[ICMP].id == testID and p[ICMP].type == 8:
                if sequence == -1:
                    sequence = p[ICMP].seq
                elif sequence != (p[ICMP].seq - 1):
                    self.assertFalse(expr=True)
                sequence = p[ICMP].seq

    def testPingPayload(self):
        testID = unique_identifier()

        def lateLunch():
            sleep(1)
            ping(address=local_target, id=testID, payload=b'test_cs305_lab_assignment_2')

        threading.Thread(target=lateLunch).start()
        pkt = sniff(filter="icmp", timeout=5, iface=iface)
        for p in pkt:
            if p[ICMP].id == testID and p[ICMP].type == 8:
                payload = p[Raw].load
                self.assertEqual(payload, b'test_cs305_lab_assignment_2')

    def testPing(self):
        testID = unique_identifier()
        global host
        host = None

        def lateLunch():
            sleep(1)
            global host
            host = ping(address='223.5.5.5', id=testID, payload=b'test_cs305_lab_assignment_2', n=5)

        threading.Thread(target=lateLunch).start()
        pkt = sniff(filter="icmp", timeout=5, iface=iface)
        packet_received = 0
        for p in pkt:
            if p[ICMP].id == testID and p[ICMP].type == 0:
                packet_received += 1

        self.assertEqual(packet_received, len(host.rtts))

    def testPingRtt(self):
        testID = unique_identifier()
        global host
        host = None

        def lateLunch():
            sleep(1)
            global host
            host = ping(address='us.blizzard.com', id=testID, n=3)

        threading.Thread(target=lateLunch).start()
        pkt = sniff(filter="icmp", timeout=5, iface=iface)
        rtt = 0
        send_time = []
        receive_time = []
        for p in pkt:
            if p[ICMP].id == testID:
                if p[ICMP].type == 8:
                    send_time.append(p.time)
                elif p[ICMP].type == 0:
                    receive_time.append(p.time)

        for i in range(len(send_time)):
            rtt += ((receive_time[i] - send_time[i]) * 1000)
        rtt /= len(send_time)
        diff = abs(host.avg_rtt - rtt)
        self.assertGreater(20, diff)

    def testTracertID(self):
        testID = unique_identifier()

        def lateLunch():
            sleep(1)
            tracert(address=local_target, id=testID)

        threading.Thread(target=lateLunch).start()
        pkt = sniff(filter="icmp", timeout=5, iface=iface)
        for p in pkt:
            if p[ICMP].id == testID:
                self.assertTrue(expr=True)
                return
        self.assertFalse(expr=True)

    def testTracertHopAddress(self):
        testID = unique_identifier()
        global host
        host = None

        def lateLunch():
            sleep(1)
            global host
            host = tracert(address='223.5.5.5', id=testID)

        threading.Thread(target=lateLunch).start()
        pkt = sniff(filter="icmp", timeout=60, iface=iface)
        ips = []
        for p in pkt:
            if (p[ICMP].id == testID and p[ICMP].type != 8) or (
                    p[ICMP].type == 11 and p[ICMP].payload.payload.id == testID):
                ip = p[IP].src
                if ip not in ips:
                    ips.append(ip)
                print(ip)

        if host is not None:
            for h in host:
                if h.address in ips:
                    ips.remove(h.address)

        self.assertEqual(0, len(ips))

    def testTracertAutoStop(self):
        testID = unique_identifier()
        global host
        host = None

        def lateLunch():
            sleep(1)
            global host
            host = tracert(address='223.5.5.5', id=testID)

        threading.Thread(target=lateLunch).start()
        pkt = sniff(filter="icmp", timeout=60, iface=iface)
        ips = []
        for p in pkt:
            if (p[ICMP].id == testID and p[ICMP].type != 8) or (
                    p[ICMP].type == 11 and p[ICMP].payload.payload.id == testID):
                ip = p[IP].src
                if ip not in ips:
                    ips.append(ip)
                print(ip)

        self.assertEqual(len(ips), len(host))


if __name__ == '__main__':
    result = ""
    id = os.path.abspath('.').split("\\")[-1].split('_')
    for i in id:
        if not i.startswith('1'):
            id.remove(i)

    # BasicTest
    suite = unittest.TestSuite()
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(BasicTest))
    test_result = unittest.TextTestRunner(verbosity=1).run(suite)
    basic_count = test_result.testsRun - len(test_result.failures) - len(test_result.errors)
    result += 'BasicTest: {}/{} passed, '.format(basic_count, test_result.testsRun)

    # PingTest
    suite = unittest.TestSuite()
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(PingTest))
    test_result = unittest.TextTestRunner(verbosity=1).run(suite)
    ping_count = test_result.testsRun - len(test_result.failures) - len(test_result.errors)
    result += 'PingTest: {}/{} passed, '.format(ping_count, test_result.testsRun)

    # TracertTest
    suite = unittest.TestSuite()
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TracertTest))
    test_result = unittest.TextTestRunner(verbosity=1).run(suite)
    tracert_count = test_result.testsRun - len(test_result.failures) - len(test_result.errors)
    result += 'TracertTest: {}/{} passed, '.format(tracert_count, test_result.testsRun)

    # PysharkTest
    suite = unittest.TestSuite()
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(PysharkTest))
    test_result = unittest.TextTestRunner(verbosity=1).run(suite)
    pyshark_count = test_result.testsRun - len(test_result.failures) - len(test_result.errors)
    result += 'DetailTest: {}/{} passed, '.format(pyshark_count, test_result.testsRun)

    finalScore = (basic_count + ping_count) * 4 + tracert_count * 2 + pyshark_count * 5
    result += 'FinalScore: {}'.format(finalScore)
    print(result)
    for i in id:
        f = open(file='E:\\CS305\\grade\\{}.txt'.format(i), mode='w+')
        f.write(result)
        f.close()
