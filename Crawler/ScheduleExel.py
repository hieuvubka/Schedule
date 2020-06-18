
from Crawler.ScheduleCrawler import ScheduleCrawler
from openpyxl import load_workbook

class ScheduleExelTable():
    def __init__(self, studentCode):
        schedule = ScheduleCrawler(studentCode)

        self.fileName = 'ScheduleTable.xlsx'
        self.wb = load_workbook(self.fileName)

        if('%d' %(studentCode) in self.wb.sheetnames):
            pass
        else:
            sheet = self.wb.create_sheet("%d" % (studentCode))
            sheet['A1'] = 'Mã SV'
            sheet['B1'] = 'Thời gian'
            sheet['C1'] = 'Tuần học'
            sheet['D1'] = 'Phòng học'
            sheet['E1'] = 'Mã lớp'
            sheet['F1'] = 'Loại lớp'
            sheet['G1'] = 'Nhóm'
            sheet['H1'] = 'Mã HP'
            sheet['I1'] = 'Tên lớp'
            sheet['J1'] = 'Ghi chú'

            for i in range(0, schedule.classCount):
                sheet['A%d' % (i + 2)] = schedule.student_code
                sheet['B%d' % (i + 2)] = schedule.time[i]
                sheet['C%d' % (i + 2)] = schedule.week[i]
                sheet['D%d' % (i + 2)] = schedule.room[i]
                sheet['E%d' % (i + 2)] = schedule.classId[i]
                sheet['F%d' % (i + 2)] = schedule.classType[i]
                sheet['G%d' % (i + 2)] = schedule.group[i]
                sheet['H%d' % (i + 2)] = schedule.subjectId[i]
                sheet['I%d' % (i + 2)] = schedule.className[i]
                sheet['J%d' % (i + 2)] = schedule.note[i]

        self.wb.save(self.fileName)
    # def writeSchedule(self, studentCode):
    #     schedule = ScheduleCrawler(studentCode)
    #     self.wb = Workbook()
    #     sheet = self.wb.create_sheet("%d" %(studentCode))
    #     sheet['A1'] = 'Mã SV'
    #     sheet['B1'] = 'Thời gian'
    #     sheet['C1'] = 'Tuần học'
    #     sheet['D1'] = 'Phòng học'
    #     sheet['E1'] = 'Mã lớp'
    #     sheet['F1'] = 'Loại lớp'
    #     sheet['G1'] = 'Nhóm'
    #     sheet['H1'] = 'Mã HP'
    #     sheet['I1'] = 'Tên lớp'
    #     sheet['J1'] = 'Ghi chú'


        # sheet.write('A1','Mã SV')
        # sheet.write('B1','Thời gian')
        # sheet.write('C1', 'Tuần học')
        # sheet.write('D1', 'Phòng học')
        # sheet.write('E1', 'Mã lớp')
        # sheet.write('F1', 'Loại lớp')
        # sheet.write('G1', 'Nhóm')
        # sheet.write('H1', 'Mã HP')
        # sheet.write('I1', 'Tên lớp')
        # sheet.write('J1', 'Ghi chú')

        # for i in range(0, schedule.classCount):
        #     sheet['A%d' %(i+2)] = schedule.student_code
        #     sheet['B%d' %(i+2)] = schedule.time[i]
        #     sheet['C%d' %(i+2)] = schedule.week[i]
        #     sheet['D%d' %(i+2)] = schedule.room[i]
        #     sheet['E%d' %(i+2)] = schedule.classId[i]
        #     sheet['F%d' %(i+2)] = schedule.classType[i]
        #     sheet['G%d' %(i+2)] = schedule.group[i]
        #     sheet['H%d' %(i+2)] = schedule.subjectId[i]
        #     sheet['I%d' %(i+2)] = schedule.className[i]
        #     sheet['J%d' %(i+2)] = schedule.note[i]
        #
        # self.wb.save(filename= 'ScheduleTable.xlsx')


b = ScheduleExelTable(20183915)





