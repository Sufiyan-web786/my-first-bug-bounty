import socket
print("🔍 Sufiyan's Subdomain Finder")
t = input("Domain: ")
for s in ["www","mail","api","admin","blog","test"]:
    try:
        print(f"[FOUND] {s}.{t} -> {socket.gethostbyname(f'{s}.{t}')}")
    except: 
        print(f"[NOT] {s}.{t}")
