call python -m venv env
call env/Scripts/activate
call pip install -r requirements.txt
call echo call .\env\Scripts\activate > activate.bat
call echo call python xlsx_to_db_converter.py >> activate.bat

