How to clear database/make new db:

first activate the virtual env:
source env/bin/activate

cd into django dir:
cd nerds

backup old database:
cp nerds.db nerds.db.YEAR

create new database:
python manage.py syncdb

set up superuser account (prompted by manage.py)

deactive virtualenv:
deactivate

end ssh session:
exit
