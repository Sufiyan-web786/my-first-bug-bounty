# VULNERABLE LOGIN - Galat tarika
print("=== Nakli Login Test ===")
user = input("Username: ")
password = input("Password: ")

# Ye hai database ka query (galat tarika)
query = f"SELECT * FROM users WHERE name='{user}' AND pass='{password}'"
print(f"\nDatabase me ye chalega: {query}")

# Hacker ye daalega: ' OR '1'='1
if "' OR '1'='1" in query or "' OR 1=1" in query:
    print("\n[!!!] HACK SUCCESSFUL! Bina password ke login ho gaya!")
    print("Hacker admin ban gaya!")
else:
    if user == "sufiyan_ansari_00786" and password == "12345":
        print("\n[OK] Login sahi hai")
    else:
        print("\n[X] Galat password")
