from mongodb_connector import MongoSQLParser

if __name__ == "__main__":
    print("lark sql") 

    # logger.setLevel(logging.DEBUG)
    # p = Lark(GRAMMAR, parser='lalr', debug=True, transformer=SQLTransformer())
    parser = MongoSQLParser.get_instance()

    # select
    # print(p.parse('SELECT hoge,hage FROM hoge WHERE ((hoge > 10)AND(hoge <10)OR(c>10))'))
    # print(p.parse('SELECT hoge,hage FROM hoge WHERE hoge > 10 AND hoge <10 OR x > -10'))
    # print(p.parse('SELECT hoge,hage FROM hoge WHERE hoge  != 20 ORDER BY hoge ASC LIMIT 10'))
    # print(p.parse('SELECT * FROM csv WHERE year!= 20 ORDER BY year ASC LIMIT 10'))
    # parsed = parser.parse('SELECT * FROM csv WHERE year!= 20 ORDER BY year ASC LIMIT 10')


    # # inseret
    # print(p.parse('INSERT INTO hoge (a, b, c) VALUES (1,2,3)'))
    # parsed = parser.parse('INSERT INTO hoge (a, b, c) VALUES (1,2,3)')
 
    # # delete
    # print(p.parse('DELETE FROM hoge WHERE x > 10'))
    # print(parser.parse('DELETE FROM hoge WHERE x > 10'))

    # # update
    # print(parser.parse('UPDATE hoge SET a=19, b=20, c=30 WHERE x > 20'))

    # create table
    # print(parser.parse('CREATE TABLE furit (id INTEGER NOT NULL, name VARCHAR(255), PRIMARY KEY(id))'))
    # print(parser.parse('CREATE TABLE furit (id INTEGER NOT NULL, name VARCHAR(255), PRIMARY KEY(id))'))

    print(parser.parse('SELECT fruit.id AS fruit_id, fruit.name AS fruit_name FROM furit WHERE fruit.id = ? LIMIT ?'))

    


    # drop table
    # print(p.parse('DROP TABLE hoge'
