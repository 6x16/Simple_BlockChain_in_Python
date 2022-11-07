import hashlib
from datetime import datetime

class Block:
    """
    結構：
        prev_hash: 父區塊hash
        transactions: 交易列表
        timestamp: 區塊創建時間戳
        hash: 當前區塊hash
        Nonce: 隨機數
    """
    def __init__(self, transactions, prev_hash):
        # 將傳入的父區塊hash值和數據保存到class variable中
        self.prev_hash = prev_hash
        self.transactions = transactions
        # 獲取當前時間
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.hash = None
        self.Nonce = None
        
        # (基本型之用) 計算區塊的hash value
        # message = hashlib.sha256()
        # message.update(str(self.prev_hash).encode('utf-8'))
        # message.update(str(self.data).encode('utf-8'))
        # message.update(str(self.timestamp).encode('utf-8'))
        # self.hash = message.hexdigest()
