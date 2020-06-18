import pyodbc

class InsertToDatabase():
    def __init__(self, studentCode):
        self.studenCode = studentCode
        self.conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=DESKTOP-4K1SNB5\SQL;'
                              'Database=Schedule;'
                              'Trusted_Connection=yes;')

        if self.CheckTable('Schedule') == True:
            pass
        else:
            self.CreateTable('Schedule')

        if self.CheckData() == True:
            pass
        else:
            self.In


    def CheckTable(self, tableName):
        dbcur = self.conn.cursor()
        dbcur.execute("""
                SELECT COUNT(*)
                FROM information_schema.tables
                WHERE table_name = '{0}'
                """.format(tableName))
        if dbcur.fetchone()[0] == 1:
            dbcur.close()
            return True

        dbcur.close()
        return False

    def CreateTable(self, tableName):
        cursor = self.conn.cursor()
        cursor.execute("""CREATE TABLE Schedule(
                                        MaSV CHAR(10),
                                        ThoiGian nVARCHAR(30),
                                        Tuan VARCHAR(30),
                                        Phong CHAR(10),
                                        MaLop CHAR(10),
                                        LoaiLop nVARCHAR(20),
                                        Nhom nVARCHAR(10),
                                        MaHP Char(10),
                                        TenLop nVARCHAR(50),
                                        GhiChu nVARCHAR(50),
                                        PRIMARY KEY (MaSV))""")
        cursor.commit()

    def CheckData(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM Schedule WHERE MaSV = {}'.format(self.studenCode))
        count = 0
        for row in cursor:
            print(row)
            count += 1

        if count > 0:
            return True
        else:
            return False

    def InsertData(self):
        cursor = self.conn.cursor()


a = InsertToDatabase(20183916)


