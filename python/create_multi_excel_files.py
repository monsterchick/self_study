import xlwings as xw


app = xw.App(visible=True, add_book=False)

dept_list = ['Administration/operations↳','Research and development',\
             'Marketing and sales','Human resources','Customer service',\
             'Accounting and finance']
for dept in dept_list:
    workbook = app.books.add()
    workbook.save("report-{department}.xlsx".format(department=dept))