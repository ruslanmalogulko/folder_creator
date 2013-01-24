#!/usr/bin/python

import os
import sys
import stat
import MySQLdb
import config
import logging
import datetime

sys.path.append(os.getcwd()) #for config dir definition

logging.basicConfig(filename="testlog.log", 
                    format='%(levelname)s:%(message)s', level=logging.DEBUG)
logging.info('-'*50)
logging.info(datetime.datetime.now())
logging.info('-'*50)
logging.info("---Start logging---")


def read_from_database(sql, db):
	# creating cursor
	cursor = db.cursor()
	pathset = [] # path set from database
 	try:
		cursor.execute(sql)
		results = cursor.fetchall()
		logging.debug("Input file path, extracted fom database: ")
		write_to_database(db1, "Input file path, extracted fom database: ")
		for row in results:
			inpfilepath = row[0]
			pathset.append(row[0])
			logging.debug(inpfilepath)
		return pathset;
    except:
		logging.warning("Unable to fetch data ")
		write_to_database(db1, "Unable to fetch data ")
 
 
def write_to_database(db1, text):
	cursor = db1.cursor()
	sql_ins="INSERT INTO rusdb(name) VALUES ('%s')" % str(text)
	print sql_ins
	try:
		cursor.execute(sql_ins)
		print('String was added to database')
		db1.commit()
	except OSError:
		db1.rollback()
		logging.warning("Unable to write data")
		write_to_database(db1, "Unable to write data")
  
  
def dirs_create(pathset):
	for path in pathset:
		try:
			print("Path: %s \n" %path)
			os.makedirs( path )
		except OSError:
			if os.path.exists(path):
				logging.warning("Dir %s exists! " %path)
				write_to_database(db1, "Dir %s exists! " %path)
				pass
			else:
				logging.warning("Unable to create dir %s" %path)
				write_to_database(db1, "Unable to create dir %s" %path)
				pass
	
	
def permissions_change(pathset, permission):
	for path in pathset:
		try:
			# logging.info("Changing permissions for dir %s" %path)
			print( "Chmod path: %s" %path )
			print(permission)
			# os.chmod( path, permission ) #permission taked from config file
		except:
			logging.warning("Unable to change permissions to %s for dir: %s" %
			                (permission, path))
			write_to_database(db1, "Unable to create dir %s" %path)


# Opens database connection for reading
print(config.host, config.passwd, config.user, config.database)
db = MySQLdb.connect(host=config.host, passwd=config.passwd, 
                     user=config.user, db=config.database)
db1 = MySQLdb.connect(host="localhost", user="russel", 
                      passwd="russel", db="test")
sql = "SELECT " + config.column + " FROM dict_source"

# Reads 'inputfilepath' from table in database
pathset = read_from_database(sql, db)
print(pathset)

# Try to create dirs
dirs_create(pathset)

# Try to change permissions for dirs
permissions_change(pathset, config.perm)

db.close()
db1.close()

logging.info("---End logging at %s---\n" %datetime.datetime.now())


