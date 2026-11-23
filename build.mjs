// בנייה: מאחד את הנתונים, הקוד והעיצוב לקובץ אחד. index.html לאתר, dist/artifact.html לעמוד ב-claude.ai.
import { readFileSync, writeFileSync, mkdirSync } from 'node:fs';
const app = readFileSync('src/app.html', 'utf8')
  .replace('/*DATA*/', () => readFileSync('src/data.js', 'utf8'))
  .replace('/*APP*/', () => readFileSync('src/app.js', 'utf8'));
mkdirSync('dist', { recursive: true });
writeFileSync('dist/artifact.html', app);
writeFileSync('index.html', `<!doctype html>
<html lang="he" dir="rtl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<style>*{box-sizing:border-box}:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}body{margin:0}img{max-width:100%}[hidden]{display:none!important}</style>
</head>
<body>
${app}
</body>
</html>
`);
console.log('נבנה:', app.length, 'תווים');
