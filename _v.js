const fs=require('fs');
const s=fs.readFileSync('leilei_co.html','utf8');
const i=s.indexOf('const articleHTML = `');
const j=s.indexOf('`;', i);
new Function(s.slice(i,j+2));
console.log('JS_OK');
