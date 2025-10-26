import time
import dbatm

def main():
    print("Please insert Your CARD")


    time.sleep(3)

    password=6660

    pin=int(input("enter your atm pin "))

    balance=60000

    if pin==password:
        while True:
        

            print("""

            1 == Balance

            2 == Withdraw balance

            3 == Deposit balance

            4 == exit

            """)

            try:

                option=int(input("Please enter your choise "))

            except:

                print("Please enter valid option")
                
            if option==1:
                print("=====================================================")

                print (f"Yuor current balance is {balance}")

                print("=====================================================")
                print("=====================================================")
                
                obj=dbatm.connectdb()
                obj.Balance(balance)
                

            if option==2:
                print("=====================================================")

                withdraw_amount=int(input("please enter withdraw_amount "))
                
                print("=====================================================")
                print("=====================================================")

                balance = balance - withdraw_amount
         
                print(f"{withdraw_amount} is debited from your account")
                
                print("=====================================================")
                print("=====================================================")

                print (f"your updated balance is {balance}")
                
                print("=====================================================")
                print("=====================================================")

                obj=dbatm.connectdb()
                obj.withdrawn(balance,withdraw_amount)

            
            if option==3:
                print("=====================================================")

                deposit_amount=int(input("please enter deposit_amount"))

                print("=====================================================")
                print("=====================================================")

                balance = balance+deposit_amount

                print(f"{deposit_amount} is credited to your account")

                print("=====================================================")
                print("=====================================================")
                

                print(f"your updated balance is {balance}")

                obj=dbatm.connectdb()
                obj.deposite(balance,deposit_amount)

            if option ==4:
               

                break

    else:
        print("Invalid pin please try again later")


main()