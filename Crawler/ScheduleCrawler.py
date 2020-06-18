
import requests
import bs4


class ScheduleCrawler():
    classCount = 0
    time = []
    week = []
    room = []
    classId = []
    classType = []
    group = []
    subjectId = []
    className = []
    note = []
    def __init__(self, student_code):
        self.student_code = student_code
        self.url = "http://sis.hust.edu.vn/ModulePlans/Timetables.aspx"
        self.form = {
        '__EVENTTARGET':'',
        'ctl00$MainContent$Studentid': '{}'.format(self.student_code),
        'ctl00$MainContent$btFind':''
        }
        soup = self.get_schedule()
        table = soup.find('table', id='MainContent_gvStudentRegister_DXMainTable')
        rows = table.findAll('tr', class_='dxgvDataRow_SisTheme')
        for row in rows:
            self.classCount += 1
            elements = row.findAll('td')
            self.time.append(elements[0].text)
            self.week.append(elements[1].text)
            self.room.append(elements[2].text)
            self.classId.append(elements[3].text)
            self.classType.append(elements[4].text)
            self.group.append(elements[5].text)
            self.subjectId.append(elements[6].text)
            self.className.append(elements[7].text)
            self.note.append(elements[8].text)
    def get_schedule(self):
        page = requests.post(self.url, data=self.form)
        if page.status_code == 200:
            # doc = lh.fromstring(page.text)
            # table_elements = doc.xpath('//table[@id="MainContent_gvStudentRegister_DXMainTable"]')[0]
            # td_elements = table_elements.xpath('.//tr[@class="dxgvDataRow_SisTheme"]')
            return bs4.BeautifulSoup(page.text, "html.parser")




