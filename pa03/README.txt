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

Pylint Output:

For transaction.py
************* Module transaction
transaction.py:15:0: C0301: Line too long (103/100) (line-too-long)
transaction.py:31:0: C0303: Trailing whitespace (trailing-whitespace)
transaction.py:53:0: C0301: Line too long (200/100) (line-too-long)
transaction.py:66:0: C0301: Line too long (108/100) (line-too-long)
transaction.py:67:0: C0301: Line too long (111/100) (line-too-long)
transaction.py:71:0: C0303: Trailing whitespace (trailing-whitespace)
transaction.py:72:38: C0303: Trailing whitespace (trailing-whitespace)
transaction.py:73:0: C0301: Line too long (110/100) (line-too-long)
transaction.py:77:0: C0303: Trailing whitespace (trailing-whitespace)
transaction.py:83:0: C0303: Trailing whitespace (trailing-whitespace)
transaction.py:85:0: C0303: Trailing whitespace (trailing-whitespace)
transaction.py:12:0: C0103: Function name "toDict" doesn't conform to snake_case naming style (invalid-name)
transaction.py:12:11: C0103: Argument name "t" doesn't conform to snake_case naming style (invalid-name)
transaction.py:18:0: C0115: Missing class docstring (missing-class-docstring)
transaction.py:32:4: C0116: Missing function or method docstring (missing-function-docstring)
transaction.py:38:4: C0116: Missing function or method docstring (missing-function-docstring)
transaction.py:42:4: C0116: Missing function or method docstring (missing-function-docstring)
transaction.py:46:4: C0116: Missing function or method docstring (missing-function-docstring)
transaction.py:52:4: C0116: Missing function or method docstring (missing-function-docstring)
transaction.py:56:4: C0116: Missing function or method docstring (missing-function-docstring)
transaction.py:60:4: C0116: Missing function or method docstring (missing-function-docstring)
transaction.py:63:8: W0622: Redefining built-in 'sum' (redefined-builtin)
transaction.py:66:4: C0116: Missing function or method docstring (missing-function-docstring)
transaction.py:69:8: W0622: Redefining built-in 'sum' (redefined-builtin)
transaction.py:72:4: C0116: Missing function or method docstring (missing-function-docstring)
transaction.py:75:8: W0622: Redefining built-in 'sum' (redefined-builtin)
transaction.py:78:4: C0116: Missing function or method docstring (missing-function-docstring)
transaction.py:81:8: W0622: Redefining built-in 'sum' (redefined-builtin)
transaction.py:10:0: W0611: Unused import os (unused-import)

-----------------------------------
Your code has been rated at 4.63/10

________________________________________
For test_transaction.py
************* Module test_transaction
test_transaction.py:11:0: C0303: Trailing whitespace (trailing-whitespace)
test_transaction.py:15:0: C0301: Line too long (104/100) (line-too-long)
test_transaction.py:16:0: C0301: Line too long (104/100) (line-too-long)
test_transaction.py:17:0: C0301: Line too long (103/100) (line-too-long)
test_transaction.py:33:0: C0301: Line too long (237/100) (line-too-long)
test_transaction.py:34:0: C0303: Trailing whitespace (trailing-whitespace)
test_transaction.py:37:0: C0301: Line too long (137/100) (line-too-long)
test_transaction.py:63:0: C0304: Final newline missing (missing-final-newline)
test_transaction.py:1:0: C0114: Missing module docstring (missing-module-docstring)
test_transaction.py:4:0: C0116: Missing function or method docstring (missing-function-docstring)
test_transaction.py:5:4: C0103: Variable name "x1" doesn't conform to snake_case naming style (invalid-name)
test_transaction.py:1:0: W0611: Unused import pytest (unused-import)

-----------------------------------
Your code has been rated at 6.00/10