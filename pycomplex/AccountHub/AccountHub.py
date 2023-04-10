import subprocess
import time
from time import sleep
import logging
import ctypes
import sys
import re
import getpass
import os
from halo import Halo
from rich.console import Console
from rich.style import Style
from rich.table import Table
from rich.panel import Panel
from rich.spinner import Spinner


console = Console()
logging.basicConfig(filename='user_accounts.log', level=logging.INFO,format='%(asctime)s:%(levelname)s:%(message)s')

console.print("WELCOME TO AccountHub .. .. ..", style=Style(color="green", bold=True, italic=True, underline=True, bgcolor="white"), justify="center")
console.print(" To get all functionalities you should run this program as administrator enjoy....", style=Style(color="dark_blue", bold=True, bgcolor="white"),justify="center")
console.print(Panel("Welcome to My Application! AccountHub ", style="bold magenta"),justify="center")
if not ctypes.windll.shell32.IsUserAnAdmin():
        console.print(Panel("You are not running this program as Administrator you might have limited access....", style="bold magenta"),justify="center")
        logging.error("Admin permission is required to delete a user account. Please run the program as an administrator.")

spinner = Halo(text='Loading...', spinner='dots',color='green')
spinner.start()
time.sleep(5)

def create_account():
    username = input("Username : ")
##    contain 8 characters long, at least one digit,at least one uppercase letter
    console.print(Panel("Password enter password ",style="bold red"),justify="center")
    password = input("Password : ")
    confirmpassword = input("Confirm password : ")
    # Validate username
    if not re.match("^[a-zA-Z ]+$", username):
        console.print(Panel("Username must only contain alphabetic characters and spaces.",style="bold red"),justify="center")
        logging.error("Username must only contain alphabetic characters and spaces.")
        return
##    if len(password) < 8:
##        console.print("Password must be at least 8 characters long.", style=Style(color="red", bgcolor="white"), justify="center")
##        logging.error("Password must be at least 8 characters long.")
##        return
    if password !=confirmpassword:
        console.print(Panel("Password does not match",style="bold red"),justify="center")
        logging.error("Password must be the same.")
        return
##    if not any(char.isdigit() for char in password):
##        console.print("Password must contain at least one digit.", style=Style(color="red", bgcolor="white"), justify="center")
##        logging.error("Password must contain at least one digit.")
##        return
##    if not any(char.isupper() for char in password):
##        console.print("Password must contain at least one uppercase letter.", style=Style(color="red", bgcolor="white"), justify="center")
##        logging.error("Password must contain at least one uppercase letter.")
##        return

    if not ctypes.windll.shell32.IsUserAnAdmin():
        console.print(Panel("Admin permission is required to create a new user account. Please run the program as an administrator. ",style="bold magenta"),justify="center")
        logging.error("Admin permission is required to create a new user account. Please run the program as an administrator.")
        return

    command = f"net user \"{username}\" {password} /add"
    try:
        subprocess.check_call(command, shell=True)
        logging.info(f"User account \"{username}\" was created successfully!")
        console.print(Panel(f"User account \"{username}\" was created successfully!",style="bold green"),justify="center")
        time.sleep(5)
    except subprocess.CalledProcessError as error:
        logging.error(f"Error creating user account \"{username}\": {error}")
        console.print(f"Error creating user account \"{username}\": {error}", style=Style(color="red"), justify="center")
    return

def delete_account():
    username = input("Username : ")
    console.print(Panel("YOU ARE ABOUT TO DELETE USER ACCOUNT", style="bold magenta"),justify="center")
    spinner.start()
    sleep(3)
    spinner.stop()
    if not ctypes.windll.shell32.IsUserAnAdmin():
        console.print(Panel("Admin permission is required to delete a user account . Please run the program as an administator. ",style="bold magenta"),justify="center")
        logging.error("Admin permission is required to delete a user account. Please run the program as an administrator.")
        return

    command = f"net user \"{username}\" /delete"
    try:
        subprocess.check_call(command, shell=True)
        logging.info(f"User account \"{username}\" was deleted successfully!")
        console.print(Panel(f"User account \"{username}\" was deleted successfully!",style="bold green"),justify="center")
    except subprocess.CalledProcessError as error:
        logging.error(f"Error deleting user account \"{username}\": {error}")
        loggingerror = logging.error(f"Error deleting user account \"{username}\": {error}")
        console.print(Panel(f"Error deleting user account \"{username}\": {loggingerror}",style="bold red"),justify="center")
    spinner.start()
    time.sleep(5)
    spinner.stop()
    console.print("Done!",style=Style(color="green"))
    return
