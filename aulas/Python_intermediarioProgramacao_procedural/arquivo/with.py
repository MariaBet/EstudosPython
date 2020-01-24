

with open('abc.txt', 'w+') as file:
    file.write('Linha1\n')
    file.write('Linha2\n')
    file.write('Linha3\n')

    file.seek(0)
    print(file.read())
