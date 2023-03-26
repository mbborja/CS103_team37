from transaction import Transaction
import sys

def print_usage():
    print('''usage (enter number):
            1. show categories
            2. add category
            3. modify category (old, new)
            4. show transactions
            5. add transaction
            6. delete transaction (item number)
            7. summarize transactions by date
            8. summarize transactions by month
            9. summarize transactions by year
            10. summarize by category
            11. print menu
            '''
            )


def process_args(arglist):
    transactions = Transaction('tracker.db') 
    if arglist == []:
        print_usage()
    elif arglist[0] == "1":
        transactions.show_categories()
    elif arglist[0] == "2":
        if len(arglist) != 1:
            print_usage()
        else:
            transactions.add_category(arglist[1])
            #some issue with adding and showing categories 
    elif arglist[0] == "3":
        if len(arglist) != 3:
            print_usage()
        else:
            transactions.modify_category(arglist[1], arglist[2])
    elif arglist[0] == "4":
        transactions.show_transactions()
    elif arglist[0] == "5":
        if len(arglist) != 6:
            print_usage()
        else:
            transaction = {'item_number':arglist[1], 'amount':arglist[2], 'category':arglist[3], 'date':arglist[4], 'description':arglist[5]} #(item #, amount, category, date, description)
            transactions.add_transaction(transaction)
    elif arglist[0] == "6":
        if len(arglist) != 2:
            print_usage()
        else:
            transactions.delete_transaction(arglist[1])
    elif arglist[0] == "7":
        transactions.summarize_by_date()  #dont know if this works
    elif arglist[0] == "8":
        print("not yet implemented")
        #transactions.summarize_by_month()
    elif arglist[0] == "9":
        print("not yet implemented")
        #transactions.summarize_by_year()
    elif arglist[0] == "10":
        print("not yet implemented")
        #transactions.summarize_by_category()
    elif arglist[0] == "11":
        print_usage()
    else:
        print(arglist, "is not implemented")
        print_usage()


def toplevel():
    ''' read the command args and process them'''
    if len(sys.argv)==1:
        # they didn't pass any arguments, 
        # so prompt for them in a loop
        print_usage()
        args = []
        while args!=['']:
            args = input("command> ").split(' ')
            if args[0]=='add':
                # join everyting after the name as a string
                args = ['add',args[1]," ".join(args[2:])]
            process_args(args)
            print('-'*40+'\n'*3)
    else:
        # read the args and process them
        args = sys.argv[1:]
        process_args(args)
        print('-'*40+'\n'*3)

toplevel()