from datetime import datetime
from xmlrpc.client import ServerProxy
from xmlrpc.client import DateTime
from xmlrpc.server import SimpleXMLRPCServer


# XML-RPCサーバ
server = SimpleXMLRPCServer(('localhost', 8000))
print('start server')

# 関数
def is_alive():
  return 'alive'

def hello():
  return 'hello'

# 関数の登録
server.register_function(is_alive, 'is_alive')
server.register_function(hello, 'hello')
# system.listMethods で参照できるように登録
server.register_introspection_functions()
# XML-RPCサーバーの起動
server.serve_forever()


# XML-RPCクライアント
proxy = ServerProxy('http://localhost:8000/')
 
# 登録されているメソッド名を取得
print(proxy.system.listMethods())
print(proxy.is_alive())
print(proxy.hello())
