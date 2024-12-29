import time
# this import time commands so i can make the code wait before doing something
import sys

# this imports system commands

user_balance = 100
# sets user balance

trans1 = "NA"
trans2 = "NA"
trans3 = "NA"
trans4 = "NA"
trans5 = "NA"
trans6 = "NA"
trans7 = "NA"
trans8 = "NA"
trans9 = "NA"
trans10 = "NA"

time.sleep(0.75)

print('''P.S The code is 1212.
      Don't use caps.
      You can only see your previous transcations''')

time.sleep(1)

print('welcome to A2Z Banking.')
print()

time.sleep(1)

attempts = True
# create a variable called attempts and set its value ti True

while attempts == True:
    attempt1 = input('please enter PIN:')
    if attempt1 == '1212':
        print('correct PIN')
        time.sleep(1)
        break

    else:
        print("Incorrect")
        time.sleep(0.75)
        attempt2 = input('please enter correct PIN:')
        if attempt2 == '1212':
            print("correct PIN")
            break

        else:
            print("Incorrect PIN")
            time.sleep(0.75)
            print("You have 1 more attempt:")
            attempt3 = input('please enter correct PIN:')
            if attempt3 == '1212':
                print("correct PIN")
                break
            else:
                print("Incorrect PIN")
                print('Wait 2 minutes to try again (or restart code):')
                time.sleep(120)
                print()

yes = 0
# create a variable and set the value to 0
valid_option = True
while valid_option == True:
    # creating an another loop
    time.sleep(0.75)
    menu = input('''
    
Please select an option:

Welcome to A2Z Banking
1- Display balance
2- Withdraw funds
3- Deposit funds
4- Print List of transactions
5- Return card
--->    ''')
    print()# printing the menu so we dont need create another variable to ask question
    if menu == "1":
        print("Display balance")
        print('$', user_balance)
        print()
        time.sleep(0.25)

    elif menu == "2":
        print("Withdraw Funds")
        time.sleep(0.75)
        wf = int(input('''
        How much would you like to withdraw?
        Your options are:
        10:
        20:
        50:
        100:
        7- Other(must be a multiple of 10):
        8- Return to main menu:
        9- Return card:
        --->:    '''))

        if wf == user_balance:
            print("Congraturations you broke, you now have $ 0 in your bank account")
            user_balance = 0
            never = 'Wtihdraw', wf

        elif wf > user_balance:
            print("you don't that much money")
            never = 0

            yes = yes - 1

        elif wf == 10:
            print("Successful withdrawn $ 10, you now have", user_balance - 10)
            user_balance = user_balance - wf
            never = 'Withdraw', wf

        elif wf == 20:
            print("Successful withdrawn $ 20, you now have", user_balance - 20)
            user_balance = user_balance - wf
            never = 'Withdraw', wf

        elif wf == 50:
            print("Successful withdrawn $ 50, you now have", user_balance - 50)
            user_balance = user_balance - wf
            never = 'Withdraw', wf

        elif wf == 100:
            print("Successful withdrawn $ 100, you now have", user_balance - 100)
            user_balance = user_balance - wf
            never = 'Withdraw', wf

        elif wf == 7:
            print("Other amount")
            ea = int(input("How much would you like to withdraw?:"))

            if ea == user_balance:
                print("Congratulations you broke, you now have $ 0 in your bank account")
                user_balance = 0
                never = 'Withdraw', ea

            elif ea > user_balance:
                print("you don't have that much money")
                never = never
                yes = yes - 1

            elif ea % 10 == 0:
                print("Successfully withdraw $", ea, "you now have $", user_balance - ea)
                user_balance = user_balance - ea
                never = 'withdraw', ea

            else:
                print("Invalid")
                print("Make sure it is a multiple of 10 and numbers only")
                never = never
                yes = yes - 1

        elif wf == 8:
            print()
            never = never
            yes = yes - 1

        elif wf == 9:
            print('thank you for banking at A2Z Bank')
            sys.exit()
        else:
            print("Invalid")
            yes = yes - 1

        yes = yes + 1

        if yes > 10:

            trans1 = trans2
            trans2 = trans3
            trans3 = trans4
            trans4 = trans5
            trans5 = trans6
            trans6 = trans7
            trans7 = trans8
            trans8 = trans9
            trans9 = trans10
            trans10 = never

        elif yes == 1:
            trans1 = never

        elif yes == 2:
            trans2 = never

        elif yes == 3:
            trans3 = never

        elif yes == 4:
            trans4 = never

        elif yes == 5:
            trans5 = never

        elif yes == 6:
            trans6 = never

        elif yes == 7:
            trans7 = never

        elif yes == 8:
            trans8 = never

        elif yes == 9:
            trans9 = never

        elif yes == 10:
            trans10 = never

    elif menu == "3":
        print("Deposit Funds")
        EA = int(input('''

choose an option:
1- Deposit
2- Return to main menu         
9- Return card                
--->: '''))

        if EA == 1:
            dp = int(input("How much would you like to deposit?:"))
            if dp > 0:
                print("Successfully deposited", dp, "you have now $", user_balance + dp)
                user_balance = user_balance + dp
                never = 'deposited', dp

            elif dp < 0:
                print("You cant't use negative numbers")
                never = never
                yes = yes - 1
        elif EA == 2:
            print()
            never = never
            yes = yes - 1

        elif EA == 9:
            print("Thank you for using A2Z banking:")
            sys.exit()

        yes = yes + 1
        if yes > 10:
            trans1 = trans2
            trans2 = trans3
            trans3 = trans4
            trans4 = trans5
            trans5 = trans6
            trans6 = trans7
            trans7 = trans8
            trans8 = trans9
            trans9 = trans10
            trans10 = never

        elif yes == 1:
            trans1 = never

        elif yes == 2:
            trans2 = never

        elif yes == 3:
            trans3 = never

        elif yes == 4:
            trans4 = never

        elif yes == 5:
            trans5 = never

        elif yes == 6:
            trans6 = never

        elif yes == 7:
            trans7 = never

        elif yes == 8:
            trans8 = never

        elif yes == 9:
            trans9 = never

        elif yes == 10:
            trans10 = never

    elif menu == "4":
        print("Print the list of transactions")
        time.sleep(0.75)
        print()
        print(trans1)
        print(trans2)
        print(trans3)
        print(trans4)
        print(trans5)
        print(trans6)
        print(trans7)
        print(trans8)
        print(trans9)
        print(trans10)
    elif menu == "9":
        print("Thank you for using A2Z banking:")
        sys.exit()

    else:
        print("please choose a valid option")