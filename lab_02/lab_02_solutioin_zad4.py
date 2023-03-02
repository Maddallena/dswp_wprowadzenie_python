# Padding and aligning strings
ciag_znakow = "Studenci"
dl = len(ciag_znakow)
print(f'{ciag_znakow:>{dl + 10}}')
print(f'{ciag_znakow:{dl + 10}}')
print(f'{ciag_znakow:*<{dl + 10}}')
print(f'{ciag_znakow:_^{dl + 10}}')
print(f'{ciag_znakow:$^9}')

# Combining truncating and padding
print(f'{ciag_znakow:{10}.5}')

# Numbers
pi = 3.141592653589793238462643
print(f'{pi:10.5}')
print(f'{pi:07.3f}')
print(f'{pi:f}')

# Getitem and Getattr
student = {'imie': 'Magdalena', 'nazwisko': 'Rajewska'}

print(f'{student["imie"]} {student["nazwisko"]}')

