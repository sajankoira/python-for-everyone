"""
PROJECT 4: Contact Book (JSON + OOP)
"""
import json
import os

FILE = "contacts.json"

class ContactBook:
    def __init__(self):
        self.contacts = {}
        self.load()

    def load(self):
        if os.path.exists(FILE):
            with open(FILE, "r") as f:
                self.contacts = json.load(f)

    def save(self):
        with open(FILE, "w") as f:
            json.dump(self.contacts, f, indent=2)

    def add(self, name, phone, email=""):
        self.contacts[name] = {"phone": phone, "email": email}
        self.save()
        print(f"Added {name}")

    def search(self, name):
        for key, val in self.contacts.items():
            if name.lower() in key.lower():
                print(f"{key}: {val}")

    def list_all(self):
        if not self.contacts:
            print("No contacts")
            return
        for name, info in self.contacts.items():
            print(f"{name} -> {info['phone']} | {info['email']}")

    def delete(self, name):
        if name in self.contacts:
            del self.contacts[name]
            self.save()
            print(f"Deleted {name}")
        else:
            print("Not found")

def main():
    book = ContactBook()
    while True:
        print("\n1. Add 2. Search 3. List 4. Delete 5. Exit")
        ch = input("Choice: ")
        if ch == "1":
            name = input("Name: ")
            phone = input("Phone: ")
            email = input("Email (optional): ")
            book.add(name, phone, email)
        elif ch == "2":
            book.search(input("Search name: "))
        elif ch == "3":
            book.list_all()
        elif ch == "4":
            book.delete(input("Delete name: "))
        elif ch == "5":
            break

if __name__ == "__main__":
    main()
