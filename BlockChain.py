class BlockChain:
    """
    區塊鏈結構體
    blocks: 區塊列表
    """
    def __init__(self):
        self.blocks = []

    def add_block(self, block):
        """
        添加新區塊
        """
        self.blocks.append(block)