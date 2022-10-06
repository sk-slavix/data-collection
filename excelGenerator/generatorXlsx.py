import xlsxwriter


class XlsxGenerator:
    

    data = [
        {
            'name': "Martin Stinger"
        }
    ]

    def generateFile(self):
        workbook = xlsxwriter.Workbook("DataCollection.xlsx")
        worksheet = workbook.add_worksheet("basicSheet")
        worksheet.write(0, 0, "#")
        worksheet.write(0, 1, "Name")
        worksheet.write(0, 2, "Phone")
        worksheet.write(0, 3, "Price")

        workbook.close()
        
# # import xlsxwriter module 
# import xlsxwriter 
  
# workbook = xlsxwriter.Workbook('sample.xlsx') 
# worksheet = workbook.add_worksheet() 
  
# # Start from the first cell. 
# # Rows and columns are zero indexed. 
# row = 0
# column = 0
  
# content = ["Welcome", "to", "Geeks", "for", "Geeks"] 
  
# # iterating through content list 
# for item in content : 
  
#     # write operation perform 
#     worksheet.write(row, column, item) 
  
#     # incrementing the value of row by one 
#     # with each iterations. 
#     row += 1
  
# workbook.close()
