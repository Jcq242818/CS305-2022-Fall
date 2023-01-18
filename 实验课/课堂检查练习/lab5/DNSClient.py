import dns.resolver
import sys

domain = sys.argv[1]
queryType = sys.argv[2]

try:
    q = dns.resolver.resolve(qname=domain, rdtype=queryType, raise_on_no_answer=False)
    print('What\'s the Answer?',q.response)
    print()
    print('Who send the server?',q.nameserver)
    print()
    print('Port Number?', q.port)
    print()
    print('Is from authority name server?','AUTHORITY' in str(q.response))
except dns.resolver.NoAnswer as na:
    print('This request contains no content')

