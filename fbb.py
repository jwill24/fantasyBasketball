import csv


def average_column(file,col):
    list = []
    with open(file, "r") as f:
        reader = csv.DictReader(f, delimiter=",")
        for row in reader:
            list.append(float(row[col]))
    average = sum(list) / (len(list))
    return average


name = raw_input("Enter draft choice: ")

if name=="del":
    lines = file('picks.csv', 'r').readlines() 
    del lines[-1] 
    file('picks.csv', 'w').writelines(lines) 
else:
    file = csv.reader(open('draftData.csv', "rb"), delimiter=",")
    fieldnames = ['NAME', 'FG', 'FT', 'TRES', 'PTS', 'REB', 'AST', 'STL', 'BLK', 'TO']
        
    for row in file:
        if name == row[2]:
            fg = row[7][:4]
            ft = row[8][:4]
            tres = row[9]
            pts = row[10]
            reb = row[11]
            ast = row[12]
            stl = row[13]
            blk = row[14]
            to = row[15]
                

    with open('picks.csv', 'a+r') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        #writer.writeheader()
        writer.writerow({'NAME': name, 'FG': fg, 'FT': ft, 'TRES': tres, 'PTS': pts, 'REB': reb, 'AST': ast, 'STL': stl, 'BLK': blk,'TO': to})

    with open('picks.csv', 'r') as csvfile:
        aFG = average_column('picks.csv','FG')
        aFT = average_column('picks.csv','FT')
        aTRES = average_column('picks.csv','TRES')
        aPTS = average_column('picks.csv','PTS')
        aREB = average_column('picks.csv','REB')
        aAST = average_column('picks.csv','AST')
        aSTL = average_column('picks.csv','STL')
        aBLK = average_column('picks.csv','BLK')
        aTO = average_column('picks.csv','TO')


    print "Your new average team stats are:"
    print " FG% ", "  FT% ", "  3PM ", "  PTS ", "  REB ", "  AST ", "  STL ", " BLK ", "  TO "
    print round(aFG,2), " ",round(aFT,2)," ", round(aTRES,2)," ", round(aPTS,2)," ", round(aREB,2)," ", round(aAST,2)," ", round(aSTL,2)," ", round(aBLK,2)," ", round(aTO,2) 





