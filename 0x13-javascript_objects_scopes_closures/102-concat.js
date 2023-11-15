#!/usr/bin/node
const fs = require('fs');
const args = process.argv;
const src_a = fs.readFileSync(args[2], 'utf8');
const src_b = fs.readFileSync(args[3], 'utf8');
fs.writeFileSync(args[4], src_a + src_b);
