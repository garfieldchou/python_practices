import urllib
import re
import sqlite3
from BeautifulSoup import *

data = ['''
<h3><span class="mw-headline" id="Abkhazia_-_GE-AB"><a href="/wiki/Abkhazia" title="Abkhazia">Abkhazia</a> - GE-AB</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=Mobile_country_code&amp;action=edit&amp;section=3" title="Edit section: Abkhazia - GE-AB">edit</a><span class="mw-editsection-bracket">]</span></span></h3>
<table class="wikitable" width="100%">
<tr>
<th width="4%">MCC</th>
<th width="4%">MNC</th>
<th width="12%">Brand</th>
<th width="22%">Operator</th>
<th width="10%">Status</th>
<th width="28%">Bands (MHz)</th>
<th width="20%">References and notes</th>
</tr>
<tr>
<td>289</td>
<td>67</td>
<td>Aquafon</td>
<td>Aquafon JSC</td>
<td>Operational</td>
<td>GSM 900 / GSM 1800 / UMTS 2100 / LTE 800</td>
<td>LTE band 20<sup id="cite_ref-gsa_lte_81-0" class="reference"><a href="#cite_note-gsa_lte-81">[81]</a></sup></td>
</tr>
<tr>
<td>289</td>
<td>88</td>
<td>A-Mobile</td>
<td>A-Mobile LLSC</td>
<td>Operational</td>
<td>GSM 900 / GSM 1800 / UMTS 2100 / LTE 800 / LTE 1800</td>
<td></td>
</tr>
</table>
<h3><span class="mw-headline" id="Bonaire.2C_Saba.2C_Sint_Eustatius_.28Kingdom_of_the_Netherlands.29_-_BQ"><a href="/wiki/BES_islands" class="mw-redirect" title="BES islands">Bonaire, Saba, Sint Eustatius</a> (<a href="/wiki/Kingdom_of_the_Netherlands" title="Kingdom of the Netherlands">Kingdom of the Netherlands</a>) - BQ</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=Mobile_country_code&amp;action=edit&amp;section=30" title="Edit section: Bonaire, Saba, Sint Eustatius (Kingdom of the Netherlands) - BQ">edit</a><span class="mw-editsection-bracket">]</span></span></h3>
<p>See <a href="#Former_Netherlands_Antilles_.28Kingdom_of_the_Netherlands.29_-_BQ.2FCW.2FSX">Former Netherlands Antilles</a></p>
<h3><span class="mw-headline" id="Vatican_-_VA"><a href="/wiki/Vatican_City" title="Vatican City">Vatican</a> - VA</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=Mobile_country_code&amp;action=edit&amp;section=241" title="Edit section: Vatican - VA">edit</a><span class="mw-editsection-bracket">]</span></span></h3>
<table class="wikitable" width="100%">
<tr>
<th width="4%">MCC</th>
<th width="4%">MNC</th>
<th width="12%">Brand</th>
<th width="22%">Operator</th>
<th width="10%">Status</th>
<th width="28%">Bands (MHz)</th>
<th width="20%">References and notes</th>
</tr>
<tr>
<td>225</td>
<td></td>
<td></td>
<td></td>
<td>Not operational</td>
<td></td>
<td>The Vatican is served by Italian networks <a href="/wiki/Telecom_Italia_Mobile" class="mw-redirect" title="Telecom Italia Mobile">TIM</a>, <a href="/wiki/Vodafone_Italy" title="Vodafone Italy">Vodafone Italy</a>, <a href="/wiki/WIND_(Italy)" title="WIND (Italy)">Wind</a> and 3</td>
</tr>
</table>
<h3><span class="mw-headline" id="Christmas_Island_.28Australia.29_-_CX"><a href="/wiki/Christmas_Island" title="Christmas Island">Christmas Island</a> (Australia) - CX</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=Mobile_country_code&amp;action=edit&amp;section=49" title="Edit section: Christmas Island (Australia) - CX">edit</a><span class="mw-editsection-bracket">]</span></span></h3>
<table class="wikitable" width="100%">
<tr>
<th width="4%">MCC</th>
<th width="4%">MNC</th>
<th width="12%">Brand</th>
<th width="22%">Operator</th>
<th width="10%">Status</th>
<th width="28%">Bands (MHz)</th>
<th width="20%">References and notes</th>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</table>
<h3><span class="mw-headline" id="Taiwan_-_TW"><a href="/wiki/Taiwan" title="Taiwan">Taiwan</a> - TW</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=Mobile_country_code&amp;action=edit&amp;section=220" title="Edit section: Taiwan - TW">edit</a><span class="mw-editsection-bracket">]</span></span></h3>
<table class="wikitable" width="100%">
<tr>
<th width="4%">MCC</th>
<th width="4%">MNC</th>
<th width="12%">Brand</th>
<th width="22%">Operator</th>
<th width="10%">Status</th>
<th width="28%">Bands (MHz)</th>
<th width="20%">References and notes</th>
</tr>
<tr>
<td>466</td>
<td>01</td>
<td><a href="/wiki/FarEasTone" title="FarEasTone">FarEasTone</a></td>
<td>Far EasTone Telecommunications Co Ltd</td>
<td>Operational</td>
<td>GSM 900 / GSM 1800 / UMTS 2100 / LTE 700 / LTE 1800 / LTE 2600</td>
<td>LTE band 28<sup id="cite_ref-gsa_lte_81-234" class="reference"><a href="#cite_note-gsa_lte-81">[81]</a></sup></td>
</tr>
<tr>
<td>466</td>
<td>02</td>
<td><a href="/wiki/FarEasTone" title="FarEasTone">FarEasTone</a></td>
<td>Far EasTone Telecommunications Co Ltd</td>
<td>Unknown</td>
<td>GSM 900</td>
<td><sup id="cite_ref-authority_tw_237-0" class="reference"><a href="#cite_note-authority_tw-237">[237]</a></sup></td>
</tr>
<tr>
<td>466</td>
<td>03</td>
<td><a href="/wiki/FarEasTone" title="FarEasTone">FarEasTone</a></td>
<td>Far EasTone Telecommunications Co Ltd</td>
<td>Unknown</td>
<td>UMTS 2100</td>
<td><sup id="cite_ref-authority_tw_237-1" class="reference"><a href="#cite_note-authority_tw-237">[237]</a></sup></td>
</tr>
<tr>
<td>466</td>
<td>05</td>
<td>APTG</td>
<td>Asia Pacific Telecom</td>
<td>Operational</td>
<td>CDMA2000 800 / LTE 700</td>
<td>LTE band 28<sup id="cite_ref-gsa_lte_81-235" class="reference"><a href="#cite_note-gsa_lte-81">[81]</a></sup></td>
</tr>
<tr>
<td>466</td>
<td>06</td>
<td><a href="/wiki/FarEasTone" title="FarEasTone">FarEasTone</a></td>
<td>Far EasTone Telecommunications Co Ltd</td>
<td>Operational</td>
<td>GSM 1800</td>
<td>Former KG Telecom until 2004</td>
</tr>
<tr>
<td>466</td>
<td>07</td>
<td><a href="/wiki/FarEasTone" title="FarEasTone">FarEasTone</a></td>
<td>Far EasTone Telecommunications Co Ltd</td>
<td>Not operational</td>
<td>WiMAX 2600</td>
<td>Shut down in 2015<sup id="cite_ref-authority_tw_237-2" class="reference"><a href="#cite_note-authority_tw-237">[237]</a></sup><sup id="cite_ref-TaipeiTimesWimax_238-0" class="reference"><a href="#cite_note-TaipeiTimesWimax-238">[238]</a></sup></td>
</tr>
<tr>
<td>466</td>
<td>09</td>
<td>VMAX</td>
<td><a rel="nofollow" class="external text" href="http://www.vmax.net.tw/">Vmax Telecom</a></td>
<td>Operational</td>
<td>WiMAX 2600</td>
<td><sup id="cite_ref-authority_tw_237-3" class="reference"><a href="#cite_note-authority_tw-237">[237]</a></sup></td>
</tr>
<tr>
<td>466</td>
<td>10</td>
<td>G1</td>
<td><a rel="nofollow" class="external text" href="http://www.g1.com.tw">Global Mobile Corp.</a></td>
<td>Operational</td>
<td>WiMAX 2600</td>
<td><sup id="cite_ref-authority_tw_237-4" class="reference"><a href="#cite_note-authority_tw-237">[237]</a></sup></td>
</tr>
<tr>
<td>466</td>
<td>11</td>
<td>Chunghwa LDM</td>
<td>LDTA/<a href="/wiki/Chunghwa_Telecom" title="Chunghwa Telecom">Chunghwa Telecom</a></td>
<td>Operational</td>
<td>GSM 1800</td>
<td>Also known as "Long Distance &amp; Mobile Business Group"</td>
</tr>
<tr>
<td>466</td>
<td>12</td>
<td></td>
<td><a rel="nofollow" class="external text" href="http://www.ambit.com.tw">Ambit Microsystems</a></td>
<td>Operational</td>
<td>LTE 700 / LTE 900</td>
<td>Subsidiary of <a href="/wiki/Foxconn" title="Foxconn">Foxconn</a>; LTE band 28 <sup id="cite_ref-239" class="reference"><a href="#cite_note-239">[239]</a></sup><sup id="cite_ref-taiwan_mnc_blog_240-0" class="reference"><a href="#cite_note-taiwan_mnc_blog-240">[240]</a></sup></td>
</tr>
<tr>
<td>466</td>
<td>56</td>
<td>FITEL</td>
<td><a href="/wiki/First_International_Telecom" title="First International Telecom">First International Telecom</a></td>
<td>Not operational</td>
<td>WiMAX 2600 / PHS</td>
<td>Bankruptcy in 2014<sup id="cite_ref-authority_tw_237-5" class="reference"><a href="#cite_note-authority_tw-237">[237]</a></sup><sup id="cite_ref-TaipeiTimesWimax_238-1" class="reference"><a href="#cite_note-TaipeiTimesWimax-238">[238]</a></sup></td>
</tr>
<tr>
<td>466</td>
<td>68</td>
<td></td>
<td>Tatung InfoComm</td>
<td>Not operational</td>
<td>WiMAX 2600</td>
<td>License expired in 2014 <sup id="cite_ref-authority_tw_237-6" class="reference"><a href="#cite_note-authority_tw-237">[237]</a></sup><sup id="cite_ref-TaipeiTimesWimax_238-2" class="reference"><a href="#cite_note-TaipeiTimesWimax-238">[238]</a></sup><sup id="cite_ref-241" class="reference"><a href="#cite_note-241">[241]</a></sup></td>
</tr>
<tr>
<td>466</td>
<td>88</td>
<td><a href="/wiki/FarEasTone" title="FarEasTone">FarEasTone</a></td>
<td>Far EasTone Telecommunications Co Ltd</td>
<td>Operational</td>
<td>GSM 1800</td>
<td>Former KG Telecom until 2004, KG Telecom brand used until 2009</td>
</tr>
<tr>
<td>466</td>
<td>89</td>
<td>T Star</td>
<td><a href="/wiki/Vibo_Telecom" class="mw-redirect" title="Vibo Telecom">Taiwan Star Telecom</a></td>
<td>Operational</td>
<td>UMTS 2100 / LTE 900 / LTE 2600</td>
<td><sup id="cite_ref-gsa_lte_81-236" class="reference"><a href="#cite_note-gsa_lte-81">[81]</a></sup></td>
</tr>
<tr>
<td>466</td>
<td>90</td>
<td>T Star</td>
<td><a href="/wiki/Vibo_Telecom" class="mw-redirect" title="Vibo Telecom">Taiwan Star Telecom</a></td>
<td>Unknown</td>
<td>LTE 900</td>
<td><sup id="cite_ref-taiwan_mnc_blog_240-1" class="reference"><a href="#cite_note-taiwan_mnc_blog-240">[240]</a></sup></td>
</tr>
<tr>
<td>466</td>
<td>92</td>
<td>Chunghwa</td>
<td><a href="/wiki/Chunghwa_Telecom" title="Chunghwa Telecom">Chunghwa Telecom</a></td>
<td>Operational</td>
<td>GSM 900 / GSM 1800 / UMTS 2100 / LTE 900 / LTE 1800 / LTE 2600</td>
<td><sup id="cite_ref-gsa_lte_81-237" class="reference"><a href="#cite_note-gsa_lte-81">[81]</a></sup></td>
</tr>
<tr>
<td>466</td>
<td>93</td>
<td>MobiTai</td>
<td>Mobitai Communications</td>
<td>Not operational</td>
<td>GSM 900</td>
<td>Acquired by <a href="/wiki/Taiwan_Mobile" title="Taiwan Mobile">Taiwan Mobile</a> in 2004, MobiTai brand used until 2008</td>
</tr>
<tr>
<td>466</td>
<td>97</td>
<td><a href="/wiki/Taiwan_Mobile" title="Taiwan Mobile">Taiwan Mobile</a></td>
<td>Taiwan Mobile Co. Ltd</td>
<td>Operational</td>
<td>GSM 900 / GSM 1800 / UMTS 2100 / LTE 700 / LTE 1800</td>
<td>LTE band 28<sup id="cite_ref-gsa_lte_81-238" class="reference"><a href="#cite_note-gsa_lte-81">[81]</a></sup></td>
</tr>
<tr>
<td>466</td>
<td>99</td>
<td>TransAsia</td>
<td>TransAsia Telecoms</td>
<td>Not operational</td>
<td>GSM 900</td>
<td>Acquired by <a href="/wiki/Taiwan_Mobile" title="Taiwan Mobile">Taiwan Mobile</a> in 2002, TransAsia brand used until 2008</td>
</tr>
</table>
''']

