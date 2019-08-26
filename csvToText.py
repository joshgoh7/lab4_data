import csv
f= open("amazon_baby_rating.txt","w+")
with open('amazon_baby.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            if int(row[2]) >= 3:
                f.write(f'positive\n    ')
            else:
                f.write(f'negative\n')
            line_count += 1
    print(f'Processed {line_count} lines.')