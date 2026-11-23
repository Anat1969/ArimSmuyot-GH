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
def thumb(f):
    import io
    from PIL import Image
    b=io.BytesIO(); Image.open(os.path.join(HERE,f)).convert('RGB').resize((360,360),Image.LANCZOS).save(b,'JPEG',quality=78,optimize=True)
    return 'data:image/jpeg;base64,'+base64.b64encode(b.getvalue()).decode()
def uri(f): return 'data:image/jpeg;base64,' + base64.b64encode(open(os.path.join(HERE, f), 'rb').read()).decode()
e = html.escape
done = {p['n'] for p in PAGES}
N = len(PAGES)
# כל כפולה: עמוד ימין (טקסט) ועמוד שמאל (תמונה). הכריכה בהתחלה, עמוד הסיום בסוף.
spreads = []
toc = ''.join(f'<li><button data-to="{k+1}"><b>{k+1:02d}</b>{e(p["n"])}<small>{e(p["t"])}</small></button></li>' for k, p in enumerate(PAGES))
mosaic = ''.join(f'<button data-to="{k+1}" aria-label="{e(p["n"])}"><img src="{thumb(p["img"])}" alt=""></button>' for k, p in enumerate(PAGES))
spreads.append((f'''<div class="pg-text cover-r">
  <div class="eyebrow"><span></span>איטלו קאלווינו · ערים סמויות</div>
  <div class="mid"><h1>ספר הערים הסמויות</h1><p class="sub">כל עיר היא מתח אחד. התמונה מחזיקה אותו, וההייקו משאיר אותו פתוח.</p></div>
  <ol class="toc">{toc}</ol>
</div>''', f'<div class="pg-img mosaic n{min(N,9)}">{mosaic}</div>', 'כריכה'))
for k, p in enumerate(PAGES):
    spreads.append((f'''<div class="pg-text">
  <div class="eyebrow"><span>{k+1:02d}</span>{e(p['cat'])}</div>
  <div class="mid">
    <h2>{e(p['n'])}</h2>
    <p class="tension"><span class="lbl">המתח</span><mark>{e(p['t'])}</mark></p>
    <p class="insight">{e(p['i'])}</p>
  </div>
  <p class="haiku">{'<br>'.join(e(x) for x in p['h'])}</p>
</div>''', f'<div class="pg-img"><img src="{uri(p["img"])}" alt="{e(p["n"])}: {e(p["t"])}"></div>', p['n']))
allnames = ''.join(f'<button data-to="{[i for i,q in enumerate(PAGES) if q["n"]==n][0]+1}" class="on">{e(n)}</button>' if n in done else f'<span>{e(n)}</span>' for n in ALL)
spreads.append((f'''<div class="pg-text">
  <div class="eyebrow"><span></span>סוף הכרך הראשון</div>
  <div class="mid"><h2>{N} מתוך {len(ALL)}</h2><p class="insight">הערים המודגשות כבר בספר. השאר עוד מחכות לתמונה שלהן, ולמתח שיחזיק אותה.</p></div>
  <p class="haiku">עיר אחת נגמרת<br>כדי שתיפתח אחרת<br>בדף שעוד לבן</p>
</div>''', f'<div class="pg-img names"><div class="all">{allnames}</div></div>', 'סוף'))
tpl = ''.join(f'<template data-name="{e(nm)}"><div class="R">{r}</div><div class="L">{l}</div></template>' for r, l, nm in spreads)

