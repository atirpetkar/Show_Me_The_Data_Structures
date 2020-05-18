import hashlib
import time

class Block:

    def __init__(self, timestamp, data, previous_hash=None):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash(self.data)
        self.next = None

    def calc_hash(self,string):
        sha = hashlib.sha256()
        hash_str = string.encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest() 
        

class BlockChain:

    def __init__(self):
        self.head = None

    def add_block(self, timestamp, data):
        if self.head == None:
            self.head = Block(timestamp, data)
            return
        block = self.head
        while block.next:
            block = block.next
        block.next = Block(timestamp, data, previous_hash=block.hash)

    def get_block(self, data):
        if self.head == None:
            return False
        block = self.head
        while block:
            if block.data == data:
                return (block.data, block.timestamp, block.hash)
            else:
                return False
            block = block.next

    def __repr__(self):
        block = self.head
        output = []
        while block:
            output.append((block.data, block.timestamp))
            block = block.next
        output = map(str, output)
        return ' '.join(output)
        
blockchain = BlockChain()
timestamp1 = time.time()
blockchain.add_block(timestamp1, "block # 1")
print(blockchain)  
print(blockchain.get_block('block # 1'))

timestamp2 = time.time()
blockchain.add_block(timestamp2, "block # 2")
print(blockchain)  

# non existent block
print(blockchain.get_block('block # 3'))
