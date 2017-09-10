from models.clientes import Cliente
cliente = Cliente('Jose', 'Ramirez', edad='28')
cliente.edad = '27'
print(cliente.edad)
print(cliente.nombres)

