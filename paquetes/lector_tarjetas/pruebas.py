from smartcard.System import readers
from smartcard.util import toHexString
import time
# # Obtener el lector
# lectores = readers()
# if not lectores:
#     print("No se encontró ningún lector.")
#     exit()

# lector = lectores[0]
# conexion = lector.createConnection()
# conexion.connect()

# # Comando APDU para obtener el UID
# get_uid_apdu = [0xFF, 0xCA, 0x00, 0x00, 0x00]
# respuesta, sw1, sw2 = conexion.transmit(get_uid_apdu)

# if sw1 == 0x90 and sw2 == 0x00:
#     print("UID de la tarjeta:", toHexString(respuesta))
# else:
#     print(f"Error al leer la tarjeta: SW1={sw1:X}, SW2={sw2:X}")



r = readers()[0]
conn = r.createConnection()

while True:
    try:
        conn.connect()
        print("🎴 Tarjeta detectada")
        get_uid_apdu = [0xFF, 0xCA, 0x00, 0x00, 0x00]
        respuesta, sw1, sw2 = conn.transmit(get_uid_apdu)
        if sw1 == 0x90 and sw2 == 0x00:
            print("UID de la tarjeta:", toHexString(respuesta))
        else:
            print(f"Error al leer la tarjeta: SW1={sw1:X}, SW2={sw2:X}")
        conn.disconnect()
    except:
        print("🔍 Esperando tarjeta...")
    time.sleep(1)
