import MySQLdb

class Bill:
    '账单表'
    def __init__(self, name, amount, items):
        self.name = name
        self.amount = amount
        self.items = items

def record_bill(bill):
    db = MySQLdb.connect("47.103.215.97", "root", "voidstar", "void", charset='utf8mb4')
    cursor = db.cursor()
    sql = "INSERT INTO `void`.`bill` (`name`, `amount`, `items`) VALUES ('{}', {}, '{}')".format(bill.name, bill.amount, bill.items)
    
    try:
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        print(e)
        db.rollback()