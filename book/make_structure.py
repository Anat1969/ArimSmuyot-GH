# מבנה "ערים סמויות": סדר קריאה ופרקים לפי ויקיפדיה (טבלת הערים לפי סדר הופעה).
# השיוך לסדרה ולמספר בתוכה נגזר מהתבנית הקבועה של הספר, ואומת מול הקובץ של ענת.
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
EN = ['Diomira','Isidora','Dorothea','Zaira','Anastasia','Tamara','Zora','Despina','Zirma','Isaura',
 'Maurilia','Fedora','Zoe','Zenobia','Euphemia','Zobeide','Hypatia','Armilla','Chloe','Valdrada',
 'Olivia','Sophronia','Eutropia','Zemrude','Aglaura','Octavia','Ersilia','Baucis','Leandra','Melania',
 'Esmeralda','Phyllis','Pyrrha','Adelma','Eudoxia','Moriana','Clarice','Eusapia','Beersheba','Leonia',
 'Irene','Argia','Thekla','Trude','Olinda','Laudomia','Perinthia','Procopia','Raissa','Andria',
 'Cecilia','Marozia','Penthesilea','Theodora','Berenice']
HE = ['דיומירה','איזידורה','דורותיאה','זאירה','אנסטסיה','תמרה','זורה','דספינה','זירמה','איסאורה',
 'מאורליה','פדורה','זואה','זנוביה','אופמיה','זוביידה','היפאטיה','ארמילה','קלואה','וואלדראדה',
 'אוליביה','סופרוניה','אוטרופיה','זמרודה','אגלאורה','אוקטביה','ארסיליה',"באוצ'יס",'לאנדרה','מלאניה',
 'אזמרלדה','פיליס','פירה','אדלמה','אודוקסיה','מוריאנה',"קלאריצ'ה",'אאוספיה','באר שבע','לאוניה',
 'אירנה','ארגיה','התקלה','טרודה','אוליינדה','לאודומיה','פרינתיה','פרוקופיה','רייסה','אנדריה',
 "צ'צ'יליה",'מרוזיה','פנתסילאה','תאודורה','ברניקה']
KEYS = ['mem','des','sig','thin','trade','eyes','names','dead','sky','cont','hidden']
# תבנית הספר: פרק 1, פרקים 2 עד 8 (סדרה c-1 מספר 5, ואז יורד), פרק 9.
seq = [(1,1),(1,2),(2,1),(1,3),(2,2),(3,1),(1,4),(2,3),(3,2),(4,1)]
for c in range(2, 9): seq += [(c-1+j, 5-j) for j in range(5)]
seq += [(8,5),(9,4),(10,3),(11,2),(9,5),(10,4),(11,3),(10,5),(11,4),(11,5)]
chap = [1]*10 + [c for c in range(2,9) for _ in range(5)] + [9]*10
assert len(seq) == 55 and len(chap) == 55
assert sorted(seq) == sorted((s, n) for s in range(1,12) for n in range(1,6))
cities = {c['n']: c for c in json.load(open(sys.argv[1], encoding='utf8'))}
out, diff = [], []
for i in range(55):
    s, n = seq[i]; he = HE[i]; c = cities.get(he)
    out.append(dict(pos=i+1, chapter=chap[i], en=EN[i], he=he, s=KEYS[s-1], n=n,
                    inFile=bool(c), t=c['t'] if c else '', d=c['d'] if c else ''))
    if c and c['k'] != KEYS[s-1]: diff.append(f"{he}: בקובץ {c['k']}, בספר {KEYS[s-1]} {n}")
json.dump(out, open(os.path.join(HERE, 'structure.json'), 'w', encoding='utf8'), ensure_ascii=False, indent=0)
print('בקובץ:', sum(o['inFile'] for o in out), 'מתוך 55. חסרות:', ', '.join(o['he'] for o in out if not o['inFile']))
print('סיווג שונה מהקובץ:', '; '.join(diff) or 'אין')
print('בקובץ ולא בספר:', ', '.join(n for n in cities if n not in HE))
