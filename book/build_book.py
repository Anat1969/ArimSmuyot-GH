# בונה את "ספר הערים הסמויות": עמוד לכל עיר, תמונה אחת, מתח, תובנה והייקו.
import base64, json, os, sys, html, math
HERE = os.path.dirname(os.path.abspath(__file__))
PAGES = [
 dict(id='desp', n='דספינה', cat='ערים והתשוקה', t='ים מול מדבר',
      i='כל עיר מקבלת את צורתה מהמדבר שאליו היא מתנגדת. מי שמגיע בספינה רואה בה גמל, ומי שמגיע על גמל רואה בה ספינה.',
      h=['ספינה רואה גמל','גמל רואה ספינה','העיר: מה שחסר'], img='desp.jpg'),
 dict(id='fed', n='פדורה', cat='ערים והזיכרון', t='עיר אפורה מול עיר בכדור זכוכית',
      i='העתיד שהיה אפשרי אתמול הופך היום לצעצוע בכדור זכוכית. מה שלא התממש נשמר כמודל, מושלם וזעיר.',
      h=['בתוך הזכוכית','העיר שכמעט הייתה','ישנה ולא גדלה'], img='fed.jpg'),
 dict(id='oct', n='אוקטביה', cat='הערים הדקות', t='רשת דקה מול תהום',
      i='החיים בה פחות חסרי ודאות, כי התושבים יודעים כמה הרשת דקה. ידיעת השבריריות היא שמקנה להם ביטחון.',
      h=['חבל מעל תהום','הם יודעים כמה הוא דק','ולכן ישנים'], img='oct.jpg'),
 dict(id='vald', n='וואלדראדה', cat='ערים והעיניים', t='עיר מול השתקפותה',
      i='שתי הערים חיות זו למען זו, אך בלי אהבה. ההשתקפות המדויקת לא משאירה מקום למקרה או לרגע פרטי.',
      h=['כל נשיקה כאן','קורית בה פעמיים','ואחת מהן קרה'], img='vald.jpg'),
 dict(id='leon', n='לאוניה', cat='ערים מתמשכות', t='שפע מבריק מול הר של עבר',
      i='העושר נמדד לא במה שקונים אלא במה שזורקים. העיר מתחדשת כל בוקר, ומוקפת בטבעת של הפסולת שלה עצמה.',
      h=['בכל בוקר חדש','ההר שמאחורי העיר','גבוה עוד קצת'], img='leon.jpg'),

 dict(id='arm', n='ארמילה', cat='הערים הדקות', t='תשתית חשופה מול קירות שנעלמו',
      i='אולי היא קורבן לנימפות על שימוש לרעה במים, ואולי שריד של מבנה שהתכלה. המעטפת נעלמה, והתשתית נותרה.',
      h=['אין קיר ואין גג','רק המים זוכרים','איפה היה בית'], img='arm.jpg'),
 dict(id='zen', n='זנוביה', cat='הערים הדקות', t='תשוקה שמתרוממת מול אדמה יבשה',
      i='אין טעם לחלק ערים למאושרות ואומללות. יש ערים שנותנות צורה לתשוקה, ויש ערים שהתשוקה נמחקה בהן.',
      h=['על רגליים דקות','הבית מושיט את ידו','אל מה שאין לו'], img='zen.jpg'),
 dict(id='eus', n='אאוספיה', cat='ערים והמתים', t='חיים מעל מול חיים זהים מתחת',
      i='כשהחיים מחקים את דפוסי המוות, אין עוד דרך לדעת מי חי ומי מת.',
      h=['מתחת לאדמה','השולחן ערוך כמו כאן','מי כאן חי באמת'], img='eus.jpg'),
 dict(id='oli', n='אוליביה', cat='ערים והסימנים', t='פאר מתואר מול פיח אמיתי',
      i='השקר אינו במילים אלא בדברים עצמם. לפעמים הדרך היחידה לתאר זוהמה היא דרך ההפך שלה.',
      h=['מילים של כסף','מעל כל ארובה','הפיח לא שומע'], img='oli.jpg'),
 dict(id='ars', n='ארסיליה', cat='ערי חילופין', t='רשת קשרים מול חלל ריק',
      i='העיר היא רשת של קשרים. כשהחוטים צפופים מדי, התושבים עוזבים, ונשארת רק הרשת.',
      h=['הבתים הלכו','החוטים נשארו מתוחים','בין מי שהיו'], img='ars.jpg'),
 dict(id='isi', n='איזידורה', cat='ערים והזיכרון', t='תשוקת נעורים מול זקנה שמגיעה מאוחר',
      i='העיר של החלומות מגיעה מאוחר מדי. האדם מגיע אליה בזקנתו, כשתשוקותיו כבר הפכו לזיכרון.',
      h=['העיר שחלמתי','מחכה לי בסוף הדרך','ואני כבר זקן'], img='isi.jpg'),
 dict(id='tam', n='תמרה', cat='ערים והסימנים', t='מציאות מול סימן שמחליף אותה',
      i='העיר אומרת לך מה לחשוב. המציאות מוסתרת תחת שכבה של סימנים, והעין רואה רק אותם.',
      h=['צבת, קנקן, מאזניים','העין קוראת סימנים','העיר עצמה נעלמת'], img='tam.jpg'),
 dict(id='euf', n='אופמיה', cat='ערי חילופין', t='סחורה מול זיכרון',
      i='המהות של העיר היא מפגש. המסחר האמיתי בה הוא בסיפורים שמחליפים סביב המדורה.',
      h=['מוכרים זנגביל','קונים סיפור של זר','והולכים עשירים'], img='euf.jpg'),
 dict(id='esm', n='אזמרלדה', cat='ערי חילופין', t='קו ישר מול רשת של אפשרויות',
      i='המרחק הקצר בין שתי נקודות הוא זיגזג. הרשת מאפשרת מסלול חדש בכל יום, ומונעת שעמום.',
      h=['אין דרך קצרה','רק זיגזג בין גשרים','כל בוקר חדש'], img='esm.jpg'),
 dict(id='eud', n='אודוקסיה', cat='ערים והשמיים', t='כאוס של סמטאות מול סדר של שטיח',
      i='השטיח מראה את הסדר שחומק מהעין בתוך המהומה. הוא האמת של העיר, או אולי רק המראה שלה.',
      h=['סבך של סמטאות','ובשטיח הכול ברור','מי משקף את מי'], img='eud.jpg'),
]
PAGES = [p for p in PAGES if os.path.exists(os.path.join(HERE, p['img']))]
ALL = [c['n'] for c in json.load(open(sys.argv[1], encoding='utf8'))]
def thumb(f):
    import io
    from PIL import Image
    b=io.BytesIO(); Image.open(os.path.join(HERE,f)).convert('RGB').resize((360,360),Image.LANCZOS).save(b,'JPEG',quality=78,optimize=True)
    return 'data:image/jpeg;base64,'+base64.b64encode(b.getvalue()).decode()
