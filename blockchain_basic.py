import hashlib
import datetime
import copy


class Node:
  def __init__(self, value):
    self.value = value
    self.next = None
  
  def __repr__(self):
    return self.value



class Block:

  def __init__(self, data, previous_hash):
    self.timestamp = datetime.datetime.now()
    self.data = data
    self.previous_hash = previous_hash
    self.hash = self.calc_hash(str(self.timestamp) + str(data) + str(previous_hash))
    
  def return_hash(self):
    return self.hash
  
  def return_pv_hash(self):
    return self.previous_hash

  def calc_hash(self, string):
    sha = hashlib.sha256()

    hash_str = string.encode('utf-8')

    sha.update(hash_str)
    return sha.hexdigest()
  
  def __repr__(self):
    string = "Timestap = "+str(self.timestamp)+"\nData = "+str(self.data)+"\nPrevious Hash = "+str(self.previous_hash)+"\nHash = "+str(self.hash)
    return string


class BlockChain:
  def __init__(self):
    self.head = None
    self.chain_array = [None for i in range(10)]
  
  def add_block(self, data):
    if self.head is None:
      self.head = Block(data, None)
      return
    new_block = Block(data, self.head.return_hash())
    self.to_array(self.head)
    self.head = new_block
  
  def to_array(self, value):
    i = self.get_index(value.return_hash())
    if self.chain_array[i] is None:
      self.chain_array[i] = Node(value)
      return
    counter = 0 
    cur = self.chain_array[i]
    while cur.next:
      cur = cur.next
      counter += 1
    cur.next = Node(value)
    if counter>=6:
      self.new_chain()
    return
  
  def get_index(self, hash_code):
    prime_no = 1
    index = 0
    hash_code = str(hash_code)
    for val in hash_code:
      index += (prime_no*ord(val))%len(self.chain_array)
      prime_no *= 37
      prime_no%len(self.chain_array)
    return index%len(self.chain_array)

  def new_chain(self):
    print("New chain function being used")
    old_chain = copy.copy(self.chain_array)
    x = len(self.chain_array)
    x *= x
    self.chain_array = [None for i in range(x)]
    for val in old_chain:
      if val is not None:
        cur = val
        while cur:
          self.to_array(cur.value)
          cur = cur.next
    return

  def __repr__(self):
    listo = []
    cur = self.head
    while True:
      listo.append(cur)
      if cur.return_pv_hash() is None:
        break
      index = self.get_index(cur.return_pv_hash())
      temp = self.chain_array[index]
      while temp:
        if temp.value.return_hash() == cur.return_pv_hash():
          cur = temp.value
          break
        temp = temp.next
    return str(listo)

#Test Case 1
block = BlockChain()
for val in range(10):
  block.add_block(val)
print(block)

#Test Case 2
block2 = BlockChain()
for quant in range(1000):
  block2.add_block("The transaction of "+str(quant+1)+" was made")
print(block2)

#Test Case 3
block3 = BlockChain()
block3.add_block("Only one block exist in this block chain")
print(block3)




      

