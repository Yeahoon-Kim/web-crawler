import os.path
def main():
    if os.path.exists('./Daily_News.xlsx'):
        pass
    else:
        import xlsxwriter
        workbook = xlsxwriter.Workbook("Daily_News.xlsx")
        worksheet = workbook.add_worksheet()
        title = workbook.add_format({'bold': True})
        title.set_font_size(20)
        worksheet.write('D1', 'Daily Newsletter', title)

        template = ['공유일','공유요일','순서','분류','보도사','보도출처','보도날짜','헤드라인','URL']
        temp_format = workbook.add_format({'bg_color': '#C6EFCE','bold':True})

        for idx, data in enumerate(template):
            worksheet.write(2,idx,data,temp_format)

        worksheet.autofilter(2, 0, 2, len(template)-1)

        workbook.close()

if __name__ == "__main__":
    main()