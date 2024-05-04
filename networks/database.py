from bson import ObjectId
from pymongo import MongoClient

# Thay thế các giá trị này bằng thông tin kết nối thực tế từ MongoDB Cloud của bạn
username = 'khoa'
password = 'Q0DFLZB2wxsLy9Si'
cluster_url = 'cluster0.rzbbz4l.mongodb.net'
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
    ipServer = collection.find_one({'_id': ObjectId('663336ecee3883f3f45e12e2')})
    print('ipServer', ipServer)
    print(ipServer['ip'])
    return ipServer['ip']

def setIpServer(ipServer):
    collection.update_one({'_id': ObjectId('663336ecee3883f3f45e12e2')}, {'$set': {'ip': str(ipServer)}})



# setIpServer('192.168.0.1')
# getIpServer()