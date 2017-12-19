"""
Parsear el log de apache y convertirlo en una tabla de Hive
"""

import apache_log_parser

sourceFile = "datos/log-prueba.txt"
destFile = "datos/salida-log_2.txt"

fo = open(sourceFile, 'r')
fd = open(destFile, 'w')
lineParser = apache_log_parser.make_parser(
    "%a %l %t \"%r\" %s %R %U \"%{User-Agent}i\"")

for linea in fo:
    jp = lineParser(linea)
    p = (
        jp['remote_ip'] + '|' +
        jp['request_first_line'] + '|' +
        jp['request_header_user_agent'] + '|' +
        jp['request_header_user_agent__browser__family'] + '|' +
        jp['request_method'] + '|' + jp['request_url'] + '|' +
        jp['status'] + '|' + jp['time_received_utc_isoformat'] + '|' +
        jp['url_path'] + '\n')
    fd.write(p)
fo.close()
fd.close()