def uri(f): return 'data:image/jpeg;base64,' + base64.b64encode(open(os.path.join(HERE, f), 'rb').read()).decode()
e = html.escape
# ---------- מבנה הספר, סדרות, סימנים ----------
STRUCT = json.load(open(os.path.join(HERE, 'structure.json'), encoding='utf8'))
POS = {c['he']: c for c in STRUCT}
SER = {'mem':('ערים והזיכרון','#8A6BB0'),'des':('ערים והתשוקה','#C0564C'),'sig':('ערים והסימנים','#B0852B'),
 'thin':('הערים הדקות','#3B8C98'),'trade':('ערי חילופין','#CC7636'),'eyes':('ערים והעיניים','#3F6DB3'),
 'names':('ערים והשמות','#7A8A38'),'dead':('ערים והמתים','#6E6C78'),'sky':('ערים והשמיים','#2F4F8F'),
 'cont':('ערים מתמשכות','#A35E46'),'hidden':('הערים הנסתרות','#954A7B')}
ORDER = list(SER)
G = {'mem':'<path d="M12 12a1.5 1.5 0 1 1 1.5 1.5a3 3 0 1 1-3-3a4.5 4.5 0 1 1 4.5 4.5a6 6 0 1 1-6-6"/>',
 'des':'<path d="M12 3l7 9-7 9-7-9z"/><path d="M12 8l3 4-3 4-3-4z"/>',
 'sig':'<path d="M5 5h14v14H5z"/><path d="M12 5v14M5 12h14"/>',
 'thin':'<path d="M7 4v16M12 4v16M17 4v16M4 8h16"/>',
 'trade':'<path d="M4 9h15l-3-3M20 15H5l3 3"/>',
 'eyes':'<path d="M3 12q9-8 18 0q-9 8-18 0z"/><circle cx="12" cy="12" r="2.5"/>',
 'names':'<path d="M5 6h14M5 11h10M5 16h12"/><circle cx="18" cy="17" r="1.6"/>',
 'dead':'<path d="M7 14a5 5 0 0 1 10 0"/><path d="M4 14h16M7 18h10"/>',
 'sky':'<path d="M12 3l2.4 5.6 6.1.6-4.6 4 1.4 6-5.3-3.2-5.3 3.2 1.4-6-4.6-4 6.1-.6z"/>',
 'cont':'<circle cx="12" cy="12" r="2.5"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="9.5"/>',
 'hidden':'<circle cx="12" cy="12" r="8" stroke-dasharray="2.4 2.6"/><circle cx="12" cy="12" r="1.6" fill="currentColor"/>'}
def glyph(k, size=16, color=None):
    return f'<svg class="gl" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" style="color:{color or SER[k][1]}" aria-hidden="true">{G[k]}</svg>'

PAGES.sort(key=lambda p: POS[p['n']]['pos'])
done = {p['n'] for p in PAGES}
N = len(PAGES)
CC = max(2, math.ceil(math.sqrt(N)))
RR = math.ceil(N / CC)
FIRST_CITY = 4  # 0 כריכה סגורה, 1 שער, 2 פרטיטורה, 3 מקרא
spreads = []
# 0: כריכה סגורה. הכריכה בצד שמאל, ובצד ימין שולחן.
ring = ''.join(f'<span style="--a:{i*360/11}deg">{glyph(k, 22, "#C9B37E")}</span>' for i, k in enumerate(ORDER))
spreads.append((f'''<div class="pg-cover"><div class="ring">{ring}</div>
  <div class="ct"><small>איטלו קאלווינו</small><h1>ספר הערים<br>הסמויות</h1><span>{N} ערים · כרך ראשון</span></div>
  <p class="open">לפתיחה, לחצי על הכריכה</p></div>''', '<div class="pg-img endpaper"></div>', 'כריכה'))
# 1: שער ותוכן
toc = ''.join(f'<li><button data-to="{FIRST_CITY+k}">{glyph(POS[p["n"]]["s"], 13)}<b>{POS[p["n"]]["pos"]:02d}</b>{e(p["n"])}</button></li>' for k, p in enumerate(PAGES))
mosaic = ''.join(f'<button class="cell" data-to="{FIRST_CITY+k}" aria-label="{e(p["n"])}"><span class="ph"><img src="{thumb(p["img"])}" alt=""></span><small><b>{k+1:02d}</b>{e(p["n"])}</small></button>' for k, p in enumerate(PAGES))
spreads.append((f'''<div class="pg-text" style="--c:#2E2E2B">
  <div class="rh"><span>שער</span><span><button class="tocover" data-to="0" title="לכריכה">ספר הערים הסמויות</button></span></div>
  <div class="mid"><h1>ספר הערים הסמויות</h1><p class="sub">כל עיר היא מתח אחד. התמונה מחזיקה אותו, וההייקו משאיר אותו פתוח.</p></div>
  <ol class="toc">{toc}</ol>
  <div class="folio">1</div>
</div>''', f'<div class="pg-img contact" style="--cols:{CC};--rows:{RR}"><div class="grid">{mosaic}</div></div>', 'שער'))
# 2: הפרטיטורה
legend = ''.join(f'<li>{glyph(k,14)}<span>{SER[k][0]}</span></li>' for k in ORDER)
spreads.append((f'''<div class="pg-text" style="--c:#2E2E2B">
  <div class="rh"><span>מפת הספר</span><span><button class="tocover" data-to="0" title="לכריכה">ספר הערים הסמויות</button></span></div>
  <div class="mid"><h2>פרטיטורה</h2>
    <p class="insight">55 ערים ב-11 סדרות, חמש בכל סדרה, מחולקות ל-9 פרקים. <b>הציר האופקי הוא סדר הקריאה</b>, מימין לשמאל, והקווים האנכיים מפרידים בין הפרקים. <b>כל שורה היא סדרה.</b></p>
    <p class="insight keys"><i class="k1"></i>בספר, לחיצה פותחת <i class="k2"></i>בקובץ, עוד בלי תמונה <i class="k3"></i>לא בקובץ</p>
    <ul class="legend">{legend}</ul>
  </div>
  <p class="src">מקור: סדר הקריאה והפרקים לפי ויקיפדיה. השיוך לסדרות נגזר מהתבנית של הספר ואומת מול הקובץ.</p>
  <div class="folio">3</div>
</div>''', '<div class="pg-img score-pg"><div class="score-wrap"><svg class="score" data-big="0"></svg></div></div>', 'פרטיטורה'))
TB = '<button class="tocover" data-to="0" title="לכריכה">ספר הערים הסמויות</button>'
LEG_R = f'''<div class="pg-text" style="--c:#2E2E2B">
  <div class="rh"><span>מקרא</span><span>{TB}</span></div>
  <div class="mid"><h2>מקרא</h2>
    <ol class="howto">
      <li><b>שורת הראש:</b> הסימן והשם של הסדרה, המקום של העיר בסדרה מתוך 5, ומספר הפרק.</li>
      <li><b>שם העיר,</b> ומתחתיו <b>המתח</b>: הניגוד האחד שהתמונה מחזיקה, במרקר בצבע הסדרה.</li>
      <li><b>התובנה:</b> פרשנות מתוך הקובץ.</li>
      <li><b>ההייקו:</b> נכתב לספר הזה, ומשאיר את המתח פתוח.</li>
      <li><b>העמוד השמאלי:</b> התמונה, שנוצרה מהמתח, בגודל מלא.</li>
      <li><b>מתחת לספר:</b> פס של 55 ערים. העיר הפתוחה ממוסגרת, ולחיצה על הפס פותחת את המפה.</li>
      <li><b>עובי הדפים</b> בשני הצדדים מראה כמה קראת וכמה נשאר.</li>
    </ol>
  </div>
  <p class="src">עובדה: מבנה הספר, הסדר והפרקים. פרשנות: התובנות מהקובץ. יצירה: המתח, ההייקו והתמונות.</p>
  <div class="folio">7</div>
</div>'''
SERDESC = {'mem':'העיר כפי שהיא נשמרת ונשכחת','des':'העיר כפי שרוצים אותה','sig':'העיר כטקסט שקוראים',
 'thin':'ערים קלות, שלד בלי משקל','trade':'מה שעובר בין אנשים','eyes':'העיר כפי שהמבט בונה אותה',
 'names':'הפער בין השם למקום','dead':'העבר שחי לצד ההווה','sky':'הסדר שמעל העיר',
 'cont':'עיר שאין לה סוף','hidden':'עיר בתוך עיר'}
