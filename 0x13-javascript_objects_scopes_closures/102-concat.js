#!/usr/bin/node
const fs = require('fs');
const argv = process.argv;
const src1 = fs.readFileSync(argv[2], 'utf8');
const src2 = fs.readFileSync(argv[3], 'utf8');
const src3 = src1 + src2;
fs.writeFileSync(argv[4], src3);
