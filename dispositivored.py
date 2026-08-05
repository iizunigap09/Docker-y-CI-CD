import re

class DispositivoRed:

  def __init__(self, nombre, ip):
    self.nombre = nombre
    self.ip = ip

  def validar_ip(self):
    # Expresión regular para IPv4 (0-255 en cada octeto)
    patron_ipv4 = r"^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"

    # Expresión regular para IPv6 (admite bloques hexadecimales y compresión ::)
    patron_ipv6 = r"^(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))$"

    if re.match(patron_ipv4, self.ip):
      print(
          f"[OK] La IP '{self.ip}' del dispositivo '{self.nombre}' es una IPV4"
          " válida."
      )
      return True
    elif re.match(patron_ipv6, self.ip):
      print(
          f"[OK] La IP '{self.ip}' del dispositivo '{self.nombre}' es una IPV6"
          " válida."
      )
      return True
    else:
      print(
          f"[ERROR] La IP '{self.ip}' del dispositivo '{self.nombre}' NO es"
          " una IP válida (IPv4/IPv6)."
      )
      return False


# Pruebas con IPv4, IPv6 y una dirección inválida
dev1 = DispositivoRed("Router-Core", "192.168.1.1")
dev2 = DispositivoRed("Switch-IPv6", "2001:0db8:85a3:0000:0000:8a2e:0370:7334")
dev3 = DispositivoRed("Router-Invalido", "999.300.1.1")

dev1.validar_ip()
dev2.validar_ip()
dev3.validar_ip()
