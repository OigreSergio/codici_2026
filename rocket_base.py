import socket

# Variabili per tupla oggetto s
SRV_ADDR = "0.0.0.0"
SRV_PORT = 44446


# crea oggetto per connessione ipv4 (AF_INET) in tcp (SOCK_STREAM)
s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

# per far in modo che quando si avvia usi l'ip SRV_ADDR e la porta SRV_PORT
s.bind((SRV_ADDR , SRV_PORT))

# Quando ti avvierai devi metterti in ascolto e accettare una connessione 
s.listen(1)

# dimostrazione che sta in ascolto prima di avviare  
print("Sono in attesa di connessione .. ")

connection , address = s.accept()

# avverto l'utente che la connessione è avvenuta 
print ("Mi sono collegato con : ",address)

# creazione ciclo infinito per gestire la connessione

while True :

    # dichiarare per quanti byte vogliamo accettare in gestione  
    data = connection.recv(1024)

    # se la connessione crolla esci 
    if not data: 
        break
    # stampa ciò che ricevi convertendolo da byte a caratteri
    print(data.decode('utf-8'))

connection.close()

