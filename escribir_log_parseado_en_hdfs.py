# coding: utf-8
"""
Copiar el log parseado en la sandbox
"""
import hdfs
from hdfs import InsecureClient

# apertura de sesion con WebHDFS
client = InsecureClient(
    'http://sandbox.hortonworks.com:50070', user='root', timeout=1000)

# estos datos podrían pasarse como parámetros del programa
sourceFile = "datos/salida-log_2.txt"
destFile = "log_parser_apache"
sandboxPath = "/datos/logApache/"
dpath = sandboxPath + destFile
limite = 1000

content = client.content(sandboxPath)
print content
# apertura del fichero y preparación del parser con los parámetros que hayamos puestp
fo = open(sourceFile, 'r')

client.write(dpath, data=fo.read())
fo.close()
