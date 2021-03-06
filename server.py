import socket
import threading

IP = socket.gethostbyname(socket.gethostname())
PORT = 5566
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"
QUIT_MSG = "QUIT"

def handle_client(conn, addr):
  print(f"[NOVA CONEXAO] {addr} conectado.")

  connected = True
  while connected:
    msg = conn.recv(SIZE).decode(FORMAT)
    if msg == QUIT_MSG:
      connected = False
    
    print(f"[{addr}] {msg}")
    msg = f"Mensagem recebida: {msg}"
    conn.send(msg.encode(FORMAT))

  conn.close()

def main():
  print("[INICIANDO] Servidor esta iniciando...")
  server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  server.bind(ADDR)
  server.listen()
  print(f"[ESCUTANDO] Servidor esta escutando em {IP}:{PORT}")

  while True:
    conn, addr = server.accept()
    thread = threading.Thread(target=handle_client, args=(conn, addr))
    thread.start()
    print(f"[CONEXOES ATIVAS] {threading.activeCount() - 1}")

if __name__ == "__main__":
  main()