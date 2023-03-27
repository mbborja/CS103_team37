Pytest Output: 

PS C:\Users\noble\onedrive\documents\python\cs103_team37\pa03> pytest -v
================================================= test session starts =================================================
platform win32 -- Python 3.8.3, pytest-7.2.2, pluggy-1.0.0 -- c:\users\noble\miniconda3\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\noble\onedrive\documents\python\cs103_team37\pa03
collected 1 item

test_transaction.py::test_transaction PASSED                                                                     [100%]

================================================== 1 passed in 0.22s ==================================================





Running program: 

command> 5 0 20 catfood 3/26/2023 Funny
----------------------------------------



command> 4
t=(0, 20.0, 'catfood', '3/26/2023', 'Funny')
[{'item_number': 0, 'amount': 20.0, 'category': 'catfood', 'date': '3/26/2023', 'description': 'Funny'}]
----------------------------------------



command> 7
[{'date': '3/26/2023', 'total': 20.0}]
----------------------------------------



command> 11
usage (enter number):
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
            
----------------------------------------



command> 5 1 20 catfood 3/26/23 Funny
----------------------------------------



command> 4
t=(0, 20.0, 'catfood', '3/26/2023', 'Funny')
t=(1, 20.0, 'catfood', '3/26/23', 'Funny')
[{'item_number': 0, 'amount': 20.0, 'category': 'catfood', 'date': '3/26/2023', 'description': 'Funny'}, {'item_number': 1, 'amount': 20.0, 'category': 'catfood', 'date': '3/26/23', 'description': 'Funny'}]
----------------------------------------



command> 7
[{'date': '3/26/2023', 'total': 20.0}, {'date': '3/26/23', 'total': 20.0}]
----------------------------------------



command> 5 2 20 catfood 3/26/2023 Funny
----------------------------------------



command> 4
t=(0, 20.0, 'catfood', '3/26/2023', 'Funny')
t=(1, 20.0, 'catfood', '3/26/23', 'Funny')
t=(2, 20.0, 'catfood', '3/26/2023', 'Funny')
[{'item_number': 0, 'amount': 20.0, 'category': 'catfood', 'date': '3/26/2023', 'description': 'Funny'}, {'item_number': 1, 'amount': 20.0, 'category': 'catfood', 'date': '3/26/23', 'description': 'Funny'}, {'item_number': 2, 'amount': 20.0, 'category': 'catfood', 'date': '3/26/2023', 'description': 'Funny'}]
----------------------------------------



command> 7
[{'date': '3/26/2023', 'total': 40.0}, {'date': '3/26/23', 'total': 20.0}]
----------------------------------------



command> 8
[{'month': '3/', 'total': 60.0}]
----------------------------------------
