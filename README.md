# COLLEGE STUDENT MANAGEMENT SYSTEM (CSMS)


The objective of College and Student Management System is to connect daily operations in the college environment ranging from Attendance management to communicational means among students and teachers.  
It facilitates keeping all the information of students such as their id, name, e-mail, date of birth, mark-sheet, subjects, attendance  etc.

It also keeps the record of professors such as their name, id, e-mail, subjects, attendance sheet  etc. They can also record the attendance of the students attending their subjects.


    git clone https://github.com/dhruvgp180901/college-student-management-system.git
    cd Collegemanagement
    
# Getting Started

### Prerequistics
    python==3.8 or up and django==3.1 or up
    
 Create virtual environment

    pip install virtualenv
    virtualenv venv
    
    source venv/bin/activate (for linux)
    ./venv/scripts/activate (for windows)
   
### Installation
    git clone https://github.com/agarwal-megha21/College-and-Student-Management-System.git

### Setup the database<br>
    In the following code replace \<USER> with any Username of your choice.<br>
    In the following code replace \<PASS> with any Password of your choice.

      mysql -u root -p
      create database CMS_database;
      create user '<USER>'@'localhost' identified by '<PASS>';
      grant usage on *.* to '<USER>'@'localhost';
      grant all priveleges on CMS_database.* to '<USER>'@'localhost';

### Setup settings.py<br>
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

   
### Migrate the database<br>

      python3 manage.py makemigrations
      python3 manage.py migrate
      python3 manage.py runserver
