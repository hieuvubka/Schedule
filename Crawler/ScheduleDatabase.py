import pyodbc
from Crawler.ScheduleCrawler import ScheduleCrawler

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
            self.InsertData()

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
                                        PRIMARY KEY (MaSV, ThoiGian, MaLop ))""")
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
        a = ScheduleCrawler(self.studenCode)
        cursor = self.conn.cursor()
        for i in range(a.classCount):
            cursor.execute("""INSERT INTO Schedule.dbo.Schedule
                                (MaSV, 
                                ThoiGian,
                                Tuan,
                                Phong,
                                MaLop,
                                LoaiLop,
                                Nhom,
                                MaHP,
                                TenLop,
                                GhiChu)
                            VALUES 
                                ('{maSV}',
                                N'{ThoiGian}',
                                '{Tuan}',
                                '{Phong}',
                                '{MaLop}',
                                N'{LoaiLop}',
                                N'{Nhom}',
                                '{MaHP}',
                                N'{TenLop}',
                                N'{GhiChu}')"""
                           .format(maSV= a.student_code,
                                   ThoiGian= a.time[i],
                                   Tuan= a.week[i],
                                   Phong= a.room[i],
                                   MaLop= a.classId[i],
                                   LoaiLop= a.classType[i],
                                   Nhom= a.group[i],
                                   MaHP= a.subjectId[i],
                                   TenLop= a.className[i],
                                   GhiChu= a.note[i]))
        cursor.commit()

InsertToDatabase(20183916)




