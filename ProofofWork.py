import hashlib
from datetime import datetime 
from Transaction import Transaction
import json


class ProofOfWork:
    """
    工作量證明, 專用黎幫block做mining
    """
    def __init__(self, block, miner, difficult=5):
        self.block = block
        self.miner = miner # Wallet object
        # 定義工作量難度，default = 5 表示hash starts with 5 zeros.
        self.difficulty = difficult
        self.reward_amount = 1
        
    def mine(self):
        """
        挖礦function
        """
        i = 0
        prefix = "0" * self.difficulty

        while True:
            message = hashlib.sha256()
            message.update(str(self.block.prev_hash).encode('utf-8'))
            message.update(str(self.block.transactions).encode('utf-8'))
            message.update(str(self.block.timestamp).encode('utf-8'))
            message.update(str(i).encode('utf-8'))
            digest = message.hexdigest()
            if digest.startswith(prefix):
                self.block.nonce = i
                self.block.hash = digest
                break
                # return self.block
            i += 1
        # Offer reward for successful mining.
        t = Transaction(
                sender = "",
                recipient=self.miner.address,
                amount=self.reward_amount
            )
        sig = self.miner.sign(t.toJSON())
        t.set_sign(sig, self.miner.pubkey)
        self.block.transactions.append(t)
        return self.block

    def validate(self):
        """
        validate nonce value satisfies PoW criterion 
        """
        message = hashlib.sha256()
        message.update(str(self.block.prev_hash).encode('utf-8'))
        message.update(str(self.block.data).encode('utf-8'))
        message.update(str(self.block.timestamp).encode('utf-8'))
        message.update(str(self.block.nonce).encode('utf-8'))
        digest = message.hexdigest()

        prefix = "0" * self.difficulty
        return digest.startswith(prefix)