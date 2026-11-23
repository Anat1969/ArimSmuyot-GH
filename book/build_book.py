# בונה את "ספר הערים הסמויות": עמוד לכל עיר, תמונה אחת, מתח, תובנה והייקו.
import base64, json, os, sys, html
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
]
PAGES = [p for p in PAGES if os.path.exists(os.path.join(HERE, p['img']))]
ALL = [c['n'] for c in json.load(open(sys.argv[1], encoding='utf8'))]
def uri(f): return 'data:image/jpeg;base64,' + base64.b64encode(open(os.path.join(HERE, f), 'rb').read()).decode()
e = html.escape
done = {p['n'] for p in PAGES}
pages = ''
for k, p in enumerate(PAGES):
    pages += f'''
<section class="leaf" id="{p['id']}" aria-label="{e(p['n'])}">
  <div class="words">
    <div class="eyebrow"><span>{k+1:02d}</span>{e(p['cat'])}</div>
    <div class="mid">
      <h2>{e(p['n'])}</h2>
      <p class="tension"><span class="lbl">המתח</span><mark>{e(p['t'])}</mark></p>
      <p class="insight">{e(p['i'])}</p>
    </div>
    <p class="haiku">{'<br>'.join(e(x) for x in p['h'])}</p>
  </div>
  <figure class="plate"><img src="{uri(p['img'])}" alt="{e(p['n'])}: {e(p['t'])}" loading="lazy"></figure>
</section>'''
index = ''.join(f'<a href="#{[q for q in PAGES if q["n"]==n][0]["id"]}" class="on">{e(n)}</a>' if n in done else f'<span>{e(n)}</span>' for n in ALL)
toc = ''.join(f'<a href="#{p["id"]}"><img class="th" data-for="{p["id"]}" alt=""><b>{k+1:02d}</b>{e(p["n"])}<small>{e(p["t"])}</small></a>' for k, p in enumerate(PAGES))
doc = f'''<title>ספר הערים הסמויות</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Frank+Ruhl+Libre:wght@300;400;500&family=Assistant:wght@300;400;600&display=swap">
<style>
/* פריסה: ספר בעמודים. כל עיר היא עמוד בגובה המסך: תמונה ריבועית גדולה ביחס זהוב מול טור מילים, והצדדים מתחלפים. עולם בהיר אחד, בכוונה */
:root{{color-scheme:light;--paper:#FBFBF9;--ink:#2E2E2B;--ink2:#7A776F;--line:#E6E4DE;--marker:#F2E3A0;
  --display:'Frank Ruhl Libre',Georgia,serif;--body:'Assistant','Segoe UI',Arial,sans-serif}}
*{{box-sizing:border-box}}
html{{scroll-behavior:smooth}}
body{{margin:0;background:var(--paper);color:var(--ink);font-family:var(--body);direction:rtl}}
.pad{{padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px))}}
.title{{min-height:92vh;display:grid;place-items:center;text-align:center;padding-block:8vh}}
.title .in{{max-width:1100px;display:flex;flex-direction:column;gap:18px;align-items:center}}
.title .kick{{font-size:13px;letter-spacing:.18em;color:var(--ink2)}}
.title h1{{font-family:var(--display);font-weight:300;font-size:clamp(46px,7vw,104px);line-height:1;margin:0;text-wrap:balance}}
.title p{{font-family:var(--display);font-weight:300;font-size:clamp(18px,1.6vw,24px);line-height:1.6;margin:0;color:var(--ink2);text-wrap:balance}}
.toc{{display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:14px;width:min(1100px,92vw)}}
.toc a{{color:inherit;text-decoration:none;display:flex;flex-direction:column;text-align:right;gap:2px}}
.toc .th{{width:100%;aspect-ratio:1/1;object-fit:cover;display:block;margin-bottom:8px;box-shadow:0 10px 24px rgba(30,28,24,.16);transition:box-shadow .25s,filter .25s}}
.toc a:hover .th{{box-shadow:0 16px 36px rgba(30,28,24,.28);filter:brightness(1.06)}}
@media (max-width:700px){{.toc{{grid-template-columns:repeat(2,minmax(0,1fr))}}}}
.toc b{{font-weight:400;font-size:12px;color:var(--ink2);font-variant-numeric:tabular-nums}}
.toc a{{font-family:var(--display);font-size:20px}}
.toc small{{font-family:var(--body);font-size:12px;color:var(--ink2)}}
.leaf{{--S:min(78vh,56vw);min-height:100vh;display:grid;grid-template-columns:minmax(0,1fr) var(--S);gap:clamp(32px,5vw,96px);align-content:center;max-width:1640px;margin-inline:auto;padding-block:6vh;border-top:1px solid var(--line)}}
.plate{{margin:0;width:var(--S);height:var(--S)}}
.plate img{{display:block;width:100%;height:100%;object-fit:cover;box-shadow:0 24px 60px rgba(30,28,24,.18)}}
.words{{min-width:0;height:var(--S);display:grid;grid-template-rows:auto 1fr auto;padding-inline-start:clamp(0px,2vw,40px)}}
.eyebrow{{font-size:13px;letter-spacing:.08em;color:var(--ink2);display:flex;gap:12px;align-items:baseline;padding-bottom:14px;border-bottom:1px solid var(--line)}}
.eyebrow span{{font-variant-numeric:tabular-nums;color:var(--ink)}}
.mid{{display:flex;flex-direction:column;gap:20px;padding-top:clamp(28px,7vh,80px);max-width:28em}}
.words h2{{font-family:var(--display);font-weight:300;font-size:clamp(46px,5vw,84px);line-height:1;margin:0}}
.tension{{margin:0;font-family:var(--display);font-weight:400;font-size:clamp(20px,1.7vw,28px);line-height:1.35}}
.tension .lbl{{display:block;font-family:var(--body);font-size:12px;letter-spacing:.12em;color:var(--ink2);font-weight:400;margin-bottom:4px}}
.tension mark{{background:linear-gradient(transparent 58%,var(--marker) 58%);color:inherit;padding:0 .1em}}
.insight{{margin:0;font-size:clamp(15px,1.05vw,17px);line-height:1.75;color:var(--ink2)}}
.haiku{{margin:0;font-family:var(--display);font-weight:300;font-size:clamp(21px,1.8vw,29px);line-height:1.55;padding-top:18px;border-top:1px solid var(--line)}}
.end{{border-top:1px solid var(--line);padding-block:10vh;text-align:center}}
.end h3{{font-family:var(--display);font-weight:300;font-size:clamp(26px,2.6vw,38px);margin:0 0 8px}}
.end p{{margin:0 0 22px;color:var(--ink2)}}
.all{{display:flex;flex-wrap:wrap;justify-content:center;gap:6px 14px;max-width:1100px;margin-inline:auto;font-family:var(--display);font-size:18px}}
.all span{{color:#C9C6BE}}
.all a{{color:var(--ink);text-decoration:none;border-bottom:2px solid var(--marker)}}
@media (max-width:860px){{
  .leaf{{--S:100%;grid-template-columns:1fr;min-height:0;padding-block:40px}}
  .plate{{order:-1;height:auto;aspect-ratio:1/1}}
  .words{{height:auto;padding-inline-start:0;gap:0}}
  .mid{{padding-block:24px}}
}}
@media (prefers-reduced-motion:reduce){{html{{scroll-behavior:auto}}}}
</style>
<header class="title pad"><div class="in">
  <div class="kick">איטלו קאלווינו · ערים סמויות</div>
  <h1>ספר הערים הסמויות</h1>
  <p>כל עיר היא מתח אחד. התמונה מחזיקה אותו, וההייקו משאיר אותו פתוח.</p>
  <nav class="toc" aria-label="תוכן">{toc}</nav>
</div></header>
<main class="pad">{pages}
<section class="end"><h3>{len(PAGES)} ערים מתוך {len(ALL)}</h3><p>הערים המסומנות כבר בספר. השאר עוד מחכות לתמונה שלהן.</p><div class="all">{index}</div></section>
</main>
<script>document.querySelectorAll('.th').forEach(function(t){{var s=document.querySelector('#'+t.dataset.for+' .plate img');if(s)t.src=s.src;}});</script>
'''
open(os.path.join(HERE, 'book.html'), 'w', encoding='utf8').write(doc)
# גרסה לאתר (Vercel): מסמך מלא, וכפתור חזרה לאפליקציה
site = doc.replace('<header class="title pad">', '<a class="back" href="../">לאפליקציה</a>\n<header class="title pad">', 1)
site = site.replace('</style>', '.back{position:fixed;top:14px;left:max(16px,env(safe-area-inset-left,0px));z-index:5;font-size:14px;color:var(--ink);text-decoration:none;background:#F1F0EC;padding:8px 14px;border-radius:4px;box-shadow:0 1px 3px rgba(0,0,0,.08)}.back:hover{background:var(--line)}\n</style>', 1)
open(os.path.join(HERE, 'index.html'), 'w', encoding='utf8').write('<!doctype html>\n<html lang="he" dir="rtl">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n</head>\n<body>\n' + site + '\n</body>\n</html>\n')
print('pages', len(PAGES), 'bytes', len(doc))
