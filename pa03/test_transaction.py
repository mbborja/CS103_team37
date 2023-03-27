import pytest
from transaction import Transaction

def test_transaction():
    x1 = Transaction("transactions.db")
    x1.delete_transaction('0')
    x1.delete_transaction('1')
    x1.delete_transaction('2')
    x1.delete_transaction('3')

    
    test1 = {'item_number':0,'amount':20,'category':"catfood",'date':"Today",'description':'Funny'}
    test2 = {'item_number':1,'amount':20,'category':"dogfood",'date':"Today",'description':'Funny'}

    test3 = {'item_number':2,'amount':20,'category':"catfood",'date':"03.26.2023",'description':'Funny'}
    test4 = {'item_number':3,'amount':20,'category':"catfood",'date':"03.27.2023",'description':'Funny'}
    #test5 = {'item_number':5,'amount':20,'category':"dogfood",'date':"Tomorrow",'description':'Funny'}



    #x1.add_transaction(test1)
    # #x1.delete_transaction('0')
    # print(x1.show_transactions())
    # print(x1.show_categories())



    #Test 4. show_transaction and 5. add_transaction - Marco
    x1.add_transaction(test1)
    x1.add_transaction(test2)
    #print(x1.show_transactions())
    #print("-------------")
    assert x1.show_transactions() == [{'item_number': 0, 'amount': 20.0, 'category': 'catfood', 'date': 'Today', 'description': 'Funny'}, {'item_number': 1, 'amount': 20.0, 'category': 'dogfood', 'date': 'Today', 'description': 'Funny'}]
    
    #Test 6. delete_transaction
    x1.delete_transaction('1')
    assert x1.show_transactions() == [{'item_number': 0, 'amount': 20.0, 'category': 'catfood', 'date': 'Today', 'description': 'Funny'}]

    #Test 7. Summarize by date - Noah
    x1.add_transaction(test2)
    #x1.add_transaction(test5)
    #print(x1.summarize_by_date())
    assert x1.summarize_by_date() == [{'date': 'Today', 'total': 40.0}]

    #Test 8. Summarize by month - Noah
    x1.delete_transaction('0')
    x1.delete_transaction('1')
    x1.add_transaction(test3)
    x1.add_transaction(test4)
    assert x1.summarize_by_month() == [{'month': '03', 'total': 40.0}]

    #Test 9. Summarize by year - Noah
    assert x1.summarize_by_year() == [{'year': '2023', 'total': 40.0}]

    #Test 10. Summarize by category - Noah
    assert x1.summarize_by_category() == [{'category': 'catfood', 'total': 40.0}]
    x1.delete_transaction('2')
    x1.delete_transaction('3')
    #print("blah")


if __name__ == "__main__":
    test_transaction()