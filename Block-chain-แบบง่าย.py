import hashlib
import json

s1 = ''
s2 = ''
s3 = ''
s4 = ''
s5 = ''
s6 = ''
s7 = ''
s8 = ''
s9 = ''
s10 = ''
# x1 = ''; x2 = ''; x3 = ''; x4 = ''; x5 = ''; x6 = ''; x7 = ''; x8 = ''; x9 = ''; x10 = ''

last_block_hash = None

block_genesis = {
    'prev_hash': None,
    'transactions': {'tx1': '10'}
}
s1 += block_genesis['transactions']['tx1']
block_2 = {
    'prev_hash': None,
    'transactions': {'tx1': '20'}
}

block_3 = {
    'prev_hash': None,
    'transactions': {'tx1': '30'}
}

block_4 = {
    'prev_hash': None,
    'transactions': {'tx1': '40'}
}

block_5 = {
    'prev_hash': None,
    'transactions': {'tx1': '50'}
}

block_6 = {
    'prev_hash': None,
    'transactions': {'tx1': '60'}
}

block_7 = {
    'prev_hash': None,
    'transactions': {'tx1': '70'}
}

block_8 = {
    'prev_hash': None,
    'transactions': {'tx1': '80'}
}

block_9 = {
    'prev_hash': None,
    'transactions': {'tx1': '90'}
}

block_10 = {
    'prev_hash': None,
    'transactions': {'tx1': '100'}
}
# block_4 ['transactions']['tx1'] = input("Donate: ")

i = 0


def hashing_block(block, prev_hash):
    if prev_hash is None:   # ถ้าเป็น Genesis Block
        block_ordered = json.dumps(block, sort_keys=True).encode('utf-8')
        block_hash = hashlib.sha256(
            block_ordered).hexdigest()  # hash block ตัวเอง
    else:
        block['prev_hash'] = prev_hash  # เก็บค่า hash ก่อนหน้า
        block_ordered = json.dumps(block, sort_keys=True).encode('utf-8')
        block_hash = hashlib.sha256(
            block_ordered).hexdigest()  # hash block ตัวเอง

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
a.append([block_genesis, block_2, block_3, block_4])

# for i in range(10):
#     x = 0
#     if i == 0:
#         print("Genesis Block's hash")
#         last_block_hash = hash_blocks(a[0][x], last_block_hash)
#         print(last_block_hash)
#     else:
#         print("\nBlock" + i + "'s hash")
#         last_block_hash = hash_blocks(a[0][x], last_block_hash)
#         print(last_block_hash)

print("\nGenesis Block's hash")
last_block_hash = hashing_block(block_genesis, last_block_hash)
# x1 += last_block_hash
print("Total donate: "+block_genesis['transactions']['tx1'])
print(last_block_hash)

print("\nBlock2's hash")
last_block_hash = hashing_block(block_2, last_block_hash)
print("Total donate: "+block_2['transactions']['tx1'])
# x2 += last_block_hash
print(last_block_hash)

print("\nBlock3's hash")
last_block_hash = hashing_block(block_3, last_block_hash)
print("Total donate: "+block_3['transactions']['tx1'])
# x3 += last_block_hash
print(last_block_hash)

print("\nBlock4's hash")
last_block_hash = hashing_block(block_4, last_block_hash)
print("Total donate: "+block_4['transactions']['tx1'])
# x4 += last_block_hash
print(last_block_hash)

print("\nBlock5's hash")
last_block_hash = hashing_block(block_5, last_block_hash)
print("Total donate: "+block_5['transactions']['tx1'])
# x5 += last_block_hash
print(last_block_hash)

print("\nBlock6's hash")
last_block_hash = hashing_block(block_6, last_block_hash)
print("Total donate: "+block_6['transactions']['tx1'])
# x6 += last_block_hash
print(last_block_hash)

print("\nBlock7's hash")
last_block_hash = hashing_block(block_7, last_block_hash)
print("Total donate: "+block_7['transactions']['tx1'])
# x7 += last_block_hash
print(last_block_hash)

print("\nBlock8's hash")
last_block_hash = hashing_block(block_8, last_block_hash)
print("Total donate: "+block_8['transactions']['tx1'])
# x8 += last_block_hash
print(last_block_hash)

print("\nBlock9's hash")
last_block_hash = hashing_block(block_9, last_block_hash)
print("Total donate: "+block_9['transactions']['tx1'])
# x9 += last_block_hash
print(last_block_hash)

print("\nBlock10's hash")
last_block_hash = hashing_block(block_10, last_block_hash)
print("Total donate: "+block_10['transactions']['tx1'])
# x10 += last_block_hash
print(last_block_hash, "\n\n")

print("Original hash")
print(hash_blocks([block_genesis, block_2, block_3, block_4,
                   block_5, block_6, block_7, block_8, block_9, block_10])+"\n")

n = int(input("Number of block to chang[0-9]: "))
print("Old Tx1: " + a[0][n]['transactions']['tx1'])
a[0][n]['transactions']['tx1'] = input("Donate: ")

print("After being tampered")
print(hash_blocks([block_genesis, block_2, block_3, block_4,
                   block_5, block_6, block_7, block_8, block_9, block_10]) + "\n")
print("New Tx1: " + a[0][n]['transactions']['tx1'])

if s1 != a[0][0]['transactions']['tx1']:
    print('Adjust Block is genesis block')
elif s2 != a[0][1]['transactions']['tx1']:
    print('Adjust Block is block2')
elif s3 != a[0][2]['transactions']['tx1']:
    print('Adjust Block is block3')
elif s4 != a[0][3]['transactions']['tx1']:
    print('Adjust Block is block4')
elif s5 != a[0][4]['transactions']['tx1']:
    print('Adjust Block is block5')
elif s6 != a[0][5]['transactions']['tx1']:
    print('Adjust Block is block6')
elif s7 != a[0][6]['transactions']['tx1']:
    print('Adjust Block is block7')
elif s8 != a[0][7]['transactions']['tx1']:
    print('Adjust Block is block8')
elif s9 != a[0][8]['transactions']['tx1']:
    print('Adjust Block is block9')
elif s10 != a[0][9]['transactions']['tx1']:
    print('Adjust Block is block10')
