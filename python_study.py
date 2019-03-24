# csvファイルの作成
import csv

drinks = [['tea',500],['coffee',600],['juice',800]]

with open('drinks.csv', 'w', encoding='shift_jis') as f:
    writer = csv.writer(f,lineterminator='\n')
    writer.writerows(drinks)

# csvファイルの読み込み

with open('drinks.csv', 'r', encoding='shift_jis') as f:
    reader = csv.reader(f)

    for row in reader:
        print(row)