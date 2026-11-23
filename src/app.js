(function () {
'use strict';
var CATS = window.CATS, CITIES = window.CITIES, SOURCES = window.SOURCES;
CITIES.forEach(function (c, i) { c.id = 'c' + (i + 1); c.idx = i; });
var ORDER = ['mem', 'des', 'sig', 'thin', 'trade', 'eyes', 'names', 'dead', 'sky', 'cont', 'hidden', 'impl'];
var LAYERS = [['t', 'רעיון ומתח'], ['p', 'מקום וצורה'], ['mt', 'חומר ומרקם'], ['L', 'אור וזמן'], ['C', 'קומפוזיציה ומבט'], ['pl', 'פלטה ואווירה']];
var LAYER_COL = ['#C0564C', '#3F6DB3', '#A35E46', '#B0852B', '#3B8C98', '#8A6BB0'];
var MJ = 'Documentary realism, Professional architecture photography, 1:1 --ar 1:1 --no text, words, writing, frame divisions';
var OTHER = 'Documentary realism, Professional architecture photography, 1:1, ללא טקסט, ללא כיתוב, ללא חלוקת מסגרות';

function store(k, v) { try { if (v === undefined) return localStorage.getItem(k); localStorage.setItem(k, v); } catch (e) { return null; } }
var state = { tool: store('arim.tool') || 'mj', variant: 0, hybrid: '' };

/* ---------- מוטיבים גרפיים: כל עיר מצוירת מהנתונים שלה ---------- */
function rng(seed) { var s = 0; for (var i = 0; i < seed.length; i++) s = (s * 31 + seed.charCodeAt(i)) >>> 0; return function () { s = (s * 1664525 + 1013904223) >>> 0; return s / 4294967296; }; }
function P(d, w, o) { return '<path d="' + d + '" stroke-width="' + (w || 0.7) + '"' + (o ? ' opacity="' + o + '"' : '') + '/>'; }
function C(x, y, r, w, f, o) { return '<circle cx="' + x.toFixed(1) + '" cy="' + y.toFixed(1) + '" r="' + r.toFixed(1) + '" stroke-width="' + (w || 0.7) + '"' + (f ? ' fill="currentColor" fill-opacity="' + f + '"' : '') + (o ? ' opacity="' + o + '"' : '') + '/>'; }
function R(x, y, w, h, sw, f, o) { return '<rect x="' + x.toFixed(1) + '" y="' + y.toFixed(1) + '" width="' + w.toFixed(1) + '" height="' + h.toFixed(1) + '" stroke-width="' + (sw || 0.7) + '"' + (f ? ' fill="currentColor" fill-opacity="' + f + '"' : '') + (o ? ' opacity="' + o + '"' : '') + '/>'; }
function house(x, y, s) { return P('M' + x + ' ' + y + 'h' + s + 'v' + (-s) + 'l' + (-s / 2) + ' ' + (-s * 0.6) + 'l' + (-s / 2) + ' ' + (s * 0.6) + 'z', 0.6); }

var M = {
  domes: function (r) { var o = ''; for (var row = 0; row < 5; row++) for (var i = 0; i < 6 + row; i++) { var x = 8 + i * (84 / (5 + row)) + r() * 3, y = 40 + row * 11, w = 5 + r() * 4; o += P('M' + (x - w) + ' ' + y + 'a' + w + ' ' + w + ' 0 0 1 ' + (2 * w) + ' 0', 0.7); o += P('M' + x + ' ' + (y - w) + 'v-2', 0.5); } o += P('M50 38V12', 0.8) + P('M47 12l3-4 3 4', 0.8); return o; },
  spiral: function () { var pts = []; for (var t = 0; t < 34; t += 0.2) { var rr = 2 + t * 1.25; pts.push((50 + rr * Math.cos(t)).toFixed(1) + ' ' + (52 + rr * Math.sin(t) * 0.9).toFixed(1)); } var o = P('M' + pts.join(' L'), 0.6); for (var i = 0; i < 9; i++) o += C(14 + i * 9, 92, 1.3, 0.5, 0.5); return o; },
  grid: function (r) { var o = ''; for (var i = 0; i < 9; i++) { var y = 10 + i * 10 + r() * 3; o += P('M8 ' + y + 'H92', 0.4, 0.6); } for (var j = 0; j < 7; j++) { var x = 12 + j * 13 + r() * 3; o += P('M' + x + ' 8V92', 0.4, 0.6); } for (var k = 0; k < 40; k++) { var a = r() * 84 + 8, b = r() * 84 + 8; o += P('M' + a + ' ' + b + 'l' + (r() * 6 - 3) + ' ' + (r() * 6 - 3), 0.8); } return o; },
  notes: function () { var o = ''; for (var s = 0; s < 3; s++) { for (var l = 0; l < 5; l++) o += P('M8 ' + (22 + s * 26 + l * 3) + 'H92', 0.35, 0.7); for (var n = 0; n < 9; n++) { var y = 22 + s * 26 + ((n * 7 + s * 3) % 5) * 3; o += C(14 + n * 9, y, 1.6, 0.6, 0.9); } } return o; },
  spheres: function (r) { var o = '', cs = [[32, 38, 18], [68, 56, 22], [36, 78, 11]]; cs.forEach(function (c) { o += C(c[0], c[1], c[2], 0.8); for (var i = -2; i <= 2; i++) o += P('M' + (c[0] - c[2] * 0.7) + ' ' + (c[1] + i * c[2] * 0.22) + 'h' + (c[2] * 1.4), 0.35, 0.7); for (var j = 0; j < 4; j++) o += R(c[0] - c[2] * 0.5 + j * c[2] * 0.25, c[1] - c[2] * 0.2 - r() * c[2] * 0.4, c[2] * 0.12, c[2] * 0.5, 0.4); o += P('M' + (c[0] - c[2] * 0.6) + ' ' + (c[1] - c[2] * 0.5) + 'a' + c[2] + ' ' + c[2] + ' 0 0 1 ' + c[2] * 0.5 + ' -' + c[2] * 0.25, 1.2, 0.6); }); return o; },
  postcards: function () { var o = '<g transform="rotate(-6 36 44)">' + R(14, 26, 44, 32, 0.8) ; for (var i = 0; i < 4; i++) o += P('M' + (18 + i * 10) + ' 54v-10a4 4 0 0 1 8 0v10', 0.5); o += '</g>'; for (var j = 0; j < 7; j++) o += R(40 + j * 7, 92 - (20 + (j * 13) % 30), 5, 20 + (j * 13) % 30, 0.6); return o; },
  towers: function () { var o = ''; [18, 38, 62, 82].forEach(function (x, i) { o += R(x - 3, 14 + i % 2 * 6, 6, 60, 0.8); }); for (var g = 0; g < 7; g++) o += P('M' + (10 + g * 12) + ' 88v-6a4 4 0 0 1 8 0v6', 0.6); o += P('M6 88H94', 0.6); for (var k = 0; k < 9; k++) o += R(10 + (k % 3) * 28, 76 + Math.floor(k / 3) * 0, 0, 0, 0); return o; },
  rings: function () { var o = ''; for (var i = 1; i <= 7; i++) o += C(50, 54, i * 6, 0.6, 0, i % 2 ? 1 : 0.5); o += P('M70 12l6 6-6 8-6-8z', 0.8) + P('M70 26q-6 14 4 24', 0.4); return o; },
  split: function (r) { var o = P('M6 60H94', 0.7); for (var i = 0; i < 6; i++) { var x = 10 + i * 6, h = 18 + r() * 22; o += R(x, 60 - h, 4, h, 0.6); } o += P('M28 22v-8M26 16h4', 0.6); for (var j = 0; j < 3; j++) { var px = 62 + j * 11; o += P('M' + px + ' 60v-16', 0.7); for (var a = 0; a < 5; a++) o += P('M' + px + ' 44q' + (Math.cos(a) * 6) + ' -3 ' + (Math.cos(a * 1.3) * 9) + ' ' + (2 + a % 2 * 2), 0.5); } for (var w = 0; w < 5; w++) o += P('M' + (8 + w * 8) + ' ' + (68 + w * 4) + 'q4 -2 8 0', 0.4, 0.7); for (var d = 0; d < 4; d++) o += P('M' + (56 + d * 9) + ' ' + (70 + d * 5) + 'q5 -3 10 0', 0.4, 0.7); return o; },
  labyrinth: function () { var o = ''; for (var i = 0; i < 6; i++) { var s = 8 + i * 7, gap = i % 2 ? 'M' + (50 - s) + ' ' + (50 - s) + 'H' + (50 + s - 10) + 'M' + (50 + s) + ' ' + (50 - s) + 'V' + (50 + s) + 'H' + (50 - s) + 'V' + (50 - s + 10) : 'M' + (50 - s + 10) + ' ' + (50 - s) + 'H' + (50 + s) + 'V' + (50 + s - 10) + 'M' + (50 + s) + ' ' + (50 + s) + 'H' + (50 - s) + 'V' + (50 - s); o += P(gap, 0.8); } return o; },
  signs: function () { var o = P('M8 20H92', 0.5); [16, 40, 64, 84].forEach(function (x) { o += P('M' + x + ' 20v6', 0.5); }); o += P('M12 30l8 14M20 30l-8 14', 0.9) + P('M36 30h8l2 6-2 10h-8l-2-10z', 0.8) + P('M64 30v14M56 34h16M56 34l-3 6h6zM72 34l-3 6h6z', 0.7) + C(84, 36, 5, 0.8) + P('M84 31v10', 0.6); for (var i = 0; i < 6; i++) o += P('M' + (8 + i * 16) + ' 92l4-22h8l4 22', 0.5, 0.6); return o; },
  repeat: function () { var o = ''; for (var i = 0; i < 3; i++) for (var j = 0; j < 3; j++) { var x = 20 + i * 30, y = 22 + j * 28; o += C(x, y, 3, 0.7) + P('M' + x + ' ' + (y + 3) + 'v10M' + (x - 5) + ' ' + (y + 8) + 'h10', 0.7) + P('M' + (x + 4) + ' ' + (y + 6) + 'a6 6 0 0 1 8 -2', 0.6); } o += '<ellipse cx="50" cy="8" rx="16" ry="4" stroke-width=".6"/>'; return o; },
  inverse: function () { var o = ''; for (var i = 0; i < 5; i++) { var x = 12 + i * 17; o += P('M' + x + ' 30h12v14l-6 7-6-7z', 0.7); o += P('M' + x + ' 82h12v-14l-6-7-6 7z', 0.7, 0.5); } o += P('M6 56H94', 0.4); for (var k = 0; k < 4; k++) o += P('M' + (20 + k * 18) + ' 18v-8m-3 3h6', 0.6); return o; },
  filigree: function (r) { var o = ''; for (var i = 0; i < 10; i++) { var x = 10 + i * 9; o += P('M' + x + ' 40c0 -10 8 -10 8 -2c0 6 -6 6 -6 0', 0.5); o += P('M' + x + ' 40v-14a4 4 0 0 1 8 0v14', 0.5); } for (var k = 0; k < 26; k++) o += C(8 + r() * 84, 58 + r() * 36, 1 + r() * 4, 0.3, 0.75); for (var c = 0; c < 4; c++) o += R(14 + c * 22, 46, 5, 18, 0.6, 0.85); return o; },
  wells: function () { var o = ''; for (var i = 0; i < 7; i++) for (var j = 0; j < 3; j++) { var x = 10 + i * 13 + (j % 2) * 6, y = 14 + j * 12; o += '<ellipse cx="' + x + '" cy="' + y + '" rx="4" ry="1.6" stroke-width=".7"/>' + P('M' + x + ' ' + (y + 1.6) + 'V58', 0.3, 0.6); } o += P('M6 52H94', 0.7); for (var w = 0; w < 6; w++) o += P('M6 ' + (66 + w * 5) + 'q11 -3 22 0t22 0t22 0t22 0', 0.4, 0.7 - w * 0.08); return o; },
  stilts: function (r) { var o = P('M4 92H96', 0.6); for (var i = 0; i < 6; i++) { var x = 10 + i * 15, y = 26 + r() * 18; o += P('M' + (x + 2) + ' ' + (y + 2) + 'V92M' + (x + 8) + ' ' + (y + 2) + 'V92', 0.4); o += house(x, y + 2, 10); if (i < 5) o += P('M' + (x + 10) + ' ' + (y + 6) + 'Q' + (x + 13) + ' ' + (y + 12) + ' ' + (x + 15) + ' ' + (y + 6), 0.4); } o += P('M80 18v-8l5 2-5 2', 0.6); return o; },
  pipes: function (r) { var o = ''; for (var i = 0; i < 8; i++) { var x = 10 + i * 11; o += P('M' + x + ' 96V' + (14 + r() * 20), 0.9); } for (var j = 0; j < 6; j++) { var y = 30 + j * 10, a = 10 + Math.floor(r() * 4) * 11; o += P('M' + a + ' ' + y + 'h' + (11 + Math.floor(r() * 3) * 11), 0.9); o += C(a + 4, y - 3, 1.5, 0.6); } o += P('M58 70h24a12 8 0 0 1 -24 0', 0.7) + P('M24 50h10l-2 6h-6z', 0.6); return o; },
  wheel: function () { var o = C(32, 42, 24, 0.8); for (var i = 0; i < 12; i++) { var a = i * Math.PI / 6; o += P('M32 42L' + (32 + 24 * Math.cos(a)).toFixed(1) + ' ' + (42 + 24 * Math.sin(a)).toFixed(1), 0.4) + C(32 + 24 * Math.cos(a), 42 + 24 * Math.sin(a), 1.6, 0.5); } o += P('M24 92L32 42L40 92', 0.7); for (var c = 0; c < 4; c++) o += R(62 + (c % 2) * 14, 58 + Math.floor(c / 2) * 16 - (c === 3 ? 6 : 0), 11, 12, 0.6, 0, c === 3 ? 0.5 : 1); o += P('M60 86h32M64 86v4M88 86v4', 0.6); return o; },
  web: function () { var o = P('M4 10L18 96M96 10L82 96', 1.1); var pts = [[18, 30], [82, 30], [16, 52], [84, 52], [20, 70], [80, 70]]; pts.forEach(function (a) { pts.forEach(function (b) { if (a[0] < 50 && b[0] > 50) o += P('M' + a[0] + ' ' + a[1] + 'L' + b[0] + ' ' + b[1], 0.35); }); }); for (var i = 0; i < 6; i++) { var x = 30 + i * 8; o += P('M' + x + ' 50v6', 0.4) + '<ellipse cx="' + x + '" cy="' + (60 + (i % 2) * 3) + '" rx="2.6" ry="4" stroke-width=".6"/>'; } return o; },
  mirror: function () { var o = P('M4 52H96', 0.8), sky = ''; var hs = [14, 22, 18, 30, 12, 24, 20]; hs.forEach(function (h, i) { var x = 8 + i * 12; sky += R(x, 52 - h, 9, h, 0.7); sky += R(x + 3, 52 - h + 4, 3, 3, 0.4); }); o += sky + '<g transform="matrix(1 0 0 -1 0 104)" opacity=".45">' + sky + '</g>'; for (var w = 0; w < 4; w++) o += P('M' + (12 + w * 20) + ' ' + (60 + w * 7) + 'h10', 0.4, 0.6); return o; },
  eye: function () { var o = P('M10 50Q50 14 90 50Q50 86 10 50z', 0.9) + C(50, 50, 13, 0.8) + C(50, 50, 5, 0.6, 0.9); for (var i = 0; i < 5; i++) o += P('M' + (20 + i * 15) + ' 20l4 -3 4 3', 0.6); for (var j = 0; j < 6; j++) o += P('M' + (12 + j * 14) + ' 86h8', 0.8); return o; },
  cloudstilts: function () { var o = ''; for (var i = 0; i < 5; i++) { var x = 14 + i * 17; o += P('M' + (x + 4) + ' 30V96', 0.35); o += house(x, 30, 9); } [[20, 40], [50, 44], [78, 40]].forEach(function (c) { o += '<ellipse cx="' + c[0] + '" cy="' + c[1] + '" rx="18" ry="5" stroke-width=".5" fill="currentColor" fill-opacity=".12"/>'; }); for (var t = 0; t < 9; t++) o += P('M' + (6 + t * 10) + ' 96l5 -12 5 12', 0.5, 0.7); return o; },
  bridges: function () { var o = ''; o += P('M4 40Q28 18 52 40', 0.8) + P('M48 62Q72 40 96 62', 0.8) + P('M4 82h40M8 82v-6a6 6 0 0 1 12 0v6M24 82v-6a6 6 0 0 1 12 0v6', 0.7); for (var i = 0; i < 6; i++) o += P('M' + (10 + i * 7) + ' ' + (36 - Math.sin(i / 5 * Math.PI) * 10) + 'V40', 0.4); o += P('M70 20h12v8a6 6 0 0 1 -12 0z', 0.7) + P('M76 20v14', 0.4); for (var t = 0; t < 7; t++) o += R(54 + t * 6, 84, 5, 5, 0.4, t % 2 ? 0.3 : 0); return o; },
  tents: function () { var o = ''; [[22, 70, 18], [52, 64, 22], [80, 72, 16]].forEach(function (t) { o += P('M' + (t[0] - t[2]) + ' ' + t[1] + 'L' + t[0] + ' ' + (t[1] - t[2] * 1.3) + 'L' + (t[0] + t[2]) + ' ' + t[1] + 'z', 0.8) + P('M' + t[0] + ' ' + (t[1] - t[2] * 1.3) + 'V' + t[1], 0.4); }); o += P('M50 90c-6 -6 -2 -10 0 -14c2 4 6 8 0 14z', 0.8, 0) + '<path d="M50 90c-6 -6 -2 -10 0 -14c2 4 6 8 0 14z" fill="currentColor" fill-opacity=".6" stroke-width=".6"/>'; for (var a = 0; a < 7; a++) { var an = a / 7 * Math.PI * 2; o += P('M50 82L' + (50 + 46 * Math.cos(an)).toFixed(1) + ' ' + (82 + 14 * Math.sin(an)).toFixed(1), 0.3, 0.5); } return o; },
  dots: function (r) { var o = '', pts = []; for (var i = 0; i < 18; i++) { var x = 10 + r() * 80, y = 14 + r() * 74; pts.push([x, y]); o += C(x, y, 2.2, 0.7, 0.6); } for (var j = 0; j < 9; j++) { var a = pts[j], b = pts[j + 9]; var mx = (a[0] + b[0]) / 2, my = (a[1] + b[1]) / 2; o += P('M' + a[0].toFixed(1) + ' ' + a[1].toFixed(1) + 'L' + ((a[0] + mx) / 2).toFixed(1) + ' ' + ((a[1] + my) / 2).toFixed(1), 0.4, 0.6) + P('M' + b[0].toFixed(1) + ' ' + b[1].toFixed(1) + 'L' + ((b[0] + mx) / 2).toFixed(1) + ' ' + ((b[1] + my) / 2).toFixed(1), 0.4, 0.6); } return o; },
  copies: function () { var o = ''; for (var i = 0; i < 3; i++) for (var j = 0; j < 3; j++) { var x = 12 + i * 28, y = 30 + j * 26; o += house(x, y, 7) + house(x + 8, y, 7) + R(x + 3, y - 14, 3, 6, 0.4); } o += P('M24 22Q38 30 52 22T80 22', 0.5, 0.7); return o; },
  threads: function (r) { var o = '', poles = []; for (var i = 0; i < 9; i++) { var x = 10 + r() * 80, y = 30 + r() * 50; poles.push([x, y]); o += P('M' + x.toFixed(1) + ' ' + y.toFixed(1) + 'v-16', 0.9); } for (var k = 0; k < 22; k++) { var a = poles[Math.floor(r() * 9)], b = poles[Math.floor(r() * 9)]; if (a === b) continue; o += P('M' + a[0].toFixed(1) + ' ' + (a[1] - 14 + r() * 10).toFixed(1) + 'L' + b[0].toFixed(1) + ' ' + (b[1] - 14 + r() * 10).toFixed(1), 0.4, [1, 0.6, 0.3][k % 3]); } return o; },
  zigzag: function () { var o = ''; for (var i = 0; i < 4; i++) o += P('M6 ' + (18 + i * 22) + 'l10 8 10 -8 10 8 10 -8 10 8 10 -8 10 8 10 -8', 0.7, i % 2 ? 0.5 : 1); for (var j = 0; j < 4; j++) o += P('M' + (18 + j * 22) + ' 6l8 10 -8 10 8 10 -8 10 8 10 -8 10 8 10 -8 10', 0.5, 0.6); return o; },
  two: function () { var o = '<g stroke-dasharray="1.5 2" opacity=".75">'; [10, 20, 30, 40, 50, 60, 70, 80].forEach(function (x, i) { var h = 16 + (i * 7) % 24; o += P('M' + x + ' 52v-' + h + 'q5 -8 10 0v' + h, 0.6); }); o += C(50, 18, 6, 0.6) + '</g>'; for (var i = 0; i < 9; i++) o += R(8 + i * 9.5, 74 - (i % 3) * 4, 8, 18 + (i % 3) * 4, 0.6); o += P('M4 92H96', 0.6); return o; },
  figurines: function () { var o = ''; for (var i = 0; i < 4; i++) { var x = 16 + i * 22; o += P('M' + (x - 7) + ' 72V48a7 7 0 0 1 14 0V72', 0.7); o += C(x, 56, 2.2, 0.6, 0.5) + P('M' + (x - 3) + ' 70l1.5 -11h3l1.5 11z', 0.6, 0, 0); } o += R(14, 82, 16, 10, 0.6) + R(36, 84, 12, 8, 0.6); return o; },
  fragments: function (r) { var o = ''; for (var i = 0; i < 7; i++) { var x = 10 + r() * 76, y = 20 + r() * 66, s = 5 + r() * 7; o += '<g transform="rotate(' + (r() * 60 - 30).toFixed(0) + ' ' + x.toFixed(0) + ' ' + y.toFixed(0) + ')">' + P('M' + x.toFixed(1) + ' ' + y.toFixed(1) + 'h' + (s * 2).toFixed(1) + 'l-2 ' + s.toFixed(1) + 'h' + (-(s * 2 - 4)).toFixed(1) + 'z', 0.7) + P('M' + (x + 2).toFixed(1) + ' ' + (y + 2).toFixed(1) + 'c2 -4 4 0 3 3M' + (x + s * 2 - 2).toFixed(1) + ' ' + (y + 2).toFixed(1) + 'c-2 -4 -4 0 -3 3', 0.5) + '</g>'; } return o; },
  stage: function () { var o = P('M8 92V30Q50 4 92 30V92', 0.9) + P('M8 40Q30 46 34 30M92 40Q70 46 66 30', 0.6); for (var i = 0; i < 3; i++) { var x = 32 + i * 18; o += C(x, 62, 3, 0.7) + P('M' + (x - 4) + ' 84l4 -18 4 18', 0.7); } o += C(68, 62, 3, 0.5, 0, 0.35) + P('M64 84l4 -18 4 18', 0.5, 0.35); return o; },
  masks: function (r) { var o = ''; for (var i = 0; i < 7; i++) { var x = 14 + (i % 4) * 24 + (i > 3 ? 12 : 0), y = 30 + (i > 3 ? 36 : 0); o += '<ellipse cx="' + x + '" cy="' + y + '" rx="8" ry="11" stroke-width=".8"' + (i % 3 === 0 ? ' fill="currentColor" fill-opacity=".18"' : '') + '/>'; o += P('M' + (x - 11) + ' ' + (y - 2) + 'Q' + x + ' ' + (y - 22) + ' ' + (x + 11) + ' ' + (y - 2), 0.5, 0.6); } return o; },
  under: function () { var o = P('M4 50H96', 0.9), s = ''; [16, 24, 12, 28, 20, 14, 22].forEach(function (h, i) { s += R(8 + i * 12, 50 - h, 10, h, 0.7); }); o += s + '<g transform="matrix(1 0 0 -1 0 100)">' + s.replace(/stroke-width/g, 'fill="currentColor" fill-opacity=".2" stroke-width') + '</g>'; return o; },
  layers: function () { var o = ''; for (var i = 0; i < 3; i++) { var y = 10 + i * 28; o += R(8, y, 84, 24, 0.7); } for (var a = 0; a < 14; a++) o += P('M' + (12 + a * 6) + ' 30v-14', 0.5); for (var b = 0; b < 7; b++) o += R(12 + b * 11, 44, 8, 14, 0.5, 0.25); for (var c = 0; c < 20; c++) o += C(14 + (c % 10) * 8, 74 + Math.floor(c / 10) * 8, 0.9, 0.4, 0.4, 0.6); return o; },
  trash: function (r) { var o = ''; for (var i = 0; i < 36; i++) { var a = i / 36 * Math.PI * 2, rr = 34 + r() * 10; o += P('M' + (50 + rr * Math.cos(a)).toFixed(1) + ' ' + (50 + rr * Math.sin(a)).toFixed(1) + 'l' + (r() * 6 - 3).toFixed(1) + ' ' + (r() * 6 - 3).toFixed(1) + 'l' + (r() * 6 - 3).toFixed(1) + ' ' + (r() * 6 - 3).toFixed(1) + 'z', 0.6, 0.8); } for (var j = 0; j < 9; j++) o += R(38 + (j % 3) * 8, 38 + Math.floor(j / 3) * 8, 6, 6, 0.6); return o; },
  sprawl: function () { var o = P('M4 30H96', 0.4); for (var row = 0; row < 6; row++) { var y = 34 + row * row * 2.2 + row * 4, s = 2 + row * 1.4, n = Math.floor(84 / (s * 1.6)); for (var i = 0; i < n; i++) o += house(8 + i * s * 1.6, y + s, s); } return o; },
  treerings: function (r) { var o = ''; for (var i = 1; i <= 9; i++) { var pts = []; for (var a = 0; a <= 24; a++) { var an = a / 24 * Math.PI * 2, rr = i * 4.6 + (r() - 0.5) * 2; pts.push((50 + rr * Math.cos(an)).toFixed(1) + ' ' + (50 + rr * Math.sin(an)).toFixed(1)); } o += P('M' + pts.join(' L') + 'z', 0.55); } o += C(50, 50, 1.6, 0.6, 1); return o; },
  carpet: function () { var o = R(14, 8, 72, 84, 0.9) + R(19, 13, 62, 74, 0.5); o += P('M50 20L74 50L50 80L26 50z', 0.8) + P('M50 32L64 50L50 68L36 50z', 0.6) + C(50, 50, 4, 0.6, 0.6); for (var i = 0; i < 4; i++) { o += C(26, 22 + i * 18.5, 2, 0.5) + C(74, 22 + i * 18.5, 2, 0.5); } return o; },
  scaffold: function () { var o = ''; for (var i = 0; i < 5; i++) for (var j = 0; j < 5; j++) { var x = 10 + i * 12, y = 40 + j * 11; o += R(x, y, 12, 11, 0.5) + (((i + j) % 2) ? P('M' + x + ' ' + y + 'l12 11', 0.35) : ''); } o += P('M82 96V14H40M82 22l-10 -8M60 14v14', 0.8); for (var s = 0; s < 6; s++) o += C(20 + s * 13, 8 + (s % 3) * 4, 0.7, 0.4, 1); return o; },
  seeds: function () { var o = '<ellipse cx="50" cy="52" rx="30" ry="38" stroke-width=".9"/><ellipse cx="50" cy="56" rx="17" ry="22" stroke-width=".7" fill="currentColor" fill-opacity=".15"/><ellipse cx="50" cy="60" rx="7" ry="9" stroke-width=".6"/>'; for (var i = 0; i < 5; i++) o += P('M' + (30 + i * 10) + ' 24c0 -6 4 -6 4 0', 0.5); o += P('M44 70h12M46 74h8', 0.5); return o; },
  venice: function () { var o = ''; for (var i = 0; i < 5; i++) o += P('M' + (8 + i * 18) + ' 50v-16a6 6 0 0 1 12 0v16', 0.7); o += P('M4 50H96', 0.6) + P('M30 64Q50 50 70 64', 0.8); for (var w = 0; w < 6; w++) o += P('M6 ' + (68 + w * 5) + 'q8 -2 16 0t16 0t16 0t16 0t16 0', 0.4, 0.75 - w * 0.1); o += P('M60 80q12 4 24 -2', 0.8); return o; }
};

function emblem(c, opts) {
  opts = opts || {};
  var col = CATS[c.k].c, r = rng(c.n), dark = opts.dark !== false;
  var id = 'g' + c.id + (opts.tag || '');
  var bg = dark ? '<defs><radialGradient id="' + id + '" cx="40%" cy="35%" r="75%"><stop offset="0" stop-color="' + col + '" stop-opacity=".55"/><stop offset=".55" stop-color="#1A1A1F" stop-opacity="1"/><stop offset="1" stop-color="#0E0E11"/></radialGradient></defs><rect x="-40" y="-40" width="200" height="200" fill="url(#' + id + ')"/>' : '';
  var stroke = dark ? '#F1EDE2' : col;
  var vb = opts.wide ? '-28 -14 156 156' : '0 0 100 100';
  return '<svg viewBox="' + vb + '" preserveAspectRatio="xMidYMid slice" aria-hidden="true">' + bg + '<g fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" style="color:' + stroke + '">' + (M[c.m] || M.grid)(r) + '</g></svg>';
}

/* ---------- בניית פרומפט ---------- */
function variantLabel(comp) {
  if (/חתך/.test(comp)) return 'חתך';
  if (/מלמעלה/.test(comp)) return 'מבט מלמעלה';
  if (/מלמטה|כלפי מעלה/.test(comp)) return 'מבט מלמטה';
  if (/תקריב/.test(comp)) return 'תקריב';
  if (/מחלון|ממרפסת|מסיפון/.test(comp)) return /מסיפון/.test(comp) ? 'מבט מהים' : 'מבט מחלון';
  if (/רחב|מהצד|אופקי/.test(comp)) return 'מבט רחב';
  return 'גובה העיניים';
}
function layersOf(c, v, other) {
  var src = other || c;
  return { t: c.t, p: src.p, mt: src.mt, L: c.v[v][0], C: c.v[v][1], pl: src.pl };
}
function promptText(L, tool) {
  return [L.t, L.p, L.mt, L.L, L.C, L.pl].join(', ') + ', ' + (tool === 'mj' ? MJ : OTHER);
}

/* ---------- עזרים ---------- */
var view = document.getElementById('view');
function esc(s) { return String(s).replace(/[&<>"]/g, function (m) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[m]; }); }
function toast(t) { var el = document.getElementById('toast'); el.textContent = t; el.classList.add('show'); clearTimeout(toast.t); toast.t = setTimeout(function () { el.classList.remove('show'); }, 1800); }
function copy(text, done) {
  function fallback() { var ta = document.createElement('textarea'); ta.value = text; ta.style.position = 'fixed'; ta.style.opacity = '0'; document.body.appendChild(ta); ta.select(); var ok = false; try { ok = document.execCommand('copy'); } catch (e) {} ta.remove(); toast(ok ? done : 'ההעתקה נחסמה. סמני את הטקסט והעתיקי ידנית.'); }
  try { navigator.clipboard.writeText(text).then(function () { toast(done); }, fallback); } catch (e) { fallback(); }
}
function setNav(r) { document.querySelectorAll('[data-go]').forEach(function (b) { b.classList.toggle('on', b.dataset.go === r); }); }
var coverAnim = null;

/* ---------- כריכה: מוזיאון כדורי הבדולח של פדורה ---------- */
var QUOTES = CITIES.map(function (c) { return [c.d, c.n]; });
function renderCover() {
  setNav('');
  view.innerHTML = '<section id="cover"><div id="orbs"></div><div class="cover-text"><div class="cover-inner"><h1>ערים סמויות</h1><div class="cover-q" id="cq"></div><button class="cover-go" data-go="atlas">פתיחה</button></div></div></section>';
  var box = document.getElementById('orbs'), W = box.clientWidth, H = box.clientHeight, orbs = [];
  var base = Math.max(46, Math.min(W, H) / 9);
  CITIES.forEach(function (c, i) {
    var r = rng(c.n + 'o'), s = base * (0.55 + r() * 0.9);
    var el = document.createElement('button'); el.className = 'orb'; el.setAttribute('aria-label', c.n);
    el.style.width = el.style.height = s + 'px';
    el.innerHTML = emblem(c, { tag: 'o' }) + '<span class="lbl">' + esc(c.n) + '</span>';
    el.style.boxShadow = 'inset -6px -8px 18px rgba(0,0,0,.55), inset 4px 5px 10px rgba(255,255,255,.12)';
    el.onclick = function () { location.hash = c.id; };
    box.appendChild(el);
    orbs.push({ el: el, s: s, x: r() * (W - s), y: r() * (H * 0.7 - s), vx: (r() - 0.5) * 0.18, vy: (r() - 0.5) * 0.14, ph: r() * 6 });
  });
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  function step(t) {
    orbs.forEach(function (o) {
      if (!reduce) { o.x += o.vx; o.y += o.vy + Math.sin(t / 2400 + o.ph) * 0.05; }
      if (o.x < -o.s * 0.3 || o.x > W - o.s * 0.7) o.vx *= -1;
      if (o.y < -o.s * 0.3 || o.y > H - o.s * 0.8) o.vy *= -1;
      o.el.style.transform = 'translate(' + o.x.toFixed(1) + 'px,' + o.y.toFixed(1) + 'px)';
    });
    if (!reduce) coverAnim = requestAnimationFrame(step);
  }
  coverAnim = requestAnimationFrame(step);
  var qi = Math.floor(Math.random() * QUOTES.length), cq = document.getElementById('cq');
  function showQ() { var q = QUOTES[qi % QUOTES.length]; cq.style.opacity = 0; setTimeout(function () { cq.innerHTML = esc(q[0]) + '<span>' + esc(q[1]) + '</span>'; cq.style.opacity = 1; }, 500); qi++; }
  showQ(); clearInterval(renderCover.qt); renderCover.qt = setInterval(function () { if (document.getElementById('cq')) showQ(); else clearInterval(renderCover.qt); }, 5200);
}

/* ---------- אטלס ---------- */
function renderAtlas(filter) {
  setNav('atlas');
  var f = (filter || '').trim();
  var html = '<div class="page"><div class="lead"><h2>אטלס הערים</h2><p><b>42 ערים</b> ב-<b>12 קבוצות</b> של קאלווינו. בחרי עיר כדי לקבל <b>שלושה פרומפטים</b> להמחשה, בנויים בחמש שכבות.</p>' +
    '<input id="q" class="search" type="search" placeholder="חיפוש עיר, חומר או רעיון" value="' + esc(f) + '" aria-label="חיפוש"></div><div class="atlas">';
  var count = 0;
  ORDER.forEach(function (k) {
    var list = CITIES.filter(function (c) { return c.k === k && (!f || (c.n + c.u + c.i + c.ph + c.t + c.mt).indexOf(f) > -1); });
    if (!list.length) return;
    count += list.length;
    html += '<section class="cat"><h3><i style="background:' + CATS[k].c + '"></i>' + CATS[k].n + '<small>' + list.length + ' ערים</small></h3>';
    list.forEach(function (c) { html += '<button class="city-row" data-city="' + c.id + '"><div class="em">' + emblem(c, { tag: 'a' }) + '</div><div><b>' + esc(c.n) + '</b><span>' + esc(c.d) + '</span></div></button>'; });
    html += '</section>';
  });
  if (!count) html += '<p>לא נמצאה עיר עבור "' + esc(f) + '". נסי מילה אחרת, למשל <b>מים</b>, <b>זיכרון</b> או <b>מראה</b>.</p>';
  html += '</div><p class="legend">הצבע מסמן את הקבוצה בספר. הסמל של כל עיר נבנה מהתיאור הפיזי שלה. השורה מתחת לשם היא <b>הזיקוק</b>: הרעיון שהתמונה צריכה להחזיק.</p></div>';
  view.innerHTML = html;
  var q = document.getElementById('q');
  q.oninput = function () { var pos = q.selectionStart; renderAtlas(q.value); var n = document.getElementById('q'); n.focus(); try { n.setSelectionRange(pos, pos); } catch (e) {} };
}

/* ---------- דף עיר ---------- */
function renderCity(c) {
  setNav('');
  var cat = CATS[c.k], prev = CITIES[(c.idx + CITIES.length - 1) % CITIES.length], next = CITIES[(c.idx + 1) % CITIES.length];
  var srcHtml = c.s.split(',').map(function (part) {
    part = part.trim(); var m = part.match(/^(\d+)-(\d+)$/), nums = [];
    if (m) for (var n = +m[1]; n <= +m[2]; n++) nums.push(n); else nums.push(+part);
    return nums.map(function (n) { return '<abbr title="' + esc(SOURCES[n] || '') + '">' + n + '</abbr>'; }).join(' ');
  }).join(' ');
  var opts = '<option value="">בחרי עיר להכלאה</option>' + CITIES.filter(function (o) { return o !== c; }).map(function (o) { return '<option value="' + o.id + '"' + (state.hybrid === o.id ? ' selected' : '') + '>' + esc(o.n) + '</option>'; }).join('');
  view.innerHTML = '<div class="page"><div class="city">' +
    '<figure class="plate" style="margin:0">' + emblem(c, { tag: 'p', wide: true }) + '<figcaption class="cap"><div class="cat-tag" style="color:' + cat.c + ';filter:brightness(1.6)">' + cat.n + '</div><h2>' + esc(c.n) + '</h2><p class="ins">' + esc(c.i) + '</p><p class="uniq">' + esc(c.u) + '</p></figcaption></figure>' +
    '<div class="lab">' +
      '<div><span class="lbl-s">זיקוק: מה התמונה צריכה להחזיק</span><p class="distil"><mark>' + esc(c.d) + '</mark></p></div>' +
      '<div><span class="lbl-s">שלוש המחשות, שונות בזווית ובאור</span><div class="tabs" id="tabs"></div></div>' +
      '<div class="layers" id="layers"></div>' +
      '<div class="tools"><button class="btn main" id="copyBtn">העתקת הפרומפט</button><button class="btn" id="copy3">העתקת שלושתם</button>' +
        '<span class="seg" role="group" aria-label="כלי יצירה"><button data-tool="mj">Midjourney</button><button data-tool="other">כלי אחר</button></span><span class="saved" id="saved"></span></div>' +
      '<div class="promptbox" id="pbox" dir="rtl"></div>' +
      '<div class="hybrid"><p><b>הכלאה:</b> המתח, האור והמבט של <b>' + esc(c.n) + '</b>, בתוך המקום, החומר והפלטה של עיר אחרת. כך קאלווינו בנה את כולן מונציה.</p><select id="hy" aria-label="עיר להכלאה">' + opts + '</select></div>' +
      '<div class="facts"><p><span class="lbl-s">תיאור פיזי בספר</span>' + esc(c.ph) + '</p><p><span class="lbl-s">משמעות מטפורית (הערכה, לא ציטוט)</span>' + esc(c.me) + '</p><p class="src"><span class="lbl-s">מקורות בקובץ, ריחוף מציג את שם המקור</span>' + srcHtml + '</p></div>' +
    '</div></div></div>' +
    '<div class="pager"><button class="btn" data-city="' + next.id + '" title="הבאה: ' + esc(next.n) + '">הבאה: ' + esc(next.n) + '</button><button class="btn" data-city="' + prev.id + '" title="הקודמת: ' + esc(prev.n) + '">הקודמת: ' + esc(prev.n) + '</button></div>';

  var tabs = document.getElementById('tabs');
  tabs.innerHTML = c.v.map(function (v, i) { return '<button class="tab" data-v="' + i + '"><b>' + ['א', 'ב', 'ג'][i] + '. ' + variantLabel(v[1]) + '</b><small>' + esc(v[0]) + '</small></button>'; }).join('');
  var last = null;
  function draw() {
    var other = state.hybrid ? CITIES.filter(function (o) { return o.id === state.hybrid; })[0] : null;
    if (other === c) other = null;
    var L = layersOf(c, state.variant, other);
    tabs.querySelectorAll('.tab').forEach(function (b) { b.classList.toggle('on', +b.dataset.v === state.variant); });
    document.querySelectorAll('[data-tool]').forEach(function (b) { b.classList.toggle('on', b.dataset.tool === state.tool); });
    document.getElementById('layers').innerHTML = LAYERS.map(function (l, i) {
      var from = other && /^(p|mt|pl)$/.test(l[0]) ? ' <small style="color:' + CATS[other.k].c + '">מ' + esc(other.n) + '</small>' : '';
      var changed = last && last[l[0]] !== L[l[0]];
      return '<div class="layer' + (changed ? ' flash' : '') + '"><span class="k"><i style="background:' + LAYER_COL[i] + '">' + (i + 1) + '</i>' + l[1] + from + '</span><span class="vv">' + esc(L[l[0]]) + '</span></div>';
    }).join('') + '<div class="layer"><span class="k"><i style="background:#2E2E2B">7</i>פרמטרים קבועים</span><span class="vv" dir="ltr" style="text-align:left;font-size:13px;color:var(--ink2)">' + esc(state.tool === 'mj' ? MJ : OTHER) + '</span></div>';
    var body = [L.t, L.p, L.mt, L.L, L.C, L.pl].join(', ');
    document.getElementById('pbox').innerHTML = esc(body) + ',<span class="par">' + esc(state.tool === 'mj' ? MJ : OTHER) + '</span>';
    last = L;
  }
  draw();
  tabs.onclick = function (e) { var b = e.target.closest('.tab'); if (!b) return; state.variant = +b.dataset.v; draw(); };
  document.querySelectorAll('[data-tool]').forEach(function (b) { b.onclick = function () { state.tool = b.dataset.tool; store('arim.tool', state.tool); draw(); var s = document.getElementById('saved'); s.textContent = 'נשמר'; setTimeout(function () { s.textContent = ''; }, 1400); }; });
  document.getElementById('hy').onchange = function (e) { state.hybrid = e.target.value; draw(); };
  document.getElementById('copyBtn').onclick = function () {
    var other = state.hybrid ? CITIES.filter(function (o) { return o.id === state.hybrid; })[0] : null;
    copy(promptText(layersOf(c, state.variant, other), state.tool), 'הפרומפט הועתק');
  };
  document.getElementById('copy3').onclick = function () {
    copy(c.v.map(function (v, i) { return c.n + ', גרסה ' + ['א', 'ב', 'ג'][i] + ' (' + variantLabel(v[1]) + ')\nזיקוק: ' + c.d + '\n' + promptText(layersOf(c, i), state.tool); }).join('\n\n'), 'שלושת הפרומפטים הועתקו');
  };
}

/* ---------- מקרא ---------- */
function renderLegend() {
  setNav('legend');
  view.innerHTML = '<div class="page"><div class="lead"><h2>מקרא ושיטה</h2><p>איך נבנה כל פרומפט, ומה מסמן כל צבע.</p></div><div class="legend-page">' +
    '<section><h3>חמש השכבות</h3><ol>' + LAYERS.map(function (l, i) { return '<li><b style="color:' + LAYER_COL[i] + '">' + l[1] + '</b>' + ['. ניגוד אחד שמחזיק את התמונה.', '. סוג המרחב וקנה המידה, מהתיאור הפיזי בספר.', '. חומר מוביל אחד ומצבו.', '. מקור האור, הכיוון והשעה. האור הוא גיבור.', '. זווית, מוקד אחד, וחוק קומפוזיציה.', '. צבעים ומצב רוח.'][i] + '</li>'; }).join('') + '</ol></section>' +
    '<section><h3>שלוש גרסאות לכל עיר</h3><p>כל גרסה שונה <b>בזווית</b> וב<b>אור</b>: רגע של סף בגובה העיניים, מבט רחב על העיר כמבנה, ותקריב שבו החומר מספר את הרעיון. <b>המתח</b> נשאר זהה, כדי שהשלוש יספרו את אותו רעיון.</p><p><b>Midjourney</b>: הפרמטרים עם שני מקפים בסוף. <b>כלי אחר</b>: בלי מקפים, ובמקומם "ללא טקסט, ללא כיתוב, ללא חלוקת מסגרות".</p></section>' +
    '<section><h3>הקבוצות בספר</h3><p>' + ORDER.map(function (k) { return '<span style="white-space:nowrap"><i style="display:inline-block;width:10px;height:10px;border-radius:50%;background:' + CATS[k].c + '"></i> ' + CATS[k].n + '</span>'; }).join(' &nbsp; ') + '</p><p>הסיווג נלקח מהקובץ. ערים עם סיווג כפול שויכו לקבוצה הראשונה.</p></section>' +
    '<section><h3>עובדה, הערכה והנחה</h3><p><b>עובדה:</b> שם העיר, הייחודיות, התיאור הפיזי והמקורות, כפי שהם בקובץ.</p><p><b>הערכה:</b> התובנה והמשמעות המטפורית, פרשנות שנאספה בקובץ.</p><p><b>הנחה:</b> הזיקוק, האור והמבט בפרומפטים. אלה החלטות המחשה, לא ציטוט מהספר.</p></section>' +
    '</div></div>';
}

/* ---------- ניתוב ---------- */
function route() {
  if (coverAnim) { cancelAnimationFrame(coverAnim); coverAnim = null; }
  var h = (location.hash || '').slice(1);
  var city = CITIES.filter(function (c) { return c.id === h; })[0];
  if (city) { if (route.lastCity !== city.id) { state.hybrid = ''; } route.lastCity = city.id; renderCity(city); window.scrollTo(0, 0); return; }
  route.lastCity = null;
  if (h === 'atlas') renderAtlas(''); else if (h === 'legend') renderLegend(); else renderCover();
  window.scrollTo(0, 0);
}
window.addEventListener('hashchange', route);
document.addEventListener('click', function (e) {
  var g = e.target.closest('[data-go]'); if (g) { location.hash = g.dataset.go; closeMenu(); return; }
  var c = e.target.closest('[data-city]'); if (c) { location.hash = c.dataset.city; return; }
  var a = e.target.closest('[data-act]'); if (a) { act(a.dataset.act); closeMenu(); return; }
  if (!e.target.closest('#menu') && !e.target.closest('#logoBtn')) closeMenu();
});
var menu = document.getElementById('menu');
function closeMenu() { menu.hidden = true; }
document.getElementById('logoBtn').onclick = function () { menu.hidden = !menu.hidden; };
document.addEventListener('keydown', function (e) {
  if (e.key === 'Escape') closeMenu();
  var h = (location.hash || '').slice(1), city = CITIES.filter(function (c) { return c.id === h; })[0];
  if (city && !/INPUT|SELECT|TEXTAREA/.test(document.activeElement.tagName)) {
    if (e.key === 'ArrowLeft') location.hash = CITIES[(city.idx + 1) % CITIES.length].id;
    if (e.key === 'ArrowRight') location.hash = CITIES[(city.idx + CITIES.length - 1) % CITIES.length].id;
  }
});
function act(a) {
  if (a === 'copyall') copy(CITIES.map(function (c) { return '## ' + c.n + ' (' + CATS[c.k].n + ')\nזיקוק: ' + c.d + '\n' + c.v.map(function (v, i) { return ['א', 'ב', 'ג'][i] + '. ' + promptText(layersOf(c, i), state.tool); }).join('\n'); }).join('\n\n'), 'כל 126 הפרומפטים הועתקו');
  if (a === 'random') location.hash = CITIES[Math.floor(Math.random() * CITIES.length)].id;
  if (a === 'legend') location.hash = 'legend';
  if (a === 'theme') { var r = document.documentElement, dark = r.dataset.theme ? r.dataset.theme === 'dark' : matchMedia('(prefers-color-scheme: dark)').matches; r.dataset.theme = dark ? 'light' : 'dark'; store('arim.theme', r.dataset.theme); }
}
var th = store('arim.theme'); if (th) document.documentElement.dataset.theme = th;
route();
})();
