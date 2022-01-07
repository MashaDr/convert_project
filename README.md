# convert_project

Convert a non-negative integer num to its English words representation.

### For example:
- Input: number = 1354789
- Result: One Million Three Hundred Fifty Four Thousand Seven Hundred Eighty Nine

###
- [How to use](#how-to-use)
- [Running the tests](#running-the-tests)
---
### How to use
- It is recommended to create a new virtual environment for the project as to not interfere with the system installation of python. `python3 -m venv name_of_virtual_env` 
- Activate the new virtual environment
    > linux `. path/to/virtual/env/bin/activate` 
- Install the python libraries `pip install -r requirements.txt`
- Run web server `python manage.py runserver`
  ```bash
  curl -X POST http://127.0.0.1:8000/num_to_english  \
       -H 'Content-Type: application/json' \
       -d '{"number":"12345"}'
  ```
  
  ```bash
  curl -X GET http://127.0.0.1:8000/num_to_english?number=1234
  ```
  
  ```bash
  python api/Num2Words.py
  ```
---
### Running the tests

- Tests can be run by simply executing `pytest`

 ```bash
  python -m pytest tests/test_num2words.py  -v
 ```


