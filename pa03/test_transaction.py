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


    # x1 = Interval(0.9,1.1)
    # x2 = Interval(1.999,2.001)
    # x3 = Interval(-1,1)
    # x4 = Interval(10,10)
    # assert f'x1= {x1}' == "x1= [0.9,1.1]"
    # assert f'x2= {x2}' == "x2= [1.999,2.001]"
    # assert f'x3= {x3}' == "x3= [-1,1]"
    # assert f'x4= {x4}' == "x4= [10,10]"
    # assert f'x1+x2= {x1 + x2}' == "x1+x2= [2.899,3.101]"
    # assert f'x2*x3= {x2 * x3}' == "x2*x3= [-2.001,2.001]"
    # assert f'x3/x4= {x3 / x4}' == "x3/x4= [-0.1,0.1]"
    # assert f'x4-x1*x2/(x4+x3)-(x1+x2) {x4-x1*x2/(x4+x3)-(x1+x2)}' == "x4-x1*x2/(x4+x3)-(x1+x2) [6.6544333333333325,6.937445454545455]"
    # assert f'x1.union(x2)= {x1.union(x2)}' == "x1.union(x2)= [0.9,2.001]"
    # assert f'x1.intersect(x3)={x1.intersect(x3)}' == "x1.intersect(x3)=[0.9,1]"
    # assert f'x3.intersect(x1)={x3.intersect(x1)}' == "x3.intersect(x1)=[0.9,1]"
    # assert f'x1.intersects(x3)={x1.intersects(x3)}' == "x1.intersects(x3)=True"
    # assert f'x1.intersects(x2)={x1.intersects(x2)}' == "x1.intersects(x2)=False"
    # with pytest.raises(Exception, match="Two Intervals not intersecting") as exc_info:
    #     x1.intersect(x4)
    # x5 = Interval(0,10)
    # with pytest.raises(Exception, match="internal division by zero") as exc_info:
    #     x1/x5
    # with pytest.raises(Exception, match="empty interval") as exc_info:
    #     Interval(0,-0.1)