email_id  = { 'Soumya': 'soumya.awesome@gmail.com',
              'Meghan': 'sunshine_meghan@yahoo.com',
              'Harry':  'harry_7898@gmail.com',
              'Kate':   'kate.middleton@gmail.com'}

for name, address in email_id.items():
    print(name, address)

del email_id['Harry']
print(email_id)

if 'Kate' in email_id.keys():
    print(email_id['Kate'])

email_id['William'] = 'thisisadded123@yahoo.com'
sorted(email_id.values())
print(email_id)

# Slicing.....
item_list = ['apple', 'mango', 'kiwi', 'pineapple', 'banana', 'water melon']
name = 'YolandaYogerson'
print(item_list[2::2])
print(name[2:6:2])



