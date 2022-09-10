#operadores and y or

usuario_logueado = True
usuario_admin = False
if usuario_logueado and usuario_admin: # si pones or revisa si una de las dos se cumpla
    print('administrador')
elif usuario_logueado:
    print('acceso al sistema')
else:
    print('debes iniciar sesion')