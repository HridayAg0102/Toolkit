call python -m venv env
call env/Scripts/activate
call pip install -r requirements.txt
call echo env/Scripts/activate > activate.bat
call echo python xlsx_to_db_converter.py >> activate.bat
