from bson import ObjectId
from pymongo import MongoClient

# Thay thế các giá trị này bằng thông tin kết nối thực tế từ MongoDB Cloud của bạn
username = 'admin_gamebansung'
password = 'admin134'
cluster_url = 'cluster0.ba6xpv6.mongodb.net'
database_name = 'FPS_Game'

# Tạo URL kết nối MongoDB
uri = f'mongodb+srv://{username}:{password}@{cluster_url}/{database_name}?retryWrites=true&w=majority'

# Kết nối tới MongoDB
client = MongoClient(uri)

# Chọn cơ sở dữ liệu
db = client[database_name]

# Lấy một collection từ cơ sở dữ liệu
collection = db['server']

def getIpServer():    
    ipServer = collection.find_one({'_id': ObjectId('67d050474fb03c8bcd630f6b')})
    print('ipServer', ipServer)
    print(ipServer['ip'])
    return ipServer['ip']

def setIpServer(ipServer):
    collection.update_one({'_id': ObjectId('67d050474fb03c8bcd630f6b')}, {'$set': {'ip': str(ipServer)}})



# setIpServer('192.168.0.1')
# getIpServer()