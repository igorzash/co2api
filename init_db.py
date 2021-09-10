import sqlite3
import csv


def main():
    con = sqlite3.connect('co2.db')
    
    with open('./db/reset.sql') as reset_file:
        con.executescript(reset_file.read())

    with open('./db/schema.sql') as schema_file:
        con.executescript(schema_file.read())
    
    with open('./db/co2.csv', newline='', encoding="utf-8") as dataset_file:
        csvreader = csv.reader(dataset_file, delimiter=',')

        rows = list(csvreader)

    header = rows.pop(0)
    
    con.execute('insert into data_types (name, units) values (?, ?)',
        ('CO2', header[-2].split(', ')[1]));
    con.execute('insert into data_types (name, units) values (?, ?)',
        ('trees', header[-1].split(', ')[1]));

    regions = {row[2] for row in rows}

    for region_name in regions:
        con.execute('insert into regions (name) values (?)', (region_name,))

    con.commit()
    cur = con.cursor()

    rows.sort(key=lambda row: ''.join(row)) 
    
    for row in rows:
        year, month, region_name, co2_output, trees_num = row

        for row in cur.execute('select id, name from regions where name=?', (region_name,)):
            region_id = int(row[0])
            break

        con.execute('insert into reports'
                    '(year, month, region_id, co2_output, trees_num)'
                    'values (?, ?, ?, ?, ?)',
                    (year, month, region_id, co2_output, trees_num))

    con.commit() 
    con.close()

if __name__ == '__main__':
    main()