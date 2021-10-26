# this program will create the database class

from tkinter import *

from PIL import ImageTk,Image
#sqlite is built in Python

import sqlite3

class Database:
    def __init__(self,db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute(
                        '''CREATE TABLE IF NOT EXISTS Jobs_Database 
                        (id INTEGER PRIMARY KEY, 
                        jobID integer, 
                        position text, 
                        company text, 
                        location text,
                        experience text,
                        salary integer)''')
        self.conn.commit()

    def fetch(self):
        self.cur.execute('SELECT * FROM Jobs_Database')
        rows = self.cur.fetchall()
        return rows

    def insert(self, jobID, position, company, location, experience, salary):
        self.cur.execute("INSERT INTO Jobs_Database VALUES (NULL, ?, ?, ?, ?, ?, ?)", 
                        (jobID, position, company, location, experience, salary))
        self.conn.commit()

    def remove(self, jobID):
        self.cur.execute("DELETE FROM Jobs_Database WHERE jobID=?", (jobID,))
        self.conn.commit()

    def update(self, jobID, position, company, location, experience, salary):
        self.cur.execute('''UPDATE Jobs_Database 
                                    SET position = ?, 
                                    company = ?,
                                    location = ?, 
                                    experience = ?,  
                                    salary = ? 
                                    WHERE jobID = ? ''', 
                        (position, company, location, experience, salary, jobID))
        self.conn.commit()

    def __del__(self):
        self.conn.close()


# Create database and insert data into it
# comment the lines after testing
#path = '/Users/dannylam/Documents/School/CISP71 - Python/PROJECT/Online_Jobs_Database/'
#db = Database(path+'Jobs.db')
#db.insert(1,'Software Developer','Apple','Cupertino, CA','Senior',95000)
#db.insert(2,'Director of Marketing','Amazon','Seattle, WA','Executive',90000)
#db.insert(3,'UX Designer','Netflix','Los Gatos, CA','Associate',70000)
#db.insert(4,'Marketing Intern','Nike','Portland, OR','Internship',20000)
#db.insert(5,'Accountant','Disney','Burbank, CA','Entry level',45000)
#db.insert(6,'Regional Manager','Dunder Mifflin','Scranton, PA','Executive',200000)
#db.insert(7,'Product Manager','Facebook','Menlo Park, CA','Senior',150000)
#db.insert(8,'Customer Service Rep','Motion Industries','Anahiem, CA','Entry level',40000)
#db.insert(9,'Account Manager','T-Mobile','New York, NY','Associate',60000)
#db.insert(10,'Business Analyst','Franciscan Health','Greenwood, IN','Entry level',56000)
#db.insert(11,'DevOps Architect','Robert Half','Santa Monica, CA','Senior',75000)
#db.insert(12,'IT Security Analyst','Dietrich Partners','Denver, CO','Entry level',49000)

