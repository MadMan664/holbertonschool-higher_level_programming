#!/usr/bin/node
const a = process.argv.slice(2).map(Number).sort((x, y) => y - x);
console.log(a.length > 1 ? a[1] : 0);
