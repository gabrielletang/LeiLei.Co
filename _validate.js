const fs = require('fs');
const s = fs.readFileSync('leilei_co.html', 'utf8');
const i = s.indexOf('const articleHTML = `');
const j = s.indexOf('`;', i);
const block = s.slice(i, j + 2);
new Function(block);            // throws if template literal is malformed
console.log('JS template OK, block length', block.length);
console.log("has Simpson h1:", block.includes("Simpson's Paradox</h1>"));
console.log("has svg figure:", block.includes('<svg'));
console.log("candy text remaining in article:", block.includes('Ultimate Sweet'));