doc = f'''<title>ספר הערים הסמויות</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Frank+Ruhl+Libre:wght@300;400;500&family=Assistant:wght@300;400;600&display=swap">
<style>
/* פריסה: ספר פתוח במרכז המסך. עמוד ימין טקסט, עמוד שמאל תמונה, שדרה באמצע, ודפדוף תלת־ממדי סביב השדרה. הכול נמדד ביחס לגודל העמוד S. עולם בהיר אחד, בכוונה */
:root{{color-scheme:light;--desk:#E7E5E0;--paper:#FBFAF7;--ink:#2E2E2B;--ink2:#7A776F;--line:#E4E1DA;--marker:#F2E3A0;
  --display:'Frank Ruhl Libre',Georgia,serif;--body:'Assistant','Segoe UI',Arial,sans-serif;
  --S:min(calc(100vh - 150px),calc((100vw - 64px)/2),860px)}}
*{{box-sizing:border-box}}
html,body{{height:100%}}
body{{margin:0;background:var(--desk);color:var(--ink);font-family:var(--body);direction:rtl;overflow:hidden;
  padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px))}}
.stage{{height:100%;display:grid;grid-template-columns:minmax(0,1fr);grid-template-rows:1fr auto;place-items:center;gap:14px;padding-block:24px 18px}}
.book{{position:relative;width:calc(var(--S)*2);height:var(--S);perspective:calc(var(--S)*5);direction:ltr}}
.book::before{{content:"";position:absolute;inset:-10px -12px;border-radius:6px;background:#D8D4CC;box-shadow:0 40px 80px rgba(40,34,24,.25)}}
.side{{position:absolute;top:0;width:var(--S);height:var(--S);background:var(--paper);overflow:hidden}}
.side.L{{left:0;border-radius:3px 0 0 3px}}
.side.R{{right:0;border-radius:0 3px 3px 0}}
.side.L::after,.side.R::after,.face::after{{content:"";position:absolute;top:0;bottom:0;width:14%;pointer-events:none;z-index:3}}
.side.L::after{{right:0;background:linear-gradient(to left,rgba(40,32,20,.22),rgba(40,32,20,0))}}
.side.R::after{{left:0;background:linear-gradient(to right,rgba(40,32,20,.16),rgba(40,32,20,0))}}
.leaf{{position:absolute;top:0;width:var(--S);height:var(--S);transform-style:preserve-3d;z-index:10;transition:transform .9s cubic-bezier(.45,.05,.25,1)}}
.leaf.fwd{{left:0;transform-origin:right center}}
.leaf.back{{right:0;transform-origin:left center}}
.face{{position:absolute;inset:0;backface-visibility:hidden;background:var(--paper);overflow:hidden}}
.face.b{{transform:rotateY(180deg)}}
.leaf.fwd .face.f::after{{right:0;background:linear-gradient(to left,rgba(40,32,20,.22),rgba(40,32,20,0))}}
.leaf.fwd .face.b::after{{left:0;background:linear-gradient(to right,rgba(40,32,20,.16),rgba(40,32,20,0))}}
.leaf.back .face.f::after{{left:0;background:linear-gradient(to right,rgba(40,32,20,.16),rgba(40,32,20,0))}}
.leaf.back .face.b::after{{right:0;background:linear-gradient(to left,rgba(40,32,20,.22),rgba(40,32,20,0))}}
/* עמוד תמונה */
.pg-img{{position:absolute;inset:0;direction:rtl}}
.pg-img>img{{width:100%;height:100%;object-fit:cover;display:block}}
.mosaic{{display:grid;gap:4px;padding:calc(var(--S)*.06);background:var(--paper)}}
.mosaic.n9,.mosaic.n8,.mosaic.n7,.mosaic.n6,.mosaic.n5{{grid-template-columns:repeat(3,1fr)}}
.mosaic.n4,.mosaic.n3,.mosaic.n2,.mosaic.n1{{grid-template-columns:repeat(2,1fr)}}
.mosaic button{{padding:0;border:0;cursor:pointer;overflow:hidden;aspect-ratio:1/1;background:#ddd}}
.mosaic img{{width:100%;height:100%;object-fit:cover;display:block;transition:transform .5s}}
.mosaic button:hover img{{transform:scale(1.05)}}
.names{{display:grid;place-items:center;padding:calc(var(--S)*.1);background:var(--paper)}}
.all{{display:flex;flex-wrap:wrap;justify-content:center;gap:calc(var(--S)*.012) calc(var(--S)*.024);font-family:var(--display);font-size:calc(var(--S)*.026)}}
.all span{{color:#C8C4BB}}
.all button{{font:inherit;color:var(--ink);background:none;border:0;padding:0;cursor:pointer;border-bottom:2px solid var(--marker)}}
/* עמוד טקסט: אותו גריד בכל עמוד */
.pg-text{{position:absolute;inset:0;direction:rtl;display:grid;grid-template-rows:auto 1fr auto;padding:calc(var(--S)*.08) calc(var(--S)*.09) calc(var(--S)*.08) calc(var(--S)*.11)}}
.eyebrow{{font-size:calc(var(--S)*.017);letter-spacing:.08em;color:var(--ink2);display:flex;gap:12px;align-items:baseline;padding-bottom:calc(var(--S)*.02);border-bottom:1px solid var(--line)}}
.eyebrow span{{font-variant-numeric:tabular-nums;color:var(--ink)}}
.mid{{display:flex;flex-direction:column;gap:calc(var(--S)*.026);padding-top:calc(var(--S)*.08)}}
.pg-text h1{{font-family:var(--display);font-weight:300;font-size:calc(var(--S)*.085);line-height:1.02;margin:0}}
.pg-text h2{{font-family:var(--display);font-weight:300;font-size:calc(var(--S)*.1);line-height:1;margin:0}}
.sub{{margin:0;font-family:var(--display);font-weight:300;font-size:calc(var(--S)*.028);line-height:1.55;color:var(--ink2)}}
.tension{{margin:0;font-family:var(--display);font-size:calc(var(--S)*.034);line-height:1.35}}
.tension .lbl{{display:block;font-family:var(--body);font-size:calc(var(--S)*.015);letter-spacing:.12em;color:var(--ink2);margin-bottom:4px}}
.tension mark{{background:linear-gradient(transparent 58%,var(--marker) 58%);color:inherit;padding:0 .1em}}
.insight{{margin:0;font-size:calc(var(--S)*.021);line-height:1.75;color:var(--ink2)}}
.haiku{{margin:0;font-family:var(--display);font-weight:300;font-size:calc(var(--S)*.034);line-height:1.55;padding-top:calc(var(--S)*.022);border-top:1px solid var(--line)}}
.toc{{list-style:none;margin:0;padding:calc(var(--S)*.02) 0 0;border-top:1px solid var(--line);display:grid;grid-template-columns:1fr 1fr;gap:2px calc(var(--S)*.03)}}
.toc button{{font:inherit;width:100%;text-align:right;background:none;border:0;cursor:pointer;padding:calc(var(--S)*.006) 0;display:flex;gap:8px;align-items:baseline;font-family:var(--display);font-size:calc(var(--S)*.024);color:var(--ink)}}
.toc button:hover{{color:#000;text-decoration:underline;text-decoration-color:var(--marker);text-decoration-thickness:3px}}
.toc b{{font-family:var(--body);font-weight:400;font-size:.62em;color:var(--ink2);font-variant-numeric:tabular-nums}}
.toc small{{display:none}}
/* בקרה */
.ctrl{{display:flex;align-items:center;gap:18px;direction:rtl;font-size:14px;color:var(--ink2)}}
.ctrl button{{font:inherit;min-width:110px;min-height:38px;border:0;border-radius:4px;background:var(--paper);color:var(--ink);cursor:pointer;box-shadow:0 1px 3px rgba(0,0,0,.1)}}
.ctrl button:hover{{background:#fff}}
.ctrl button:disabled{{opacity:.35;cursor:default}}
.ctrl .pos{{min-width:150px;text-align:center;font-variant-numeric:tabular-nums}}
.ctrl .pos b{{color:var(--ink);font-weight:600}}
.hit{{position:absolute;top:0;bottom:0;width:50%;z-index:20;background:none;border:0;cursor:pointer}}
.hit.L{{left:0;cursor:w-resize}}.hit.R{{right:0;cursor:e-resize}}
.side .mosaic,.side .names,.side .toc{{position:relative;z-index:25}}
.side .pg-img.mosaic,.side .pg-img.names{{position:absolute}}
@media (max-width:820px){{
  :root{{--S:calc(100vw - 44px)}}
  .book::before{{inset:-5px}}
  .stage{{padding-block:52px 18px;height:auto;min-height:100%}}
  .side.R{{height:auto;min-height:var(--S);position:relative;top:auto}}
  .book{{display:flex;flex-direction:column}}
  .side.L{{position:relative}}
  .pg-text{{position:relative;inset:auto;min-height:var(--S);padding:22px 20px;gap:0}}
  .eyebrow{{font-size:12px}}.tension .lbl{{font-size:11px}}
  .pg-text h1{{font-size:38px}}.pg-text h2{{font-size:40px}}
  .sub{{font-size:16px}}.tension{{font-size:19px}}.insight{{font-size:14.5px}}.haiku{{font-size:19px;margin-top:20px}}
  .toc button{{font-size:16px}}.all{{font-size:14px}}
  .mid{{padding-block:22px}}
  .ctrl{{gap:10px}}.ctrl button{{min-width:84px}}.ctrl .pos{{min-width:0;font-size:13px}}
  body{{overflow:auto}}
  .book{{width:var(--S);height:auto}}
  .side.L{{top:0;border-radius:3px 3px 0 0}}
  .side.R{{right:auto;left:0;border-radius:0 0 3px 3px}}
  .side.L::after,.side.R::after{{display:none}}
  .hit{{display:none}}
  .book.turn{{animation:turn .45s ease}}
}}
@keyframes turn{{0%{{opacity:1;transform:none}}45%{{opacity:0;transform:translateX(var(--dx,-24px))}}55%{{opacity:0;transform:translateX(calc(var(--dx,-24px)*-1))}}100%{{opacity:1;transform:none}}}}
@media (prefers-reduced-motion:reduce){{.leaf{{transition:none}}.book.turn{{animation:none}}}}
</style>
<div class="stage">
  <div class="book" id="book" aria-live="polite">
    <div class="side L" id="sideL"></div>
    <div class="side R" id="sideR"></div>
    <button class="hit L" id="hitL" aria-label="העמוד הבא"></button>
    <button class="hit R" id="hitR" aria-label="העמוד הקודם"></button>
  </div>
  <nav class="ctrl" aria-label="דפדוף">
    <button id="prev">הקודם</button>
    <span class="pos" id="pos"></span>
    <button id="next">הבא</button>
  </nav>
</div>
{tpl}
<script>
(function(){{
  var T=[].slice.call(document.querySelectorAll('template')), n=T.length, i=0, busy=false;
  var L=document.getElementById('sideL'), R=document.getElementById('sideR'), book=document.getElementById('book');
  function part(k,side){{return T[k].content.querySelector('.'+side).innerHTML;}}
  function show(k){{L.innerHTML=part(k,'L'); R.innerHTML=part(k,'R'); i=k; ui(); try{{history.replaceState(null,'','#p'+k);}}catch(e){{}}}}
  function ui(){{
    document.getElementById('prev').disabled=i===0; document.getElementById('next').disabled=i===n-1;
    var nm=T[i].dataset.name;
    document.getElementById('pos').innerHTML = i===0 ? '<b>כריכה</b>' : i===n-1 ? '<b>סוף</b>' : '<b>'+nm+'</b> · '+i+' מתוך '+(n-2);
  }}
  var narrow=function(){{return matchMedia('(max-width:820px)').matches;}};
  var reduce=matchMedia('(prefers-reduced-motion: reduce)').matches;
  function go(k){{
    if(busy||k<0||k>=n||k===i) return;
    if(reduce){{show(k);return;}}
    if(narrow()){{busy=true;book.style.setProperty('--dx',k>i?'-24px':'24px');book.classList.remove('turn');void book.offsetWidth;book.classList.add('turn');setTimeout(function(){{show(k);}},200);setTimeout(function(){{busy=false;}},460);return;}}
    busy=true; var fwd=k>i, leaf=document.createElement('div');
    leaf.className='leaf '+(fwd?'fwd':'back');
    // קדימה בספר עברי: העמוד השמאלי מתהפך אל הימין. אחורה: העמוד הימני מתהפך אל השמאל.
    leaf.innerHTML='<div class="face f">'+(fwd?part(i,'L'):part(i,'R'))+'</div><div class="face b">'+(fwd?part(k,'R'):part(k,'L'))+'</div>';
    book.appendChild(leaf);
    if(fwd) L.innerHTML=part(k,'L'); else R.innerHTML=part(k,'R');
    requestAnimationFrame(function(){{requestAnimationFrame(function(){{leaf.style.transform='rotateY('+(fwd?180:-180)+'deg)';}});}});
    setTimeout(function(){{show(k);leaf.remove();busy=false;}},920);
  }}
  document.getElementById('next').onclick=function(){{go(i+1);}};
  document.getElementById('prev').onclick=function(){{go(i-1);}};
  document.getElementById('hitL').onclick=function(){{go(i+1);}};
  document.getElementById('hitR').onclick=function(){{go(i-1);}};
  book.addEventListener('click',function(ev){{var t=ev.target.closest('[data-to]');if(t){{ev.stopPropagation();go(+t.dataset.to);}}}},true);
  document.addEventListener('keydown',function(ev){{if(ev.key==='ArrowLeft'||ev.key==='PageDown'||ev.key===' ')go(i+1);if(ev.key==='ArrowRight'||ev.key==='PageUp')go(i-1);if(ev.key==='Home')go(0);if(ev.key==='End')go(n-1);}});
  var sx=null;book.addEventListener('touchstart',function(ev){{sx=ev.touches[0].clientX;}},{{passive:true}});
  book.addEventListener('touchend',function(ev){{if(sx===null)return;var dx=ev.changedTouches[0].clientX-sx;if(Math.abs(dx)>40)go(dx>0?i+1:i-1);sx=null;}});
  var m=(location.hash||'').match(/^#p(\\d+)$/); show(m?Math.min(+m[1],n-1):0);
}})();
</script>
'''
open(os.path.join(HERE, 'book.html'), 'w', encoding='utf8').write(doc)
# גרסה לאתר (Vercel): מסמך מלא, וכפתור חזרה לאפליקציה
site = doc.replace('<div class="stage">', '<a class="back" href="../">לאפליקציה</a>\n<div class="stage">', 1)
site = site.replace('</style>', '.back{position:fixed;top:12px;left:max(16px,env(safe-area-inset-left,0px));z-index:50;font-size:13px;color:var(--ink);text-decoration:none;background:var(--paper);padding:6px 12px;border-radius:4px;box-shadow:0 1px 3px rgba(0,0,0,.1)}\n</style>', 1)
open(os.path.join(HERE, 'index.html'), 'w', encoding='utf8').write('<!doctype html>\n<html lang="he" dir="rtl">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n</head>\n<body>\n' + site + '\n</body>\n</html>\n')
print('spreads', len(spreads), 'bytes', len(doc))
