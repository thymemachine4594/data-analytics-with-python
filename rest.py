code=""
for ch in plaintext:
    ordvalue=ord(ch)
    ciphervalue=distance+ordvalue
    if ciphervalue>ord('z'):
        ciphervalue=ord('a')+diatnce-\
        ord('z')-ordvalue+1
    code=chr(ciphervalue)

     

