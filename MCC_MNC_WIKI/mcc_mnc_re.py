import urllib
import re
import sqlite3

fhand = urllib.urlopen('https://en.wikipedia.org/wiki/Mobile_country_code')
# fhand = open('openurl.txt')
html_str = fhand.read()

conn = sqlite3.connect('mcc_mnc_db.sqlite')
cur = conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS COUNTRY;
DROP TABLE IF EXISTS MCC_MNC;

CREATE TABLE COUNTRY (
    id         INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name       TEXT UNIQUE
);

CREATE TABLE MCC_MNC (
    id         INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    country_id INTEGER,
    mcc        TEXT,
    mnc        TEXT,
    support_band TEXT    
);

''')

item_list = re.findall('''
<h3><span class="\S*" id="(\S+?)"><a href=|
<tr>\s*<td>([0-9]*)</td>\s*<td>([0-9]*)</td>\s*<td>.*</td>\s*<td>.*</td>\s*<td>.*</td>\s*<td>(.*)</td>''', html_str)
print 'len of item_list', len(item_list)
country_name = ''
for item in item_list:
    print '*************'
#    print item
#    if len(item[0]) > 0: print item
    if item[0]:
        country_name = item[0]
        print 'Get country name', country_name
        continue

    if item[1]:
        if item[1] == '901': break # international operators
        mcc_code = item[1]
        mnc_code = item[2]
        support_band = item[3]
    else:
        print 'No MCC, ignore', country_name
        continue
    if not country_name: continue # skip TEST Network
    print country_name, mcc_code, mnc_code, support_band

    cur.execute('''INSERT OR IGNORE INTO COUNTRY (name) 
    VALUES (?)''', (country_name, ))

    cur.execute('SELECT id FROM COUNTRY WHERE name = ? ', (country_name, ))
    country_id = cur.fetchone()[0]
    
    cur.execute('''INSERT OR IGNORE INTO MCC_MNC (country_id, mcc, mnc, support_band) 
    VALUES (?, ?, ?, ?)''', (country_id, mcc_code, mnc_code, support_band))

    conn.commit()
    