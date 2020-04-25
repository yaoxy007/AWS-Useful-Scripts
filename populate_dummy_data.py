import psycopg2
import sys

def parse_args(args):
    global config
    i = 1
    while i<len(args):
        arg=args[i]
        if arg=="-h" and i+1 < len(args):
            config['HostName'] = args[i+1]
            i += 1
        elif arg=="-U" and i+1 < len(args):
            config['UserName'] = args[i+1]
            i += 1
        elif arg=="-d" and i+1 < len(args):
            config['DatabaseName'] = args[i+1]
            i += 1
        elif arg=="-p" and i+1 < len(args):
            config['Port'] = args[i+1]
            i += 1
        if arg=="-W" and i+1 < len(args):
            config['Password'] = args[i+1]
            i += 1
        if arg=="-D" and i+1 < len(args):
            config['DataSize'] = args[i+1]
            i += 1
        else:
            print("Error: Invalid command line argument"+arg)
            return False
        i+=1
    return True

def pop_data():
    global config
    if {'HostName','UserName','DatabaseName','Password','DataSize'}.issubset(config):
        hostName = config['HostName']
        usrName = config['UserName']
        dbName = config['DatabaseName']
        pswd = config['Password']
        data = config['DataSize']
    else:
        print("Error: Values for the required field not specified")
        return
    try:
        connection = psycopg2.connect(host=hostName,user=usrName,password=pswd,dbname=dbName)
    except(Exception,psycopg2.DatabaseError) as error:
        print(error)
    cursor = connection.cursor()

    create_table = 'CREATE TABLE IF NOT EXISTS pop_data AS \
        SELECT s, md5(random()::text) AS col1, \
            md5(random()::text) AS col2, \
                md5(random()::text) AS col3 \
                    FROM generate_series(1,1000) s;'
    
    insert_data='INSERT INTO pop_data VALUES(generate_series(1,10000),md5(random()::text),md5(random()::text),md5(random()::test));'

    cursor.execute(create_table)
    connection.commit()
    size=0

    while size<=int(data):
        cursor.execute(insert_data)
        connection.commit()
        cursor.execute('SELECT pg_database_size(\'%s\');'% dbName)
        size=cursor.fetchone()
        print(size[0]/1024/1024," MB data inserted")
        size = int(size[0])
        size = size/1024/1024

    cursor.close()
    connection.close

config={}

if(parse_args(sys.argv)):
    pop_data()