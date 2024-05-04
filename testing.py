from helpers.ipLibrary import get_ipv4_address
from networks.database import getIpServer


def test_ip_address_from_mongo():
    getIpServer()

def test_ip_local():
    print(get_ipv4_address())
   
print('Testing')
print('1. ip from mongo database')
print('2. ip in local')
choice = int(input('what do you want to check ? : '))

if choice == 1:
    test_ip_address_from_mongo()
    exit(0)
if choice == 2:
    test_ip_local()
    exit(0)

exit(0)