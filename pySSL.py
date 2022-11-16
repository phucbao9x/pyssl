from pyssl._makecode import (
    makessl,
    default_value as DV
)
import subprocess
import sys, os

def inputvalue(cast = str):
    while True:
        tmp = input('>>')
        if tmp == "": return 'ENT'
        else:
            try: 
                return cast(tmp)
            except:
                print('It\'s only supported for %s'%cast.__name__)
                exit(0)

def runcmd():
    os.system('title PySSL')
    os.system('echo off')
    os.system('cls')
    print('PySSL maker')
    print('Verson: BA 0.0.1')
    print('Setting RSA Algorithms')

    print('$ KEY_SIZE ', end='')
    tmp = inputvalue(int)
    key_value = tmp if tmp != 'ENT' else DV.key_size
    print('$root>> SET KEY_SIZE TO \'%d\''%key_value)

    print('$ HOST_NAME ', end='')
    tmp = inputvalue()
    h_name = tmp if tmp != 'ENT' else DV.h_name
    print('$root>> SET HOST_NAME TO \'%s\''%h_name)

    print('$ SERVER IP ', end='')
    tmp = inputvalue()
    server_ip = tmp if tmp != 'ENT' else DV.server_ip
    print('$root>> SET SERVER IP TO \'%s\''%server_ip)

    print('$ PUBLIC EXPONENT ', end='')
    tmp = inputvalue(int)
    public_exponent = tmp if tmp != 'ENT' else DV.public_exponent
    print('$root>> SET PUBLIC EXPONENT TO \'%s\''%public_exponent)

    print('$ DAYS ', end='')
    tmp = inputvalue(int)
    days = tmp if tmp != 'ENT' else DV.days
    print('$root>> SET DAYS TO \'%s\''%days)

    print('$ SERIAL NUMBER ', end='')
    tmp = inputvalue(int)
    serialnum = tmp if tmp != 'ENT' else DV.serialnumber
    print('$root>> SET SERIAL NUMBER TO \'%s\''%serialnum)

    print('$ CERTIO ', end='')
    tmp = inputvalue(int)
    certio = tmp if tmp != 'ENT' else None
    print('$root>> SET CERTIO TO \'%s\''%certio)

    print('$ KEYIO ', end='')
    tmp = inputvalue(int)
    keyio = tmp if tmp != 'ENT' else None
    print('$root>> SET KEYIO TO \'%s\''%keyio)

    os.system('cls')
    print(f'{"all":=^50}')
    print(f'$ {"key_size:":20}\'%d\''%key_value)
    print(f'$ {"host_name:":20}\'%s\''%h_name)
    print(f'$ {"server ip:":20}\'%s\''%server_ip)
    print(f'$ {"public exponent:":20}\'%s\''%public_exponent)
    print(f'$ {"days:":20}\'%s\''%days)
    print(f'$ {"serial number:":20}\'%s\''%serialnum)
    print(f'$ {"certio:":20}\'%s\''%certio)
    print(f'$ {"keyio:":20}\'%s\''%keyio)
    print(f'Press any to next stop ', end='')
    inputvalue()

    os.system('cls')
    print(f'{"make":=^50}')
    print('$>> INITIALIZE PYSSQLMAKE: ', end='')
    try:
        a = makessl(
            key_size = key_value, 
            hostname = h_name, 
            server_ip = server_ip, 
            public_exponent = public_exponent,
            days = days,
            serialnumber = serialnum,
            certio = certio,
            keyio = keyio
        )
        print("SUCCESS")
    except:
        print('FAIL')
        exit(0)
    print('SUCCESS')

    print('$>> MAKE RSA KEY: ', end='')
    try:
        a.makekey()
        print("SUCCESS")
    except:
        print('FAIL')
        exit(0)

    print('$>> MAKE COMMON NAME: ', end='')
    try:
        a.makename()
        print("SUCCESS")
    except:
        print('FAIL')
        exit(0)

    print('$>> MAKE ALTERNATIVE NAME: ', end='')
    try:
        a.makealtenativename()
        print("SUCCESS")
    except:
        print('FAIL')
        exit(0)

    print('$>> MAKE BASIC CONSTRAINTS: ', end='')
    try:
        a.makebasicconstr()
        print("SUCCESS")
    except:
        print('FAIL')
        exit(0)

    print('$>> BUILD CERTIFICATE: ', end='')
    try:
        a.buildCert()
        print("SUCCESS")
    except:
        print('FAIL')
        exit(0)

    print('$>> MAKE PEM: ', end='')
    try:
        c, k = a.makepem()
        print("SUCCESS")
        print('CERTIFICATE PEM: ')
        print(c[:120].decode(), '...', c[-50:].decode())
        print('PRIVATE PEM: ')
        print(k[:120].decode(), '...', k[-50:].decode())
    except:
        print('FAIL')
        exit(0)

    print('$>> EXPORT FILE: ', end='')
    try:
        a.exportfile()
        print("SUCCESS")
    except:
        print('FAIL')
        exit(0)
    
    print(f'{"RESULT":=^50}')
    print(f'Certificate at: \'{os.path.abspath(a.certio)}\'')
    print(f'Private key at: \'{os.path.abspath(a.keyio)}\'')

runcmd()