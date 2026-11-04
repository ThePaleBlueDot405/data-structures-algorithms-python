heros = ['spider man','thor','hulk','iron man','captain america']

# Length of the list
print(len(heros))

# Add black panther at the end
heros.append('black panther')
print(heros)

# Add black panther after hulk
heros.remove('black panther')
heros.insert(3, 'black panther')
print(heros)

# Replace thor and hulk with doctor strange
heros[1:3] = ['doctor strange']
print(heros)

# Sort the list alphabetically
heros.sort()
print(heros)
