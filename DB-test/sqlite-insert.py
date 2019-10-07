#!/usr/bin/python3

import sqlite3

conn = sqlite3.connect('db.sqlite')

print ("Opened database successfully");

#
#sqlite> select * from users_customuser;
#1|pbkdf2_sha256$150000$kbTJv1gB3kuo$FKjk+SiDUBIUyj/PMkdEOKlnIvhuCnx+LkrttQHwscc=|2019-10-06 12:02:28.186765|1|soa|||code@aurehoej.net|1|1|2019-10-06 11:46:23.293827

# {"model": "users.customuser", "pk": 1, "fields": {"password": "pbkdf2_sha256$150000$kbTJv1gB3kuo$FKjk+SiDUBIUyj/PMkdEOKlnIvhuCnx+LkrttQHwscc=", "last_login": "2019-10-06T19:10:30.987Z", "is_superuser": true, 
# "username": "soa", "first_name": "", "last_name": "", "email": "code@aurehoej.net", "is_staff": true, "is_active": true, "date_joined": "2019-10-06T11:46:23.293Z", "groups": [], "user_permissions": []}},
# {"model": "users.customuser", "pk": 2, "fields": {"password": "pbkdf2_sha256$150000$21mgpQVGrsFZ$bLmbWPremyZ5j6H0EGT/uAUW9S1lvKmfO48DkyrGq3c=", "last_login": "2019-10-06T12:11:13.228Z", "is_superuser": false, "username": "testhest", "first_name": "", "last_name": "", "email": "testhest@aurehoej.net", "is_staff": false, "is_active": true, "date_joined": "2019-10-06T12:10:53.192Z", "groups": [], "user_permissions": []}},

conn.execute("INSERT INTO users.customuser (pk, password,last_login,is_superuser,username,first_name,last_name,email,is_staff,is_active,date_joined,groups,user_permissions,) \
      VALUES (10, 'Marktest','2019-10-06T19:11:30.987Z','false','klytberg','cirkusdk','summarum','cirkus@aurehoej.net','false','true','2019-10-06T19:12:30.987Z','','' )");

conn.commit()
print ("Records created successfully");
conn.close()
print ("Database closed successfully");
