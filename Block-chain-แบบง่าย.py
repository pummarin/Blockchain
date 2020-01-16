import hashlib
import json

hashs = []

last_block_hash = None
# สร้างบล็อค
block_genesis = {
    'prev_hash': None,
    'transactions': {'tx1': '10'}
}

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


# ทำการแสดงค่าhashของแต่ละบล็อค
TotalDonate = 0
a = 0
blocks = []
for block in block_genesis, block_2, block_3, block_4, block_5, block_6, block_7, block_8, block_9, block_10:
    blocks.append(block)
    if a == 0:
        print("Genesis Block's hash")
    else:
        print("block", a + 1, "'s hash")
    TotalDonate += int(blocks[a]['transactions']['tx1'])
    last_block_hash = hashing_block(blocks[a], last_block_hash)
    print("prev hash:", blocks[a]['prev_hash'])
    print("Tx1: " + blocks[a]['transactions']['tx1'])
    print("Total Donate:", TotalDonate)
    hashs.append(last_block_hash)
    print(last_block_hash + "\n")
    a += 1

print("Original hash All Block")
old = hash_blocks([block_genesis, block_2, block_3, block_4,
                   block_5, block_6, block_7, block_8, block_9, block_10])
print(old)
print("Total Donate: ", TotalDonate, "\n")

# เลือกบล็อคที่ต้องการเปลี่ยนและเปลี่ยนแปลงค่า
n = int(input("Input number for test chang data[0-9]: "))
blocks[n]['transactions']['tx1'] = input("Input data: ")

# hash บล็อคที่เปลี่ยนค่า
tmp = hashing_block(blocks[n], last_block_hash)
# newSumTotalDonate&&check block

if hashs[n] != tmp:
    if n == 0:
        print("\ngenesis block is change")
    else:
        print("\nblock", n + 1, "is change")
newTotalDonate = 0
temp = []
for i in range(len(blocks)):
    newTotalDonate += int(blocks[i]['transactions']['tx1'])
    temp.append(newTotalDonate)
print("Tx1: ", blocks[n]['transactions']['tx1'])
print("Total Donaate: ", temp[n])

# print(hashs[0] == hashs1[0]+"\n")
print("\nOriginal hash All Block")
print(old)
print("Total Donate: ", TotalDonate)
print("\nAfter being modify")
print(hash_blocks([block_genesis, block_2, block_3, block_4,
                   block_5, block_6, block_7, block_8, block_9, block_10]))
print("New Total Donate: ", newTotalDonate)