leg = ''.join(f'<li>{glyph(k,18)}<div><b style="color:{SER[k][1]}">{SER[k][0]}</b><span>{SERDESC[k]}</span></div></li>' for k in ORDER)
spreads.append((LEG_R, f'''<div class="pg-img legend-pg"><div class="lg-in">
  <h3>11 הסדרות <small>פרשנות קצרה</small></h3><ul class="serlist">{leg}</ul>
  <h3>במפה</h3><p class="keys"><i class="k1"></i>בספר, לחיצה פותחת <i class="k2"></i>בקובץ, עוד בלי תמונה <i class="k3"></i>לא בקובץ <i class="k4"></i>העיר הפתוחה</p>
  <h3>ניווט</h3><ul class="navkeys"><li><kbd>←</kbd> או "הבא": עמוד קדימה</li><li><kbd>→</kbd> או "הקודם": עמוד אחורה</li><li>לחיצה על העמוד השמאלי או הימני</li><li><kbd>Home</kbd> או "לכריכה": חזרה לכריכה</li><li><kbd>End</kbd>: סוף הספר</li><li><kbd>M</kbd>: מפת הספר</li><li><kbd>?</kbd>: המקרא</li><li>בנייד: החלקה</li></ul>
</div></div>''', 'מקרא'))
for k, p in enumerate(PAGES):
    st = POS[p['n']]; sname, col = SER[st['s']]
    spreads.append((f'''<div class="pg-text" style="--c:{col}">
  <div class="rh"><span>{glyph(st['s'],15)}{sname} · {st['n']} מתוך 5</span><span><button class="tocover" data-to="0" title="לכריכה">ספר הערים הסמויות</button> · פרק {st['chapter']}</span></div>
  <div class="mid">
    <h2>{e(p['n'])}</h2>
    <p class="tension"><span class="lbl">המתח</span><mark>{e(p['t'])}</mark></p>
    <p class="insight">{e(p['i'])}</p>
  </div>
  <p class="haiku">{'<br>'.join(e(x) for x in p['h'])}</p>
  <div class="folio">{2*(FIRST_CITY+k)-1}</div>
</div>''', f'<div class="pg-img"><img src="{uri(p["img"])}" alt="{e(p["n"])}: {e(p["t"])}"></div>', p['n']))
allnames = ''.join(f'<button data-to="{FIRST_CITY+[i for i,q in enumerate(PAGES) if q["n"]==c["he"]][0]}" class="on">{e(c["he"])}</button>' if c['he'] in done else f'<span>{e(c["he"])}</span>' for c in STRUCT)
spreads.append((f'''<div class="pg-text" style="--c:#2E2E2B">
  <div class="rh"><span>סוף הכרך הראשון</span><span><button class="tocover" data-to="0" title="לכריכה">ספר הערים הסמויות</button></span></div>
  <div class="mid"><h2>{N} מתוך 55</h2><p class="insight">הערים המודגשות כבר בספר. השאר עוד מחכות לתמונה שלהן, ולמתח שיחזיק אותה.</p></div>
  <p class="haiku">עיר אחת נגמרת<br>כדי שתיפתח אחרת<br>בדף שעוד לבן</p>
  <div class="folio">{2*(FIRST_CITY+N)-1}</div>
</div>''', f'<div class="pg-img names"><div class="all">{allnames}</div></div>', 'סוף'))
tpl = ''.join(f'<template data-name="{e(nm)}"><div class="R">{r}</div><div class="L">{l}</div></template>' for r, l, nm in spreads)
# נתונים לפרטיטורה
thumbs = {p['n']: thumb(p['img']) for p in PAGES}
SD = [dict(p=c['pos'], c=c['chapter'], h=c['he'], s=ORDER.index(c['s']), n=c['n'], f=c['inFile'], t=c['t'],
          sp=(FIRST_CITY+[i for i,q in enumerate(PAGES) if q['n']==c['he']][0]) if c['he'] in done else -1) for c in STRUCT]
SDATA = json.dumps(dict(cities=SD, ser=[[SER[k][0], SER[k][1], G[k]] for k in ORDER], th=thumbs), ensure_ascii=False)

