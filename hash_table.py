hash_table = {}

hash_table['name'] = 'Alice'
hash_table['age'] = 30
hash_table['city'] = 'New York'

print("Name:", hash_table['name'])  
print("Age:", hash_table['age'])    
print("City:", hash_table['city'])  

if 'name' in hash_table:
    print("The key 'name' exists in the hash table.")

del hash_table['age']

print("Updated hash table:", hash_table)