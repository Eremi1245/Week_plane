#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Подключение к MySql
from configparser import ConfigParser
from functools import wraps
import mysql.connector
from mysql.connector import Error


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
        if func(*args, **kwargs):
            conn.close()
            print('Соединение закрыто.')
            return func(*args, **kwargs)
        else:
            conn.close()
            print('Соединение закрыто.')

    return (wrapper)


@connect
def query_with_fetchall():
    '''Чтение данных'''
    try:
        cursor.execute("SELECT * FROM inter_goal")
        rows = cursor.fetchall()

        '''Что бы выводить данные по одному как в генераторе'''
        # row = cursor.fetchone()
        #
        # while row is not None:
        #     print(row)
        #     row = cursor.fetchone()

        '''Сразу все значения как в списке'''
        print('Total Row(s):', cursor.rowcount)
        for row in rows:
            print(row)

    except Error as e:
        print(e)

@connect
def insert_into_db(**kwargs):
    ''' Вставка значения'''
    query = f"INSERT INTO  VALUES()"
    # cursor.execute(query, args)
    # conn.commit()

@connect
def update_book(**kwargs):
    ''' Обновление данных '''
    query = f"UPDATE {''} SET {''} = %s WHERE {''} = %s"
    # cursor.execute(query, data)
    # conn.commit()

@connect
def delete_book(**kwargs):
    ''' Удаление данных'''
    query = f"DELETE FROM {''} WHERE {''} = %s"
    cursor = conn.cursor()
    # cursor.execute(query, (book_id,))
    # conn.commit()


if __name__ == '__main__':
    query_with_fetchall()
    insert_into_db()
