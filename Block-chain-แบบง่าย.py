import hashlib, json

last_block_hash = None

block_genesis = {
 'prev_hash' : None,
 'transactions' : {'tx1' : 'send 10', 'tx2' : 'send 100'}
}

block_2 = {
 'prev_hash' : None,
 'transactions' : {'tx1' : 'send 20', 'tx2' : 'send 200'}
}

block_3 = {
 'prev_hash' : None,
 'transactions' : {'tx1' : 'send 30', 'tx2' : 'send 300'}
}

block_4 = {
 'prev_hash' : None,
 'transactions' : {'tx1' : ''}
}

# block_4 ['transactions']['tx1'] = input("Donate: ")

i = 0

def hashing_block(block, prev_hash):
    if prev_hash is None:   # ถ้าเป็น Genesis Block
        block_ordered = json.dumps(block, sort_keys=True).encode('utf-8') 
        block_hash = hashlib.sha256(block_ordered).hexdigest() # hash block ตัวเอง
    else:
        block['prev_hash'] = prev_hash #เก็บค่า hash ก่อนหน้า
        block_ordered = json.dumps(block, sort_keys=True).encode('utf-8')
        block_hash = hashlib.sha256(block_ordered).hexdigest() # hash block ตัวเอง
    
    return block_hash

def hash_blocks(blocks):
 prev_hash = None
 for block in blocks:
  block['prev_hash'] = prev_hash
  block_serialized = json.dumps(block, sort_keys=True).encode('utf-8')
  block_hash = hashlib.sha256(block_serialized).hexdigest()
  prev_hash = block_hash
 return prev_hash

a = []
a.append([block_genesis,block_2,block_3,block_4])


print("\nGenesis Block's hash")
last_block_hash = hashing_block(block_genesis, last_block_hash)
print(last_block_hash)


print("\nBlock2's hash")
last_block_hash = hashing_block(block_2, last_block_hash)
print(last_block_hash)

print("\nBlock3's hash")
last_block_hash = hashing_block(block_3, last_block_hash)
print(last_block_hash)

print("\nBlock4's hash")
last_block_hash = hashing_block(block_4, last_block_hash)
print(last_block_hash,"\n\n")

print("Original hash")
print(hash_blocks([block_genesis, block_2, block_3, block_4])+"\n")

n = int(input("Number of block to chang: "))
print("tx1: "+a[0][n] ['transactions']['tx1'])
a[0][n] ['transactions']['tx1'] = input("Donate: ")
print("After being tampered")
print(hash_blocks([block_genesis, block_2, block_3, block_4]))

print("tx1: "+a[0][n] ['transactions']['tx1'])

#print("block_4 tx1: "+block_4 ['transactions']['tx1'])

