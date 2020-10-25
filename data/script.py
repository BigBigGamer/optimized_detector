import xlrd

excel_files = ["data/data_" + name + ".xlsx" for name in ["determ",
                                                          #   "phase",
                                                          #   "amplitude",
                                                          "phase_amplitude"]]

# Значения СКО по листам
sheets_dict = {"0": 0.25, "1": 0.5, "2": 1.0, "3": 1.5, "4": 0.01}
# Порог
ceiling = [0.5, 1, 3.0, 5.0, 7.0, 10.0, 15.0, 20.0, 23.0, 25.0, 27.0, 30.0]

for excel_file in excel_files:
    wb = xlrd.open_workbook(excel_file)
    for sh_ind in sheets_dict.keys():
        current_sko = sheets_dict[sh_ind]
        sh_ind = int(sh_ind)
        sheet = wb.sheet_by_index(sh_ind)

        signal2noise = sheet.col_values(1)[1:]  # dB
        correct_prob = sheet.col_values(2)[1:]
        incorrect_prob = sheet.col_values(3)[1:]
        
        print("СКО:", current_sko)
        print("С/Ш:", signal2noise)
        print("P по:", correct_prob)
        print("P лт:", incorrect_prob)
    # for rownum in range(sheet.nrows):
        # row = sheet.row_values(rownum)
        # print(row)
