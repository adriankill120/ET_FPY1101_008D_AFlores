import json
def menu(titulo,lista):
    print('=================================')
    print(titulo.upper())
    print('=================================')
    while True:
        i=1
        for item in lista:
            print(i,'.-',item)
            i+=1
        print(i,'.- Salir')
        opc=input('Ingrese Opción: ')
        if opc.isdigit():
            opc_int=int(opc)
            if opc_int>=1 and opc_int<=i:
                return opc_int
            else:
                print('La opción debe estar entre 1 y ',i)
        else:
            print('Debe Ingresar un Número')

def lee_archivo_vacunas():
    with open('Vacunas.json',encoding='utf-8') as archivo:
        lista_dic=json.load(archivo)
    return lista_dic

def lee_archivo_atenciones():
    with open('tipos_atenciones.json',encoding='utf-8') as archivo:
        diccionario=json.load(archivo)
    lista_dic=diccionario.get('Tipos Atenciones')
    return lista_dic

def valida_codigo(codigo):
    lista=codigo.split('M')
    if lista[0]=='' and lista[1].isdigit() and len(lista[1])==3 and len(lista)==2:
        return True
    else:
        return False

def valida_letras(nombre):
    if nombre.isalpha():
        return True
    else:
        return False

def valida_tipo(tipo):
    if tipo in ['P','G','C','A','T','H']:
        return True
    else:
        return False

def valida_edad(edad):
    if edad>0 and edad<40:
        return True
    else:
        return False

def lee_codigo():
    while True:
        cod=input('Ingrese Código de la Mascota: ')
        if valida_codigo(cod):
            return cod
        else:
            print('Código Incorrecto')

def lee_nombre():
    while True:
        nom=input('Ingrese Nombre de la Mascota: ')
        if valida_letras(nom):
            return nom
        else:
            print('Nombre Incorrecto')

def lee_tipo():
    while True:
        tip=input('Ingrese Tipo de la Mascota (P=Perro, G=Gato, C=Conejo, A=Ave, T=Tortuga y H=Humster): ')
        if valida_tipo(tip):
            return tip
        else:
            print('Tipo Incorrecto')

def lee_edad():
    while True:
        edad=input('Ingrese Edad de la Mascota: ')
        if edad.isdigit():
            if valida_edad(int(edad)):
                return int(edad)
            else:
                print('Edad Fuera de Rango')
        else:
            print('La edad debe ser un número')

def busca_mascota(codigo,lista):
    for dic in lista:
        if dic.get('codigo')==codigo:
            return dic
    return None

def imprime_mascota(mascota):
    print('REGISTRO MASCOTA')
    print('______________________________')
    for clave,valor in mascota.items():
        print(clave,valor)

def nombre_tipo(tipo):
    nombre={'P':'Perro', 'G':'Gato','C':'Conejo', 'A':'Ave', 'T':'Tortuga', 'H':'Humster'}
    return nombre.get(tipo)

def escoge_vacunas(animal,vacunas):
    lista=[]
    for dicc in vacunas:
        if dicc.get('Animal')==animal:
               lista.append(dicc.get('Vacuna'))
    return lista
def asigna_vacunas(tipo,vacunas):
    lista=escoge_vacunas(nombre_tipo(tipo),vacunas)
    opc_salir=len(lista)+1
    cantidad=0
    while True:
        opc=menu('lista de vacunas',lista)
        if opc==opc_salir:
            return(cantidad)
        cantidad+=1

def escoge_atenciones(atenciones):
    lista=[]
    for dicc in atenciones:
        lista.append(dicc.get('Atención'))
    return lista

def asigna_atenciones(atenciones):
    lista=escoge_atenciones(atenciones)
    opc_salir=len(lista)+1
    total=0
    while True:
        opc=menu('lista de atenciones',lista)
        if opc==opc_salir:
            return(total)
        for dicc in atenciones:         
            if lista[opc-1]==dicc.get('Atención'):
                total+=int(dicc.get('Precio'))
                break

# Programa Principal
lista_mascotas=[]
lista_vacunas=lee_archivo_vacunas()
lista_atenciones=lee_archivo_atenciones()
while True:
    opc=menu('menu principal',['Ingresar','Desplegar','Informe'])
    if opc==1:
        diccionario={}
        codigo=lee_codigo()
        nombre=lee_nombre()
        tipo=lee_tipo()
        edad=lee_edad()
        cant_vac=asigna_vacunas(tipo,lista_vacunas)
        total_aten=asigna_atenciones(lista_atenciones)
        diccionario['codigo']=codigo
        diccionario['nombre']=nombre
        diccionario['tipo']=tipo
        diccionario['edad']=edad
        diccionario['vacunas']=cant_vac
        diccionario['atenciones']=total_aten
        lista_mascotas.append(diccionario)
        print(lista_mascotas)
    elif opc==2:
        cod=lee_codigo()
        dicc=busca_mascota(cod,lista_mascotas)
        imprime_mascota(dicc)
    elif opc==3:
        lista=lee_archivo_vacunas()
        escoge_vacuna('Perro',lista)
        with open('archivo.json', 'w') as archivo:
            json.dump(lista_mascotas, archivo)
    else:
        break