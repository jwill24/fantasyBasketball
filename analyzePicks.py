import csv
import pandas
import numpy as np
import os, sys

teamSize = 15

fg_ratings=[0.44,0.47,0.51,0.56]
ft_ratings=[0.69,0.74,0.83,0.86]
tres_ratings=[0.3,1.0,2.0,3.4]
pts_ratings=[5.0,10.3,16,27.5]
reb_ratings=[2.5,4.1,6.0,12.0]
ast_ratings=[1.0,1.7,4.5,7.0]
stl_ratings=[0.3,0.7,1.4,1.7]
blk_ratings=[0.2,0.4,1.0,1.5]
to_ratings=[3.4,4.2,4.8,5.6] # 6 - ratings

#----------

def averageCol(col):
    array = []
    for index, row in df.iterrows():
        array.append( float(row[col]) )
    average = round( sum(array) / len(array), 2 )
    return average

#----------

def gradeStat(stat,name):
    if name == fg:
        return findRange(stat,fg_ratings)
    elif name == ft:
        return findRange(stat,ft_ratings)
    elif name == tres:
        return findRange(stat,tres_ratings)
    elif name == pts:
        return findRange(stat,pts_ratings)
    elif name == reb:
        return findRange(stat,reb_ratings)
    elif name == ast:
        return findRange(stat,ast_ratings)
    elif name == stl:
        return findRange(stat,stl_ratings)
    elif name == blk:
        return findRange(stat,blk_ratings)
    elif name == to:
        return findRange(6.0-stat,to_ratings)

#----------
def findRange(stat,array):
    if stat <= array[0]: return 'Not good'
    elif stat > array[0] and stat <= array[1]: return 'Below average'
    elif stat > array[1] and stat <= array[2]: return 'Average'
    elif stat > array[2] and stat <= array[3]: return 'Good'
    elif stat > array[3]: return 'Very good'


#----------

for i in range(teamSize):

    # Get name of draft pick
    print("")
    print("")
    name = input("Enter draft choice: ")

    # Delete the last line
    if name=="delete":
        lines = open('picks.csv', 'r').readlines()
        del lines[-1]
        open('picks.csv', 'w').writelines(lines)
        i = i-1

    elif name=="done":
        sys.exit()

    # Open the drafData to get the info of the player
    else:
        file = csv.reader(open('draftData.csv', "r"), delimiter=",")
        fieldnames = ['NAME', 'FG', 'FT', 'TRES', 'PTS', 'REB', 'AST',
        'STL', 'BLK', 'TO']

        # Get the stats from the corresponding line
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

        # Open the csv file with stored picks
        with open('picks.csv', 'a') as csvfile:
            # Store stats of the drafted player
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({'NAME': name, 'FG': fg, 'FT': ft, 'TRES': tres,
            'PTS': pts, 'REB': reb, 'AST': ast, 'STL': stl, 'BLK': blk,'TO': to})

        # Import the picks file
        df = pandas.read_csv('picks.csv')

        # Get averages of team
        aFG = averageCol(1)
        aFT = averageCol(2)
        aTRES = averageCol(3)
        aPTS = averageCol(4)
        aREB = averageCol(5)
        aAST = averageCol(6)
        aSTL = averageCol(7)
        aBLK = averageCol(8)
        aTO = averageCol(9)

        print("")
        print("")
        print("Roster:")
        for val in df['NAME']:
            print(val)
        print("")

        print("Your new average team stats are:")
        # Build data frame from inputs
        data = [ ['FG%',aFG,gradeStat(aFG,fg)], ['FT%',aFT,gradeStat(aFT,ft)],
        ['3PM',aTRES,gradeStat(aTRES,tres)], ['PTS',aPTS,gradeStat(aPTS,pts)],
        ['REB',aREB,gradeStat(aREB,reb)], ['AST',aAST,gradeStat(aAST,ast)],
        ['STL',aSTL,gradeStat(aSTL,stl)], ['BLK',aBLK,gradeStat(aBLK,blk)],
        ['TO',aTO,gradeStat(aTO,to)] ]

        output = pandas.DataFrame(data, columns = ['Stat', 'Average', 'Grade'])

        print( output.transpose() )
