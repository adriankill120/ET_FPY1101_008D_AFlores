from datetime import datetime,date
# Lee una fecha con formato dd-mm-yyyy, la valida y retorna el valor.
def lee_fecha():
   while True:
      fec=input('Ingrese Fecha (dd-mm-yyyy): ')
      formato = '%d-%m-%Y'
      try:
         fecha = datetime.strptime(fec, formato).date()
         return fecha
      except:
         print('Fecha Incorrecta')
# Recibe una fecha y retorna el string correspondiente con formato dd/mm/yyyy.
def fecha_a_string(fecha):
      fecha_str=fecha.strftime('%d/%m/%Y')
      return fecha_str
# Retorna la cantidad de años entre 2 fechas.      
def agnios(fecha_inicial, fecha_final):
  diferencia = fecha_final - fecha_inicial
  anios = diferencia.days//365
  return anios

# Programa principal para pruebas.      
fec=lee_fecha()
print(fec)
print(fecha_a_string(fec))
f=date.today()
print(agnios(fec,f))
