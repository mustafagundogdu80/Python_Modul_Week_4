# membership_transactions.py

import file_transactions,  drawing

def add_member(members, members_file):
    """
    Adds a new member to the list of members.
    """
    if len(members) == 0:
        member_id = 1
    else:
        member_id = max(member["id"] for member in members) + 1
    name = input("Enter the member's name and surname: ")
    member_tel = input("Enter the member's phone number: ")
    member_address = input("Enter the member's address: ")
    member = {
        "id": member_id,
        "name": name,
        "tel": member_tel,
        "address": member_address
    }
    members.append(member)
    print("Member added successfully.")
    file_transactions.save_file(members_file, members)
    return members

def update_member(members, members_file):
    """
    Updates the information of a member.
    """
    member_id = int(input("Enter the ID of the member to update: "))
    for member in members:
        if member["id"] == member_id:
            name = input("Enter the member's new name and surname: ")
            member_tel = input("Enter the member's new phone number: ")
            member_address = input("Enter the member's new address: ")
            member["name"] = name
            member["tel"] = member_tel
            member["address"] = member_address
            print("Member updated successfully.")
            file_transactions.save_file(members_file, members)
            return members
    print("Member not found.")
    return members

def delete_member(members, members_file):
    """
    Deletes a member from the list of members.
    """
    member_id = int(input("Enter the ID of the member to delete: "))
    for member in members:
        if member["id"] == member_id:
            members.remove(member)
            print("Member deleted successfully.")
            file_transactions.save_file(members_file, members)
            return members
    print("Member not found.")
    return members

def list_members(members, kwargs=None):
    """
    Lists all members in the list of members.
    """
    if kwargs :
        members_list = []
        for member in members:
            for key, value in kwargs.items():
                if member[key] == value:
                    members_list.append(member)
    else:
        members_list = members
    for i in drawing.create_grid(members_list, ["id", "name", "tel", "address"], [10, 40, 15, 50], "Members"):
        print(i)

def search_members(members):
    """
    Searches for members in the list of members.
    """
    search_dicttionary = {}
    while True:
        print("Search by:")
        print("1. ID")
        print("2. Name")
        print("3. Phone number")
        print("4. Address")
        print("Q. Quit")
        Choose = input("Enter your choice: ")
        if Choose in ["Q", "q", "exit", "quit"]:
            break
        elif Choose == "1":
            search_dicttionary["id"] = int(input("Enter the member's ID: "))
        elif Choose == "2":
            search_dicttionary["name"] = input("Enter the member's name: ")
        elif Choose == "3":
            search_dicttionary["tel"] = input("Enter the member's phone number: ")
        elif Choose == "4":
            search_dicttionary["address"] = input("Enter the member's address: ")
        else:
            print("Invalid choice.")
    list_members(members, search_dicttionary)