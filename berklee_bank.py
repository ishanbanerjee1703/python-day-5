bank_dict = {
    "Priya": {"balance": 100, "pin": "4821"},
    "Carlos": {"balance": 300, "pin": "1092"},
    "Amira": {"balance": 0, "pin": "0000"},
    "Jordan": {"balance": 7788, "pin": "9999"},
}

'''
Name: wecome_message
Task: Show welcome message
Input: none
Side Effects: Print "Welcome to Berklee Bank!"
Return: none
'''
def welcome_message():
    print("Welcome to Berklee Bank!")
    
    


'''
Name: input_name
Task: inpout name and see if its a key value
Input: none
Side Effects: print what is your name
Return: return name
'''
def input_name():
    name = input("What is your name? ")
    return name
    


'''
Name: input_pin
Task: ask for pin and see if it exsits
Input: none
Side Effects: print what is pin
return: return pin
'''
def input_pin():
    pin = input("What is your pin? ")
    return pin 
    

'''
Name: verify_identity
Task:  take name and pin and see if valid user in system, if so get data. if not, error message
Input: username, pin
Side Effects: access granted if they exist. if they dont exist, say access denied
Return: none
'''
def verify_identity(username, pin):
    if bank_dict.get(username):
        users_values = (bank_dict.get(username))
        if pin == users_values.get("pin"):
            return True
        print("Access Denied for", username, "with pin", pin)
    return False

        

    
'''
Name: display_menu
Task:  show all the options, and ask what they want
Input: 
Side Effects: do you want to deposit, withdraw, check balance, quit (they type answer)
Return: string the user typed in
'''
def display_menu():
    choice = input("Do you want to: deposit, withdraw, balance or quit?")
    return choice
    


'''
Name: check_balance
Task:  checks balance for user
Input: username
Side Effects: print balance
Return: none
'''
def check_balance(username):
    if bank_dict.get(username):
        users_values = bank_dict.get(username)
        balance = user_values.get("balance")
        print("Your balance is: " balance)
    
    return None
    


'''
Name: deposit_money
Task:  add money to balance
Input: username
Side Effects: prompt user for deposit amount
Return: none
'''
def deposit_money(username):
    deposit_amount = int(input("How much would you like to deposit? "))
    if bank_dict.get(username):
        users_values = bank_dict.get(username)
        previous_bal = users_values.get("balance") 
        new_bal = previous_bal + deposit_amount
        users_values.update({"balance": new_bal})

    return None
    
    


'''
Name: withdraw_money
Task:  ask how much money to removes from balance. if they have enough, reduce. if not, tell insufficient fund
Input: username
Side Effects: prompt user for amount to withdraw, telling if successful or not
Return: none
'''
def withdraw_money(username):
    withdraw_amount = int(input("How much would you like to withdraw? "))
    if bank_dict.get(username):
        users_values = bank_dict.get(username)
        previous_bal = users_values.get("balance") 
        new_bal = previous_bal - withdraw_amount
        if new_bal < 0: 
            print("Insufficient Funds...")
        else: 
            users_values.update({"balance": new_bal})

    

'''
Name: quit_atm
Task:  stop the program and quit
Input: 
Side Effects: print "thank you"
Return: none
'''
def quit_atm():
    pass

def run_tests():
    withdraw_money("Priya") # asks for amount, if 200 fail
    withdraw_money("Priya") # asks for amount, if 100 should success

    deposit_money("Priya") # asks for amount, if 100 should succeed

    check_balance("Priya") # Print $100

    verify_identity("Priya", "4821") # Expect successful log in
    verify_identity("Priya", "0000") # expect fail log in

