import json

class Transaction:
    """
    交易
    """
    def __init__(self, sender, recipient, amount):
        """
        初始化交易 (包含發送方、接收方和交易數量)
        """
        if isinstance(sender, bytes):
            sender = sender.decode('utf-8')
        self.sender = sender
        if isinstance(recipient, bytes):
            recipient = recipient.decode('utf-8')
        self.recipient = recipient
        self.amount = amount

    def set_sign(self, signature, pubkey):
        """
        發送方需要輸入他的公鑰和簽名，以驗證交易的可靠性
        """
        self.signature = signature
        self.pubkey = pubkey

    def __repr__(self):
        """
        預設列印函數：列印 挖礦所得 及 轉賬交易
        """
        if self.sender:
            s = "從 %s 轉至 %s %f個加密貨幣。" % (self.sender, self.recipient, self.amount)
        else:
            s = "%s 挖礦取得 %f個加密貨幣。" % (self.recipient, self.amount)
        return s
    
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)