def list_account():
    command = f"net user"
    try:
        output = subprocess.check_output(command, shell=True)
        logging.info("List of user accounts:\n" + output.decode('utf-8'))
        console.print(output.decode('utf-8'), style=Style(color="white", bgcolor="green"), justify="left")
    except subprocess.CalledProcessError as error:
        logging.error(f"Error listing user accounts: {error}")
        console.print(Panel(f"Error listing user accounts: {error}",style="bold red"),justify="center")


def create_accountas(username, password):
##    print("Password should contain  characters long, at least one digit, at least one uppercase letter")
##    # Validate username
##    if not re.match("^[a-zA-Z ]+$", username):
##        print("Username must only contain alphabetic characters and spaces.")
##        logging.error("Username must only contain alphabetic characters and spaces.")
##        return
##    if len(password) > 0 :
##        print("Password must be at least 8 characters long.")
##        logging.error("Password must be at least 8 characters long.")
##        return
####    if password != confirmpassword:
####        print("Password does not match")
####        logging.error("Password must be the same.")
####        return
##    if not any(char.isdigit() for char in password):
##        print("Password must contain at least one digit.")
##        logging.error("Password must contain at least one digit.")
##        return
##    if not any(char.isupper() for char in password):
##        print("Password must contain at least one uppercase letter.")
##        logging.error("Password must contain at least one uppercase letter.")
##        return
##
    if not ctypes.windll.shell32.IsUserAnAdmin():
        console.print(Panel("Admin permission is required to create a new user account. Please run the program as an administrator. ",style="bold magenta"),justify="center")
        logging.error("Admin permission is required to create a new user account. Please run the program as an administrator.")
        return

    command = f"net user \"{username}\" {password} /add"
    try:
        subprocess.check_call(command, shell=True)
        logging.info(f"User account \"{username}\" was created successfully!")
        console.print(Panel(f"User account \"{username}\" was created successfully!",style="bold green"),justify="center")
    except subprocess.CalledProcessError as error:
        logging.error(f"Error creating user account \"{username}\": {error}")
        console.print(Panel(f"Error creating user account \"{username}\": {error}",style="bold red"),justify="center")
    print("\n\n")

def create_multiple_accounts():
    console.print(Panel("Enter username and password separated by ',' and multiple accounts separated by '/': ",style="bold purple4"),justify="center")
    input_string = input(">")
    accounts = input_string.split('/')
    accounts_list = []
    for account in accounts:
        if account:
            account_parts = account.split(',')
            if len(account_parts) == 2:
                username = account_parts[0].strip()
                password = account_parts[1].strip()
                accounts_list.append((username, password))
    for account in accounts_list:
        username, password = account
        console.print(Panel(f"Creating account for {username}...",style="bold green"),justify="center")
        create_accountas(username, password)

def delete_multiple_account(username):
    if not ctypes.windll.shell32.IsUserAnAdmin():
        console.print(Panel("Admin permission is required to delete a user account . Please run the program as an administator. ",style="bold magenta"),justify="center")
        logging.error("Admin permission is required to delete a user account. Please run the program as an administrator.")
        return

    command = f"net user \"{username}\" /delete"
    try:
        subprocess.check_call(command, shell=True)
        logging.info(f"User account \"{username}\" was deleted successfully!")
        console.print(Panel(f"User account \"{username}\" was deleted successfully!",style="bold green"),justify="center")
    except subprocess.CalledProcessError as error:
        logging.error(f"Error deleting user account \"{username}\": {error}")
        console.print(Panel(f"Error deleting user account \"{username}\": {error}",style="bold red"),justify="center")
    print("\n\n")
    return


def delete_multiple_accounts():
    input_delete = input("Enter usernames separated by /: ")
    accounts = input_delete.split('/')
    accounts_list=[]
    for account in accounts:
        username = account.strip()
        console.print(Panel(f"deleting {username}....",style="bold green"),justify="center")
        delete_multiple_account(username)


