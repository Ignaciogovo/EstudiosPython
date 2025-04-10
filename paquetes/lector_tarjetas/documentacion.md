```markdown
# 📚 Uso del lector NFC ACR122U con Python

Este documento describe cómo manejar el lector NFC **ACR122U** usando Python con la librería `pyscard`.

---

## ✅ Requisitos previos

1. **Instalar la librería `pyscard`:**

   ```bash
   pip install pyscard
   ```

2. **Tener el driver del ACR122U instalado:**
   - **Windows**: Generalmente se instala automáticamente.
   - **Linux**: Asegúrate de tener instalado `pcscd`:
     ```bash
      sudo apt-get install pcscd pcsc-tools
     sudo systemctl start pcscd
     ```

    - Editar el archivo: /etc/modprobe.d/blacklist.conf añadiendo:
     ```bash
    install nfc /bin/false
    install pn533 /bin/false
     ```    
    - Instalar drivers desde: https://www.acs.com.hk/en/driver/3/acr122u-usb-nfc-reader/
    -Reiniciar sistema
---

## 🧪 Verificar lectores conectados

```python
from smartcard.System import readers

lectores = readers()
print("Lectores disponibles:")
for lector in lectores:
    print("-", lector)
```

---

## 🔄 Leer el UID de una tarjeta MIFARE

```python
from smartcard.System import readers
from smartcard.util import toHexString

# Obtener el lector
lectores = readers()
if not lectores:
    print("No se encontró ningún lector.")
    exit()

lector = lectores[0]
conexion = lector.createConnection()
conexion.connect()

# Comando APDU para obtener el UID
get_uid_apdu = [0xFF, 0xCA, 0x00, 0x00, 0x00]
respuesta, sw1, sw2 = conexion.transmit(get_uid_apdu)

if sw1 == 0x90 and sw2 == 0x00:
    print("UID de la tarjeta:", toHexString(respuesta))
else:
    print(f"Error al leer la tarjeta: SW1={sw1:X}, SW2={sw2:X}")
```

---

## ⚠️ Notas adicionales

- Si estás en **Linux**, puede que necesites permisos para acceder al dispositivo USB. Considera crear una regla UDEV para que funcione sin `sudo`.

- Este ejemplo está enfocado en leer el **UID** de una tarjeta MIFARE. Para operaciones de lectura/escritura en bloques, se necesitan comandos APDU más específicos y autenticar con claves A/B.

---