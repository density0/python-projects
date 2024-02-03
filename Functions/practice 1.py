def old_macdonald(name):
    if len(name) > 3:
        return name[:3] + name[3:].capitalize()
    else:
        return 'Name is too short!'


print(old_macdonald('bruhfff'))

def master_yoda(sentence):
    return ' '.join(sentence.split()[::-1])

print(master_yoda("how are you"))