def manage_accounts():
     while True:

        table = Table(show_header=False, title="Select an option:",style=Style(color="royal_blue1"))
        table.add_column("")
        table.add_column("Option")

        table.add_row("1", "Change account password.", style=Style(bgcolor="white", color="black"))
        table.add_row("2", "See all accounts.", style=Style(bgcolor="white", color="black"))
        table.add_row("3", "Logging History.", style=Style(bgcolor="white", color="black"))
        table.add_row("4", "Delete account.", style=Style(bgcolor="white", color="black"))
        table.add_row("5", "Return home menu.", style=Style(bgcolor="white", color="black"))

        console.print(table,justify="center")
        choice = input("Enter choice: ")

        if choice == "1":
            change_password()
        elif choice == "2":
            list_account()
        elif choice == "3":
            with open("user_accounts.log") as file:
                print(file.read())
        elif choice == "4":
            table = Table(show_header=False, title="Select an option:",style=Style(color="royal_blue1"))
            table.add_column("")
            table.add_column("Option")

            table.add_row("1", "delete single account", style=Style(bgcolor="white", color="black"))
            table.add_row("2", "delete multiple account", style=Style(bgcolor="white", color="black"))
            table.add_row("3", "return home menu", style=Style(bgcolor="white", color="black"))

            console.print(table,justify="center")
            try:
                delter = int(input("Enter choice: "))
                if delter == 1:
                    delete_account()
                    break
                elif delter == 2:
                    delete_multiple_accounts()
                    break
                elif choose == 3:
                    main()
                else:
                    console.print(Panel("enter correct value",style="bold red"),justify="center")
            except ValueError:
                console.print(Panel("Enter a valid integer choice (1 or 2)",style="bold red"),justify="center")
        elif choice =="5":
            main()
        else:
            console.print(Panel("Invalid choice. Try again.",style="bold red"),justify="center")

def change_password():
    username = input("username: ")
    new_password = input("Enter new password: ")
    cmd = f"net user {username} {new_password}"
    result = subprocess.run(cmd, shell=True, capture_output=True)
    if result.returncode == 0:
        console.print(Panel("Password changed successfully.",style="bold green"),justify="center")
    else:
        console.print(Panel("Error changing password.",style="bold red"),justify="center")
def about():
    spinner.start()
    time.sleep(2)
    table = Table(show_header=False, title="ABOUT DEVELOPER ....", style=Style(color="royal_blue1"))
    table.add_column("")
    table.add_column("Option")

    table.add_row("1","DEVELOPER", "YHACKER KENNY","KENNEDY NNKO",style=Style(bgcolor="white", color="black"))
    table.add_row("2","FACEBOOK", "YHACKER KENNY","KENNEDY NNKO",style=Style(bgcolor="white", color="black"))
    table.add_row("3","INSTAGRAM", "YHACKER_KENNY",style=Style(bgcolor="white", color="black"))
    table.add_row("4","YOUTUBE", "YHACKER KENNY",style=Style(bgcolor="white", color="black"))
    table.add_row("5","CONTACT", "+255752994381",style=Style(bgcolor="white", color="black"))
    table.add_row("6","GITHUB", "YHACKERXL.GITHUB.IO",style=Style(bgcolor="white", color="black"))
    console.print(table, justify="center")

spinner.stop()
#console.clear()
def main():
    while True:
        table = Table(show_header=False, title="Select an option:",style=Style(color="royal_blue1"))
        table.add_column("")
        table.add_column("Option")

        table.add_row("1", "Create new account",style=Style(bgcolor="white", color="black"))
        table.add_row("2", "Manage Accounts",style=Style(bgcolor="white", color="black"))
        table.add_row("3", "About",style=Style(bgcolor="white", color="black"))
        table.add_row("4", "Exit",style=Style(bgcolor="white", color="black"))

        console.print(table, justify="center")


        a = input("Enter the selection from 1-4 ?  ")
        if a == "1":
            table = Table(show_header=False, title="Select an option:",style=Style(color="royal_blue1"))
            table.add_column("")
            table.add_column("Option")

            table.add_row("1", "create single account", style=Style(bgcolor="white", color="black"))
            table.add_row("2", "create multiple account", style=Style(bgcolor="white", color="black"))
            table.add_row("3", "return home menu", style=Style(bgcolor="white", color="black"))

            console.print(table,justify="center")
            try:
                choose = int(input("Enter choice: "))
                if choose == 1:
                    create_account()
                elif choose == 2:
                    create_multiple_accounts()
                elif choose == 3:
                    main()
                else:
                    console.print(Panel("enter correct value :",style="bold red"),justify="center")
            except ValueError:
                console.print(Panel("Enter a valid integer choice ",style="bold red"),justify="center")
        elif a == "2":
            manage_accounts()
        elif a == "3":
            about()
        elif a == "4":
            console.print("Exiting the program...", style=Style(color="white", bgcolor="white"), justify="center")
            logging.info("Exiting the program...")
            console.print(Panel("Thank you for using our program welcome again !!!!!",style="bold cyan"),justify="center")
            console.print(Panel("dEVELOPED BY YHACKER KENNY 69", style="bold magenta"),justify="center")
            sleep(7)
            sys.exit()
        else:
            console.print(Panel("Invalid input. Please enter a number from 1-4.", style="bold red"),justify="center")
        console.print(Panel("\nReturning to main menu...", style="bold purple4"),justify="center")
main()