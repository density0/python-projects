alien_0 = {'color': 'green', 'points': 5}
print(alien_0)


# deletes a key-value pair
del alien_0['points']
print(alien_0)

# Using get() to access values

alien_0 = {'color': 'green', 'speed': 'slow'}


# can use get() to set a default value if the requested key doesn't exist
point_value = alien_0.get('points', 'NAH')

print(point_value)



