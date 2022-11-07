import socket
import threading

# 定義一個global list保存所有結點，每個
NODE_LIST = []

class Node(threading.Thread):
    """
    結點：每個結點都是獨立運行，並共同參與區塊鏈的維護。
    """
    def __init__(self, name, port, host="localhost"):
        threading.Thread.__init__(self, name=name)
        self.host = host  # 服務器地址，本機則設為"localhost"
        self.port = port  # 每個結點對對應一個唯一的端口
        self.name = name  # 唯一的結點名稱
        self.wallet = Wallet()
        self.blockchain = None  # 存儲一個區塊鏈副本

    def run(self):