conn = sqlite3.connect('mcc_mnc_db.sqlite')
cur = conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS MCC;
DROP TABLE IF EXISTS MNC;

CREATE TABLE MCC (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    code   TEXT UNIQUE,
    name   TEXT UNIQUE
);

CREATE TABLE MNC (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    mcc_id INTEGER,
    mnc_code TEXT
);

''')

item_list = re.findall('<h3><span class="\S*" id="(\S+?)"|<tr>..<td>([0-9]*)</td>..<td>([0-9]*)</td>', str(data))
print 'len of item_list', len(item_list)
for item in item_list:
    print '*************'
#    print item
#    if len(item[0]) > 0: print item
    if item[0]:
        country_name = item[0]
        print 'Get country name', country_name
        continue
    if item[1]:
        mcc_code = item[1]
        mnc_code = item[2]
    else:
        print 'No MCC, ignore', country_name
        continue
    print country_name, mcc_code, mnc_code
    
    cur.execute('''INSERT OR IGNORE INTO MCC (code, name) 
    VALUES (?, ?)''', (mcc_code, country_name))

    cur.execute('SELECT id FROM MCC WHERE code = ? ', (mcc_code, ))
    mcc_id = cur.fetchone()[0]
    
    cur.execute('''INSERT INTO MNC (mcc_id, mnc_code)
    VALUES (?, ?)''', (mcc_id, mnc_code))
    
    conn.commit()
    