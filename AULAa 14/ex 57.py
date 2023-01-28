sexo = input('Informe seu sexo: [M/F]').strip().upper()[0]
while sexo not in 'mMfF':
    sexo = input('dados invalidos.por favor, informe seu sexo ')
print ('sexo {} registrado com sucesso'.format(sexo))