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
Side Effects: Print "Welcome to Berklee Bank"
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
    pass
    


'''
Name: input_pin
Task: ask for pin and see if it exsits
Input: 
Side Effects: print what is pin
return: return pin
'''
def input_pin():
    pass
    

'''
Name: verify_identity
Task:  take name and pin and see if valid user in system, if so get data. if not, error message
Input: username, pin
Side Effects: access granted if they exist. if they dont exist, say access denied
Return: none
'''
def verify_identity():
    pass

    
'''
Name: display_menu
Task:  show all the options, and ask what they want
Input: 
Side Effects: do you want to deposit, withdraw, check balance, quit (they type answer)
Return: string the user typed in
'''
def display_menu():
    pass
    


'''
Name: check_balance
Task:  checks balance for user
Input: username
Side Effects: print balance
Return: none
'''
def check_balance():
    pass
    


'''
Name: deposit_money
Task:  add money to balance
Input: username
Side Effects: prompt user for deposit amount
Return: none
'''
def deposit_money():
    pass
    


'''
Name: withdraw_money
Task:  ask how much money to removes from balance. if they have enough, reduce. if not, tell insufficient fund
Input: username
Side Effects: prompt user for amount to withdraw, telling if successful or not
Return: none
'''
def withdraw_money():
    pass
    

'''
Name: quit_atm
Task:  stop the program and quit
Input: 
Side Effects: print "thank you"
Return: none
'''
def quit_atm():
    pass
