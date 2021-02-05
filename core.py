#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Подключение к MySql
from configparser import ConfigParser
from functools import wraps
import mysql.connector
from mysql.connector import Error
from UI import *
from calendar import Calendar as cal
# from datetime import date as dt
from datetime import datetime as dt
def read_db_config(filename='db_config.ini', section='mysql'):
    """ Читает конфигурацию Базы данных и возвращает словарь с параметрами
    :param filename: имя конфига
    :param section: секция с данными базы данных
    :return: словарь с параментрами
    """
    parser = ConfigParser()
    parser.read(filename)

    db = {}
    if parser.has_section(section):
        items = parser.items(section)
        for item in items:
            db[item[0]] = item[1]
    else:
        raise Exception('{0} not found in the {1} file'.format(section, filename))

    return db


def connect(func):
    """Подключение в БД """
    @wraps(func)
    def wrapper(*args, **kwargs):
        db_config = read_db_config()

        try:
            print('Соединение с MySQL базой...')
            global conn
            conn = mysql.connector.connect(**db_config)
            global cursor
            cursor = conn.cursor()
            if conn.is_connected():
                print('соединение установлено.')
            else:
                print('соединения нет!!!.')

        except Error as error:
            print(error)
        func_result=func(*args, **kwargs)
        if func_result:
            conn.close()
            print('Соединение закрыто.')
            return func_result
        else:
            conn.close()
            print('Соединение закрыто.')

    return (wrapper)


# Чтение данных
@connect
def query_with_fetchall(table=str,columns=''):
    '''Чтение данных'''
    try:
        if columns=='':
            cursor.execute(f"SELECT * FROM {table};")
        else:
            cursor.execute(f"SELECT {columns} FROM {table};")
        rows = cursor.fetchall()
        # print(rows)
        return rows
        '''Что бы выводить данные по одному как в генераторе'''
        # row = cursor.fetchone()
        # while row is not None:
        #     print(row)
        #     row = cursor.fetchone()
        '''Сразу все значения как в списке'''
        # print('Total Row(s):', cursor.rowcount)
        # for row in rows:
        #     print(row)

    except Error as e:
        print(e)

# Вставка значения
@connect
def insert_into_db(table=str,columns='',values=dict):
    ''' Вставка значения'''
    value_str=''
    for i in list(values.keys())[0:-1]:
    	value_str=value_str+str(values[i])+','+'\n'
    value_str=value_str+str(values[list(values.keys())[-1]])+';'
    if columns=='':
    	query = f"INSERT INTO {table} VALUES {value_str}"
    else:
    	query = f"INSERT INTO {table}({columns}) VALUES {value_str}"
    print(query)
    cursor.execute(query)
    conn.commit()

# Обновление данных
@connect
def update_db(**kwargs):
    ''' Обновление данных '''
    query = f"UPDATE {''} SET {''} = %s WHERE {''} = %s"
    # cursor.execute(query, data)
    # conn.commit()

# Удаление данных
@connect
def delete_db(**kwargs):
    ''' Удаление данных'''
    query = f"DELETE FROM {''} WHERE {''} = %s"
    cursor = conn.cursor()
    # cursor.execute(query, (book_id,))
    # conn.commit()

def dowload_timetable():
	month=[x for x in cal().itermonthdates(2021, 2)]
	for i in range(0,len(month)+1,8):
		month.insert(i,'x')
	date_from_base=dict(query_with_fetchall('inter_date'))
	dates=list(date_from_base.keys())
	for i in month:
		if i == 'x':
			continue
		elif i in dates and i != 'x':
			month[month.index(i)]=str(i)+'\n'*3+date_from_base[i]
		else:
			month[month.index(i)]=str(i)+'\n'*3+'Свободный день'
	return month


def dowload_interesttable():
	template=''
	query=query_with_fetchall('inter_goal')
	interests={x[0] for x in query}
	count_inter=0
	for i in interests:
		count_inter+=1
		count_goal=0
		template+=f'\n{count_inter}) Интерес: {i}\nЦели:\n'
		for m in query:
			if i == m[0]:
				count_goal+=1
				template+=f'{count_goal}) {m[1]} - {m[2]}\n'

	return(template)



if __name__ == '__main__':
    #query_with_fetchall('inter_date')
    dowload_timetable()
    #insert_into_db()
    #вызов UI
    app = QApplication(sys.argv)
    ex = Example(dowload_timetable(),dowload_interesttable())
    sys.exit(app.exec_())





