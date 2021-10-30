import hashlib
import itertools


secret_key = 'ckczppom'
for i in itertools.count(0, 1):
    hash_ = hashlib.md5(f'{secret_key}{i}'.encode())
    if hash_.hexdigest().startswith('000000'):
        print(i)
        break
