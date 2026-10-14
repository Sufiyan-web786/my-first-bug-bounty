# SECURE LOGIN - Sahi tarika
import sqlite3
print("=== Secure Login ===")
user = input("Username: ")
password = input("Password: ")

# Sahi tarika -? use karo, direct string mat jodo
# conn.execute("SELECT * FROM users WHERE name=? AND pass=?", (user, password))
print(f"\n[SAFE] Tumne likha: {user}")
print("Database isko sirf TEXT samjhega, CODE nahi!")
print("Ab ' OR '1'='1 likhne se bhi hack nahi hoga - Blocked!")
