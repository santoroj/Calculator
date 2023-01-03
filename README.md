# Calculator

## Setup virtual environment
 python -m venv calculator 
 . calculator/bin/activate

Install:
pip install flake8 pytest pytest-cov 

pip freeze > requirements.txt
cat requirements.txt

### Check if anything is wrong
flake8 --statistics

### To test the code
pytest  -v --cov .