doc = f'''<title>ספר הערים הסמויות</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Frank+Ruhl+Libre:wght@300;400;500&family=Assistant:wght@300;400;600&display=swap">
<style>
/* פריסה: ספר פתוח במרכז המסך. עמוד ימין טקסט עם שורת ראש ומספר עמוד, עמוד שמאל תמונה מלאה בגודל S. השדרה במרכז. מתחת לספר: שורת בקרה עם פרטיטורה זעירה. עולם בהיר אחד, וכריכה כהה */
:root{{color-scheme:light;--desk:#E7E5E0;--paper:#FBFAF7;--ink:#2E2E2B;--ink2:#7A776F;--line:#E4E1DA;--board:#1F2733;--gold:#C9B37E;
  --display:'Frank Ruhl Libre',Georgia,serif;--body:'Assistant','Segoe UI',Arial,sans-serif;
  --S:min(calc(100vh - 170px),calc((100vw - 96px)/2),860px)}}
*{{box-sizing:border-box}}
html,body{{height:100%}}
@media (min-width:821px){{html{{overflow:hidden;overflow:clip}}}}
body{{margin:0;background:var(--desk);color:var(--ink);font-family:var(--body);direction:rtl;overflow:hidden;
  padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px))}}
.stage{{height:100%;display:grid;grid-template-columns:minmax(0,1fr);grid-template-rows:1fr auto;place-items:center;gap:14px;padding-block:22px 16px}}
.book{{position:relative;width:calc(var(--S)*2);height:var(--S);perspective:calc(var(--S)*5);direction:ltr;--tl:8px;--tr:2px;transition:transform .42s cubic-bezier(.45,.05,.25,1)}}
.book.closed{{transform:translateX(calc(var(--S)/-2))}}
.book::before{{content:"";position:absolute;inset:-10px calc(-12px - var(--tr)) -10px calc(-12px - var(--tl));border-radius:6px;background:#D8D4CC;box-shadow:0 40px 80px rgba(40,34,24,.25);transition:inset .6s}}
/* עובי הדפים: מחוץ לעמודים, כך שהעמוד והתמונה לא מצטמצמים */
.stack{{position:absolute;top:3px;bottom:3px;background:repeating-linear-gradient(90deg,#F4F1EA 0 1px,#D9D4CA 1px 2px);transition:width .6s}}
.stack.L{{right:100%;width:var(--tl);border-radius:3px 0 0 3px}}
.stack.R{{left:100%;width:var(--tr);border-radius:0 3px 3px 0}}
.book.closed::before{{inset:-10px -12px -10px calc(50% - 2px)}}
.book.closed .stack{{display:none}}
.side{{position:absolute;top:0;width:var(--S);height:var(--S);background:var(--paper);overflow:hidden}}
.side.L{{left:0;border-radius:3px 0 0 3px}}
.side.R{{right:0;border-radius:0 3px 3px 0}}
.book.closed .side.L{{visibility:hidden}}
.side.L::after,.side.R::after,.face::after{{content:"";position:absolute;top:0;bottom:0;width:14%;pointer-events:none;z-index:3}}
.side.L::after{{right:0;background:linear-gradient(to left,rgba(40,32,20,.22),rgba(40,32,20,0))}}
.side.R::after{{left:0;background:linear-gradient(to right,rgba(40,32,20,.16),rgba(40,32,20,0))}}
.leaf{{position:absolute;top:0;width:var(--S);height:var(--S);transform-style:preserve-3d;z-index:10;transition:transform .9s cubic-bezier(.45,.05,.25,1)}}
.leaf.fwd{{right:0;transform-origin:left center}}
.leaf.back{{left:0;transform-origin:right center}}
.face{{position:absolute;inset:0;backface-visibility:hidden;-webkit-backface-visibility:hidden;background:var(--paper);overflow:hidden}}
.face.b{{transform:rotateY(180deg)}}
.book .pg-text,.book .pg-cover .ct,.book .pg-cover .open,.book .pg-cover .ring{{transition:opacity .15s ease}}
.book.textout .pg-text,.book.textout .pg-cover .ct,.book.textout .pg-cover .open,.book.textout .pg-cover .ring{{opacity:0}}
.book.textin .pg-text,.book.textin .pg-cover .ct,.book.textin .pg-cover .open,.book.textin .pg-cover .ring{{animation:tin .22s ease}}
@keyframes tin{{from{{opacity:0}}to{{opacity:1}}}}
.endpaper{{background:#EEE8DC;box-shadow:inset 0 0 0 calc(var(--S)*.03) #E3DBCB}}
/* כריכה */
.pg-cover{{position:absolute;inset:0;direction:rtl;background:radial-gradient(120% 90% at 30% 20%,#2C3746,var(--board) 60%,#151B24);color:var(--gold);display:grid;place-items:center;cursor:pointer}}
.pg-cover::before{{content:"";position:absolute;inset:calc(var(--S)*.045);border:1px solid rgba(201,179,126,.35)}}
.ring{{position:absolute;inset:0}}
.ring span{{position:absolute;left:50%;top:50%;transform:rotate(var(--a)) translateY(calc(var(--S)*-.36)) rotate(calc(-1*var(--a)));margin:-11px 0 0 -11px;opacity:.85}}
.ct{{text-align:center;display:flex;flex-direction:column;gap:calc(var(--S)*.02);align-items:center}}
.ct small{{font-size:calc(var(--S)*.02);letter-spacing:.3em}}
.ct h1{{margin:0;font-family:var(--display);font-weight:300;font-size:calc(var(--S)*.095);line-height:1.05;text-shadow:0 1px 0 rgba(0,0,0,.6),0 -1px 0 rgba(255,240,200,.15)}}
.ct span{{font-size:calc(var(--S)*.018);letter-spacing:.2em;opacity:.8}}
.open{{position:absolute;bottom:calc(var(--S)*.07);margin:0;font-size:calc(var(--S)*.017);letter-spacing:.12em;opacity:.6}}
/* עמוד תמונה */
.pg-img{{position:absolute;inset:0;direction:rtl}}
.pg-img>img{{width:100%;height:100%;object-fit:cover;display:block}}
.contact{{background:var(--paper);display:flex;flex-direction:column;direction:rtl;padding:calc(var(--S)*.07) calc(var(--S)*.07) calc(var(--S)*.06) calc(var(--S)*.08)}}
.contact .grid{{flex:1;min-height:0;display:grid;grid-template-columns:repeat(var(--cols),minmax(0,1fr));grid-template-rows:repeat(var(--rows),minmax(0,1fr));gap:calc(var(--S)*.022) calc(var(--S)*.018)}}
.cell{{min-width:0;min-height:0;display:flex;flex-direction:column;background:none;border:0;padding:0;cursor:pointer;font:inherit;color:var(--ink);text-align:right}}
.cell .ph{{flex:1;min-height:0;overflow:hidden;background:#DCD8CF;box-shadow:0 1px 2px rgba(40,32,20,.12)}}
.cell img{{width:100%;height:100%;object-fit:cover;display:block;transition:transform .5s}}
.cell:hover img{{transform:scale(1.04)}}
.cell small{{flex:none;display:block;font-size:calc(var(--S)*.016);color:var(--ink2);padding-top:5px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}}
.cell small b{{font-weight:400;color:var(--ink);font-variant-numeric:tabular-nums;margin-inline-end:6px}}
.cell:focus-visible{{outline:2px solid var(--ink);outline-offset:3px}}
.names{{display:grid;place-items:center;padding:calc(var(--S)*.09);background:var(--paper)}}
.all{{display:flex;flex-wrap:wrap;justify-content:center;gap:calc(var(--S)*.012) calc(var(--S)*.024);font-family:var(--display);font-size:calc(var(--S)*.024)}}
.all span{{color:#C8C4BB}}
.all button{{font:inherit;color:var(--ink);background:none;border:0;padding:0;cursor:pointer;border-bottom:2px solid #F2E3A0}}
.score-pg{{background:var(--paper);display:grid;place-items:center;padding:calc(var(--S)*.05) calc(var(--S)*.04)}}
.score-wrap{{width:100%;overflow-x:auto}}
.score{{display:block;width:100%;height:auto;direction:ltr}}
.score .note{{cursor:pointer}}
.score .note:hover circle.o{{stroke-width:2.4}}
/* עמוד טקסט: אותו גריד בכל עמוד */
.pg-text{{position:absolute;inset:0;direction:rtl;display:grid;grid-template-rows:auto 1fr auto;padding:calc(var(--S)*.075) calc(var(--S)*.09) calc(var(--S)*.1) calc(var(--S)*.11)}}
.rh{{font-size:calc(var(--S)*.016);letter-spacing:.06em;color:var(--ink2);display:flex;justify-content:space-between;align-items:center;gap:10px;padding-bottom:calc(var(--S)*.018);border-bottom:1px solid var(--line)}}
.rh span{{display:inline-flex;align-items:center;gap:8px}}
.rh span:first-child{{color:var(--c)}}
.folio{{position:absolute;bottom:calc(var(--S)*.035);left:0;right:0;text-align:center;font-family:var(--display);font-size:calc(var(--S)*.017);color:var(--ink2);font-variant-numeric:tabular-nums}}
.mid{{display:flex;flex-direction:column;gap:calc(var(--S)*.024);padding-top:calc(var(--S)*.075)}}
.pg-text h1{{font-family:var(--display);font-weight:300;font-size:calc(var(--S)*.085);line-height:1.02;margin:0}}
.pg-text h2{{font-family:var(--display);font-weight:300;font-size:calc(var(--S)*.1);line-height:1;margin:0}}
.sub{{margin:0;font-family:var(--display);font-weight:300;font-size:calc(var(--S)*.028);line-height:1.55;color:var(--ink2)}}
.tension{{margin:0;font-family:var(--display);font-size:calc(var(--S)*.034);line-height:1.35}}
.tension .lbl{{display:block;font-family:var(--body);font-size:calc(var(--S)*.015);letter-spacing:.12em;color:var(--ink2);margin-bottom:4px}}
.tension mark{{background:linear-gradient(transparent 58%,color-mix(in srgb,var(--c) 26%,transparent) 58%);color:inherit;padding:0 .1em}}
.insight{{margin:0;font-size:calc(var(--S)*.021);line-height:1.75;color:var(--ink2)}}
.insight b{{color:var(--ink);font-weight:600}}
.keys{{display:flex;flex-wrap:wrap;gap:6px 14px;align-items:center}}
.keys i{{display:inline-block;width:12px;height:12px;border-radius:50%;margin-inline-start:6px;vertical-align:middle}}
.k1{{background:conic-gradient(#C0564C,#3F6DB3,#B0852B,#C0564C);box-shadow:0 0 0 2px var(--paper),0 0 0 3px var(--ink)}}
.k2{{background:var(--ink2)}}.k3{{border:1.5px solid #B9B4AA}}
.legend{{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:1fr 1fr;gap:4px 16px;font-size:calc(var(--S)*.019);color:var(--ink)}}
.legend li{{display:flex;align-items:center;gap:8px}}
.src{{margin:0;font-size:calc(var(--S)*.015);color:var(--ink2);line-height:1.6;padding-top:calc(var(--S)*.02);border-top:1px solid var(--line)}}
.haiku{{margin:0;font-family:var(--display);font-weight:300;font-size:calc(var(--S)*.034);line-height:1.55;padding-top:calc(var(--S)*.022);border-top:1px solid var(--line)}}
.toc{{list-style:none;margin:0;padding:calc(var(--S)*.02) 0 0;border-top:1px solid var(--line);display:grid;grid-template-columns:1fr 1fr;gap:2px calc(var(--S)*.03)}}
.toc button{{font:inherit;width:100%;text-align:right;background:none;border:0;cursor:pointer;padding:calc(var(--S)*.005) 0;display:flex;gap:8px;align-items:center;font-family:var(--display);font-size:calc(var(--S)*.023);color:var(--ink)}}
.toc button:hover{{text-decoration:underline;text-decoration-color:#F2E3A0;text-decoration-thickness:3px}}
.toc b{{font-family:var(--body);font-weight:400;font-size:.62em;color:var(--ink2);font-variant-numeric:tabular-nums}}
/* בקרה ופרטיטורה זעירה */
.ctrl{{display:grid;grid-template-columns:auto auto minmax(0,1fr) auto auto;align-items:center;gap:18px;direction:rtl;font-size:14px;color:var(--ink2);width:min(100%,calc(var(--S)*2))}}
.ctrl button.sub2{{font:inherit;min-height:34px;padding:0 12px;border:0;border-radius:4px;background:transparent;color:var(--ink2);cursor:pointer}}
.ctrl button.sub2:hover{{background:var(--paper);color:var(--ink)}}
.ctrl button.sub2:disabled{{opacity:.35;cursor:default}}
.ctrl button.nav{{font:inherit;min-width:104px;min-height:38px;border:0;border-radius:4px;background:var(--paper);color:var(--ink);cursor:pointer;box-shadow:0 1px 3px rgba(0,0,0,.1)}}
.ctrl button.nav:hover{{background:#fff}}
.ctrl button.nav:disabled{{opacity:.35;cursor:default}}
.mini{{display:flex;flex-direction:column;align-items:center;gap:4px;min-width:0;background:none;border:0;cursor:pointer;font:inherit;color:inherit;padding:4px}}
.mini svg{{width:100%;max-width:560px;height:16px;display:block}}
.mini .pos{{font-variant-numeric:tabular-nums}}
.mini .pos b{{color:var(--ink);font-weight:600}}
.mini:hover .pos{{color:var(--ink)}}
.tocover{{font:inherit;color:inherit;background:none;border:0;padding:0;cursor:pointer;position:relative;z-index:26;letter-spacing:inherit}}
.tocover:hover{{color:var(--ink);text-decoration:underline}}
.rh{{position:relative;z-index:26}}
.howto{{margin:0;padding-inline-start:1.2em;display:flex;flex-direction:column;gap:calc(var(--S)*.008);font-size:calc(var(--S)*.019);line-height:1.6;color:var(--ink2)}}
.howto b{{color:var(--ink);font-weight:600}}
.legend-pg{{background:var(--paper);padding:calc(var(--S)*.07) calc(var(--S)*.08)}}
.lg-in{{display:flex;flex-direction:column;gap:calc(var(--S)*.016);height:100%}}
.lg-in h3{{margin:0;font-family:var(--display);font-weight:400;font-size:calc(var(--S)*.026);border-bottom:1px solid var(--line);padding-bottom:4px}}
.lg-in h3 small{{font-family:var(--body);font-size:.55em;color:var(--ink2);font-weight:400}}
.serlist{{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:1fr 1fr;gap:calc(var(--S)*.008) calc(var(--S)*.03)}}
.serlist li{{display:flex;gap:8px;align-items:flex-start;font-size:calc(var(--S)*.016);line-height:1.35}}
.serlist li div{{display:flex;flex-direction:column}}
.serlist b{{font-weight:600}}.serlist span{{color:var(--ink2)}}
.navkeys{{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:1fr 1fr;gap:4px 18px;font-size:calc(var(--S)*.016);color:var(--ink2)}}
kbd{{font-family:var(--body);font-size:.9em;background:#F1EFEA;border-radius:3px;padding:0 5px;color:var(--ink);box-shadow:0 1px 0 #D8D4CC}}
.k4{{border:2px solid var(--ink);background:transparent}}
.hit{{position:absolute;top:0;bottom:0;width:50%;z-index:20;background:none;border:0;cursor:pointer}}
.hit.L{{left:0;cursor:w-resize}}.hit.R{{right:0;cursor:e-resize}}
.side .contact,.side .names,.side .toc,.side .score-pg,.side .pg-cover,.side .legend-pg{{z-index:25}}
.legov .sheet{{display:grid;grid-template-columns:1fr 1fr;width:min(100%,1300px);margin-inline:auto;background:var(--paper);--S:min(760px,calc((100vh - 150px)),calc((100vw - 64px)/2))}}
.legov .sheet>div{{position:relative;min-height:var(--S)}}
/* מפה במסך מלא */
.mapov{{position:fixed;inset:0;z-index:60;background:var(--paper);display:grid;grid-template-rows:auto 1fr auto;padding:20px max(16px,env(safe-area-inset-right,0px)) 16px max(16px,env(safe-area-inset-left,0px))}}
.mapov[hidden],[hidden]{{display:none!important}}
.mapov header{{display:flex;justify-content:space-between;align-items:baseline;gap:16px;flex-wrap:wrap}}
.mapov h2{{margin:0;font-family:var(--display);font-weight:300;font-size:clamp(26px,2.6vw,40px)}}
.mapov p{{margin:0;color:var(--ink2);font-size:14px}}
.mapov .close{{font:inherit;min-height:38px;padding:0 16px;border:0;border-radius:4px;background:var(--ink);color:var(--paper);cursor:pointer}}
.mapov .score-wrap{{align-self:center}}
@media (max-width:820px){{
  :root{{--S:calc(100vw - 44px)}}
  body{{overflow:auto}}
  .book::before{{inset:-5px}}
  .stack{{display:none}}
  .stage{{padding-block:52px 18px;height:auto;min-height:100%}}
  .book{{width:var(--S);height:auto;display:flex;flex-direction:column}}
  .side.L{{position:relative;top:0;border-radius:3px 3px 0 0}}
  .side.R{{position:relative;right:auto;left:0;height:auto;min-height:var(--S);top:auto;border-radius:0 0 3px 3px}}
  .side.L::after,.side.R::after{{display:none}}
  .book.closed::before{{inset:-5px}}
  .book.closed{{transform:none}}
  .book.closed .side.L{{display:none}}
  .book.closed .side.R{{display:block}}
  .contact .grid{{grid-template-rows:none;grid-auto-rows:auto}}
  .cell .ph{{flex:none;aspect-ratio:1/1}}
  .cell small{{font-size:11.5px;padding-top:6px}}
  .contact{{padding:22px 20px 26px}}
  .contact .grid{{gap:16px 12px}}
  .pg-text{{position:relative;inset:auto;min-height:var(--S);padding:22px 20px 44px;gap:0}}
  .rh{{font-size:12px}}.tension .lbl{{font-size:11px}}.folio{{font-size:12px;bottom:14px}}
  .pg-text h1{{font-size:38px}}.pg-text h2{{font-size:40px}}
  .sub{{font-size:16px}}.tension{{font-size:19px}}.insight{{font-size:14.5px}}.haiku{{font-size:19px;margin-top:20px}}
  .toc button{{font-size:16px}}.all{{font-size:14px}}.legend{{font-size:13px}}.src{{font-size:11px;margin-top:14px}}
  .mid{{padding-block:22px}}
  .hit{{display:none}}
  .score{{min-width:640px}}
  .score-pg{{place-items:start;padding:10px}}
  .score-pg .score-wrap{{max-height:100%;overflow:auto}}
  .mapov .score{{min-width:1100px}}
  .mapov .score-wrap{{overflow:auto;max-height:100%}}
  .ctrl{{gap:6px;grid-template-columns:auto auto minmax(0,1fr) auto auto;position:fixed;bottom:0;left:0;right:0;width:auto;z-index:40;background:color-mix(in srgb,var(--desk) 94%,transparent);backdrop-filter:blur(6px);box-shadow:0 -1px 0 rgba(0,0,0,.08);padding:8px max(10px,env(safe-area-inset-right,0px)) calc(8px + env(safe-area-inset-bottom,0px)) max(10px,env(safe-area-inset-left,0px))}}
  .stage{{padding-bottom:96px}}.ctrl button.nav{{min-width:64px}}.ctrl button.sub2{{padding:0 6px;font-size:13px}}
  .legov .sheet{{grid-template-columns:1fr;--S:calc(100vw - 32px)}}
  .legend-pg{{position:relative}}
  .side.L:has(.legend-pg){{height:auto}}
  .side.L .legend-pg{{position:relative;inset:auto}}.serlist,.navkeys{{grid-template-columns:1fr}}.serlist li,.navkeys,.howto{{font-size:13.5px}}.lg-in h3{{font-size:18px}}
  .book.turn{{animation:turn .45s ease}}
}}
@keyframes turn{{0%{{opacity:1;transform:none}}45%{{opacity:0;transform:translateX(var(--dx,-24px))}}55%{{opacity:0;transform:translateX(calc(var(--dx,-24px)*-1))}}100%{{opacity:1;transform:none}}}}
@media (prefers-reduced-motion:reduce){{.leaf{{transition:none}}.book.turn{{animation:none}}}}
</style>
<div class="stage">
  <div class="book closed" id="book" aria-live="polite">
    <div class="stack L"></div><div class="stack R"></div>
    <div class="side L" id="sideL"></div>
    <div class="side R" id="sideR"></div>
    <button class="hit L" id="hitL" aria-label="העמוד הבא"></button>
    <button class="hit R" id="hitR" aria-label="העמוד הקודם"></button>
  </div>
  <nav class="ctrl" aria-label="דפדוף">
    <button class="nav" id="prev">הקודם</button>
    <button class="sub2" id="toCover">לכריכה</button>
    <button class="mini" id="mini" title="פתיחת מפת הספר"><svg id="miniSvg" viewBox="0 0 560 16" preserveAspectRatio="none" aria-hidden="true"></svg><span class="pos" id="pos"></span></button>
    <button class="sub2" id="legBtn">מקרא</button>
    <button class="nav" id="next">הבא</button>
  </nav>
</div>
<div class="mapov" id="mapov" hidden>
  <header><div><h2>מפת הספר</h2><p>סדר הקריאה מימין לשמאל, שורה לכל סדרה, וקו אנכי בין הפרקים. לחיצה על תמונה פותחת את העיר.</p></div><button class="close" id="closeMap">סגירה</button></header>
  <div class="score-wrap"><svg class="score" id="bigScore" data-big="1"></svg></div>
  <p id="mapNote"></p>
</div>
<div class="mapov legov" id="legov" hidden>
  <header><div><h2>מקרא</h2><p>איך לקרוא את הספר, את המפה ואת הסימנים.</p></div><button class="close" id="closeLeg">סגירה</button></header>
  <div class="score-wrap"><div class="sheet" id="legSheet"></div></div>
  <p></p>
</div>
{tpl}
<script>
var SD={SDATA};
(function(){{
  var T=[].slice.call(document.querySelectorAll('template')), n=T.length, i=0, busy=false, pending=null, flying=0, FC={FIRST_CITY}, LEG=FC-1;
  var L=document.getElementById('sideL'), R=document.getElementById('sideR'), book=document.getElementById('book');
  var NS='http://www.w3.org/2000/svg';
  function part(k,side){{return T[k].content.querySelector('.'+side).innerHTML;}}
  function cityAt(k){{for(var j=0;j<SD.cities.length;j++)if(SD.cities[j].sp===k)return SD.cities[j];return null;}}
  /* הפרטיטורה: 55 עמודות לפי סדר הקריאה מימין לשמאל, 11 שורות */
  function score(svg,big){{
    var W=big?1500:1000, padR=big?205:175, padL=20, top=big?44:34, rh=big?52:58, H=top+rh*11+12;
    svg.setAttribute('viewBox','0 0 '+W+' '+H); svg.innerHTML='';
    var gap=big?14:10, usable=W-padR-padL-gap*8, step=usable/55;
    function X(c){{return W-padR-(c.p-0.5)*step-(c.c-1)*gap;}}
    var cur=cityAt(i), out='';
    for(var s=0;s<11;s++){{var y=top+rh*s+rh/2, col=SD.ser[s][1];
      out+='<line x1="'+padL+'" x2="'+(W-padR+6)+'" y1="'+y+'" y2="'+y+'" stroke="'+col+'" stroke-opacity=".28" stroke-width="1"/>';
      out+='<g transform="translate('+(W-28)+','+(y-11)+') scale(.92)" fill="none" stroke="'+col+'" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round">'+SD.ser[s][2]+'</g>';
      out+='<text x="'+(W-36)+'" y="'+(y+5)+'" font-family="Assistant,Arial" font-size="'+(big?16:15)+'" fill="'+col+'" direction="rtl" text-anchor="start">'+SD.ser[s][0]+'</text>';}}
    for(var c=1;c<=9;c++){{var cs=SD.cities.filter(function(q){{return q.c===c;}}), xr=X(cs[0])+step/2+gap/2, xl=X(cs[cs.length-1])-step/2-gap/2;
      out+='<text x="'+((xr+xl)/2)+'" y="'+(top-14)+'" font-family="Assistant,Arial" font-size="'+(big?14:13)+'" fill="#7A776F" text-anchor="middle">פרק '+c+'</text>';
      if(c>1)out+='<line x1="'+(xr)+'" x2="'+(xr)+'" y1="'+(top-6)+'" y2="'+(H-8)+'" stroke="#2E2E2B" stroke-opacity=".18"/>';}}
    svg.insertAdjacentHTML('beforeend',out);
    SD.cities.forEach(function(q){{var x=X(q), y=top+rh*q.s+rh/2, col=SD.ser[q.s][1], r=Math.min(step*.62,big?14:11), g=document.createElementNS(NS,'g');
      var tip=q.h+' · '+SD.ser[q.s][0]+' '+q.n+' · פרק '+q.c+(q.t?' · '+q.t:'')+(q.sp<0?(q.f?' · עוד בלי תמונה':' · לא בקובץ'):'');
      var h='<title>'+tip+'</title>';
      if(q.sp>=0){{var id='cl'+(big?'b':'s')+q.p;
        h+='<clipPath id="'+id+'"><circle cx="'+x+'" cy="'+y+'" r="'+r+'"/></clipPath><image href="'+SD.th[q.h]+'" x="'+(x-r)+'" y="'+(y-r)+'" width="'+(2*r)+'" height="'+(2*r)+'" clip-path="url(#'+id+')" preserveAspectRatio="xMidYMid slice"/><circle class="o" cx="'+x+'" cy="'+y+'" r="'+r+'" fill="none" stroke="'+col+'" stroke-width="1.6"/>';
        g.setAttribute('class','note'); g.dataset.to=q.sp;}}
      else if(q.f) h+='<circle cx="'+x+'" cy="'+y+'" r="'+(r*.42)+'" fill="'+col+'" fill-opacity=".75"/>';
      else h+='<circle cx="'+x+'" cy="'+y+'" r="'+(r*.42)+'" fill="#FBFAF7" stroke="#B9B4AA" stroke-width="1.3"/>';
      if(cur&&cur.p===q.p) h+='<circle cx="'+x+'" cy="'+y+'" r="'+(r+5)+'" fill="none" stroke="#2E2E2B" stroke-width="2"/>';
      if(big) h+='<text x="'+x+'" y="'+(y+r+(q.p%2?13:25))+'" font-family="Assistant,Arial" font-size="10.5" fill="'+(q.f?'#2E2E2B':'#9A958B')+'" text-anchor="middle">'+q.h+'</text>';
      g.innerHTML=h; svg.appendChild(g);}});
  }}
  function mini(){{
    var svg=document.getElementById('miniSvg'), W=560, out='', cur=cityAt(i);
    SD.cities.forEach(function(q){{var x=W-6-(q.p-1)*((W-12-8*6)/54)-(q.c-1)*6, col=SD.ser[q.s][1];
      out+=q.sp>=0?'<rect x="'+(x-3)+'" y="4" width="6" height="8" rx="1.5" fill="'+col+'"/>':'<rect x="'+(x-1)+'" y="6" width="2" height="4" fill="'+col+'" fill-opacity="'+(q.f?.55:.22)+'"/>';
      if(cur&&cur.p===q.p)out+='<rect x="'+(x-4.5)+'" y="1" width="9" height="14" rx="2" fill="none" stroke="#2E2E2B" stroke-width="1.5"/>';}});
    svg.innerHTML=out;
  }}
  function show(k){{
    L.innerHTML=part(k,'L'); R.innerHTML=part(k,'R'); i=k; book.classList.toggle('closed',k===0);
    book.classList.remove('textout'); book.classList.add('textin'); setTimeout(function(){{book.classList.remove('textin');}},260);
    var sc=L.querySelector('svg.score'); if(sc) score(sc,false);
    var f=n>1?k/(n-1):0; book.style.setProperty('--tr',(2+f*10)+'px'); book.style.setProperty('--tl',(2+(1-f)*10)+'px');
    ui(); mini();
  }}
  function ui(){{
    document.getElementById('prev').disabled=i===0; document.getElementById('next').disabled=i===n-1; document.getElementById('toCover').disabled=i===0;
    var nm=T[i].dataset.name, c=cityAt(i);
    document.getElementById('pos').innerHTML = c ? '<b>'+nm+'</b> · '+SD.ser[c.s][0]+' '+c.n+' · '+(i-FC+1)+' מתוך '+(n-FC-1) : '<b>'+nm+'</b>';
  }}
  var narrow=function(){{return matchMedia('(max-width:820px)').matches;}};
  var reduce=matchMedia('(prefers-reduced-motion: reduce)').matches;
  function go(k){{
    if(k<0||k>=n) return;
    if(busy){{pending=k;return;}}
    if(k===i) return;
    flying=k;
    if(reduce){{show(k);return;}}
    // ספר עברי: קדימה, הישן יוצא ימינה והחדש נכנס משמאל
    if(narrow()){{busy=true;book.style.setProperty('--dx',k>i?'24px':'-24px');book.classList.remove('turn');void book.offsetWidth;book.classList.add('turn');setTimeout(function(){{show(k);}},200);setTimeout(done,460);return;}}
    busy=true; var fwd=k>i;
    // קודם הטקסט יורד, ורק אחר כך הדף נהפך. כך אין טקסט על דף שזז
    book.classList.add('textout');
    setTimeout(function(){{
      // פתיחת הכריכה: קודם הספר נע למרכז, ורק אז הכריכה מתהפכת
      if(fwd&&i===0&&book.classList.contains('closed')){{book.classList.remove('closed');setTimeout(function(){{flip(k,true);}},440);return;}}
      flip(k,fwd);
    }},160);
  }}
  function base(){{return pending!==null?pending:(busy?flying:i);}}
  function done(){{busy=false;if(pending!==null){{var t=pending;pending=null;if(t!==i)go(t);}}}}
  function hyd(el){{el.querySelectorAll('svg.score').forEach(function(x){{score(x,false);}});}}
  function flip(k,fwd){{
    var leaf=document.createElement('div');
    leaf.className='leaf '+(fwd?'fwd':'back');
    // ספר עברי. קדימה: העמוד הימני (טקסט) נהפך אל השמאל, וגבו הוא הוויזואל של העמוד הבא.
    // אחורה: העמוד השמאלי (ויזואל) נהפך אל הימין, וגבו הוא הטקסט של העמוד הקודם.
    if(fwd){{
      leaf.innerHTML='<div class="face f">'+part(i,'R')+'</div><div class="face b">'+part(k,'L')+'</div>';
      R.innerHTML=part(k,'R');
    }} else {{
      leaf.innerHTML='<div class="face f">'+part(i,'L')+'</div><div class="face b">'+part(k,'R')+'</div>';
      L.innerHTML=part(k,'L');
    }}
    book.appendChild(leaf); hyd(leaf); hyd(L); hyd(R);
    requestAnimationFrame(function(){{requestAnimationFrame(function(){{leaf.style.transform='rotateY('+(fwd?-180:180)+'deg)';}});}});
    setTimeout(function(){{show(k);leaf.remove();done();}},940);
  }}
  var ov=document.getElementById('mapov');
  function openMap(){{score(document.getElementById('bigScore'),true);var inB=SD.cities.filter(function(q){{return q.sp>=0;}}).length,inF=SD.cities.filter(function(q){{return q.f;}}).length;
    document.getElementById('mapNote').textContent=inB+' ערים כבר בספר, '+(inF-inB)+' בקובץ ועוד בלי תמונה, ו-'+(55-inF)+' לא בקובץ.';ov.hidden=false;document.getElementById('closeMap').focus();}}
  function closeMap(){{ov.hidden=true;}}
  var lov=document.getElementById('legov');
  function openLeg(){{document.getElementById('legSheet').innerHTML='<div>'+part(LEG,'R')+'</div><div>'+part(LEG,'L')+'</div>';lov.hidden=false;document.getElementById('closeLeg').focus();}}
  function closeLeg(){{lov.hidden=true;}}
  document.getElementById('legBtn').onclick=openLeg;
  document.getElementById('closeLeg').onclick=closeLeg;
  lov.addEventListener('click',function(ev){{var t=ev.target.closest('[data-to]');if(t){{closeLeg();go(+t.dataset.to);}}}});
  document.getElementById('toCover').onclick=function(){{go(0);}};
  document.getElementById('mini').onclick=openMap;
  document.getElementById('closeMap').onclick=closeMap;
  ov.addEventListener('click',function(ev){{var t=ev.target.closest('[data-to]');if(t){{closeMap();go(+t.dataset.to);}}}});
  document.getElementById('next').onclick=function(){{go(base()+1);}};
  document.getElementById('prev').onclick=function(){{go(base()-1);}};
  document.getElementById('hitL').onclick=function(){{go(base()+1);}};
  document.getElementById('hitR').onclick=function(){{go(base()-1);}};
  book.addEventListener('click',function(ev){{var t=ev.target.closest('[data-to]');if(t){{ev.stopPropagation();go(+t.dataset.to);return;}}if(ev.target.closest('.pg-cover')){{ev.stopPropagation();go(1);}}}},true);
  document.addEventListener('keydown',function(ev){{if(!ov.hidden){{if(ev.key==='Escape')closeMap();return;}}if(!lov.hidden){{if(ev.key==='Escape')closeLeg();return;}}
    // מקש רווח או אנטר על כפתור מפעילים את הכפתור עצמו, ולא דפדוף נוסף
    if((ev.key===' '||ev.key==='Enter')&&ev.target.closest&&ev.target.closest('button'))return;
    if(ev.key==='?'){{openLeg();return;}}
    if(ev.key==='ArrowLeft'||ev.key==='PageDown'||ev.key===' '){{ev.preventDefault();go(base()+1);}}if(ev.key==='ArrowRight'||ev.key==='PageUp'){{ev.preventDefault();go(base()-1);}}if(ev.key==='Home')go(0);if(ev.key==='End')go(n-1);if(ev.key==='m'||ev.key==='M')openMap();}});
  var sx=null;book.addEventListener('touchstart',function(ev){{sx=ev.touches[0].clientX;}},{{passive:true}});
  book.addEventListener('touchend',function(ev){{if(sx===null)return;var dx=ev.changedTouches[0].clientX-sx;if(Math.abs(dx)>40)go(dx>0?i+1:i-1);sx=null;}});
  try{{if(location.hash)history.replaceState(null,'',location.pathname+location.search);}}catch(e){{}}
  show(0);
}})();
</script>
'''
open(os.path.join(HERE, 'book.html'), 'w', encoding='utf8').write(doc)
# גרסה לאתר (Vercel): מסמך מלא, וכפתור חזרה לאפליקציה
site = doc.replace('<div class="stage">', '<a class="back" href="lab/">מעבדת ההמחשה</a>\n<div class="stage">', 1)
site = site.replace('</style>', '.back{position:fixed;top:12px;left:max(16px,env(safe-area-inset-left,0px));z-index:50;font-size:13px;color:var(--ink);text-decoration:none;background:var(--paper);padding:6px 12px;border-radius:4px;box-shadow:0 1px 3px rgba(0,0,0,.1)}\n</style>', 1)
open(os.path.join(HERE, '..', 'index.html'), 'w', encoding='utf8').write('<!doctype html>\n<html lang="he" dir="rtl">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n</head>\n<body>\n' + site + '\n</body>\n</html>\n')
print('spreads', len(spreads), 'bytes', len(doc))
