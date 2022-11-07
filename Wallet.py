from ecdsa import SigningKey, SECP256k1, VerifyingKey, BadSignatureError
from hashlib import sha256
import binascii
import base64

class Wallet:
    """
    錢包：管理賬戶和公私密鑰
    每位用戶有且僅有一個Wallet object作為其區塊鏈中的代表。
    """
    def __init__(self):
        """
        錢包初始化時會based on SECPk1橢圓曲線算法生成一對唯一的密鑰對, 以代表區塊鏈上唯一帳戶
        """
        self._private_key = SigningKey.generate(curve=SECP256k1)
        self._public_key = self._private_key.get_verifying_key()

    @property
    def address(self):
        """
        用公鑰生成地址
        """
        h = sha256(self._public_key.to_pem())
        return base64.b64encode(h.digest())

    @property
    def pubkey(self):
        """
        返回公鑰字符串
        """
        return self._public_key.to_pem()

    def sign(self, message):
        """
        Generate digital signature 
        """
        h = sha256(message.encode('utf-8'))
        return binascii.hexlify(self._private_key.sign(h.digest()))

def verify_sign(pubkey, message, signature):
    """
    驗證簽名
    """
    verifier = VerifyingKey.from_pem(pubkey)
    h = sha256(message.encode('utf-8'))
    return verifier.verify(binascii.unhexlify(signature), h.digest())

def get_balance(blockchain, user):
    """
    遍歷整個區塊鏈，計算該用戶在所有區塊中的支出/收入，從而獲得他的錢包總額。
    """
    balance = 0
    for block in blockchain.blocks:
        for t in block.transactions:
            if t.sender == user.address.decode():
                balance -= t.amount
            elif t.recipient == user.address.decode():
                balance += t.amount
    return balance
