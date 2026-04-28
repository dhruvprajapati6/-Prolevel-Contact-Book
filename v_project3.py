# create contact book to perform
# 1. add contact
# 2. serch contact
# 3. update cotact
# 4. delete contact

contacts = {}

print("📘 Prolevel Contact Book")

while True:
    print("\n===== MENU =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter choice (1-6): ")

    # ➤ Add Contact
    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        contacts[name] = phone
        print("✅ Contact Saved!")

    # ➤ View Contacts
    elif choice == "2":
        if contacts:
            print("\n📋 Contact List:")
            for name, phone in contacts.items():
                print(name, ":", phone)
        else:
            print("⚠️ No contacts found!")

    # ➤ Search Contact
    elif choice == "3":
        search = input("Enter name to search: ")
        if search in contacts:
            print("📞 Number:", contacts[search])
        else:
            print("❌ Contact not found!")

    # ➤ Update Contact
    elif choice == "4":
        name = input("Enter name to update: ")
        if name in contacts:
            new_phone = input("Enter new number: ")
            contacts[name] = new_phone
            print("✏️ Contact Updated!")
        else:
            print("❌ Contact not found!")

    # ➤ Delete Contact
    elif choice == "5":
        name = input("Enter name to delete: ")
        if name in contacts:
            del contacts[name]
            print("🗑️ Contact Deleted!")
        else:
            print("❌ Contact not found!")

    # ➤ Exit
    elif choice == "6":
        print("👋 Exiting Contact Book")
        break

    else:
        print("❌ Invalid choice!")
