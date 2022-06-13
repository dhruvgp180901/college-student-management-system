# COLLEGE STUDENT MANAGEMENT SYSTEM (CSMS)


The objective of College and Student Management System is to connect daily operations in the college environment ranging from Attendance management to communicational means among students and teachers.  
CSMS facilitates keeping all the information of students such as their id, name, e-mail, date of birth, mark-sheet, subjects, leave requests, leave records, attendance  etc.

    git clone https://github.com/agarwal-megha21/Collegemanagement.git
    cd Collegemanagement
    
 Create virtual environment

    pip install virtualenv
    virtualenv venv
    
    source venv/bin/activate (for linux)
    ./venv/scripts/activate (for windows)
   
   Install Packages
   

    pip install -r requirements.txt

Setup the database<br>
In the following code replace \<USER> with any Username of your choice.<br>
In the following code replace \<PASS> with any Password of your choice.

    mysql -u root -p
    create database CMS_database;
    create user '<USER>'@'localhost' identified by '<PASS>';
    grant usage on *.* to '<USER>'@'localhost';
    grant all priveleges on CMS_database.* to '<USER>'@'localhost';

Setup settings.py<br>
In the following code replace \<USER> with the Username you created above.<br>
In the following code replace \<PASS> with the Password you created above.<br>
Replace the following code in settings.py : 

    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME' : 'CMS_database',
        'USER' : '<USER>',
        'PASSWORD' : '<PASS>',
        'HOST' : 'localhost',
        'OPTIONS': {
                'init_command': 'SET default_storage_engine=INNODB',
                }
        }
    }

   
   Migrate the database<br>
  (If python3 does not work, use python instead of python3)

    python3 manage.py makemigrations
    python3 manage.py migrate
    python3 manage.py runserver
