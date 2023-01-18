from password_generator import PasswordGenerator

pwo = PasswordGenerator()
pwo.minlen = 10
pwo.maxlen = 20
print(pwo.generate())
