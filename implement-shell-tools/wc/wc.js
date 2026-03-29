#!/usr/bin/env node

const fs = require('fs');
const path = require('path');

function countFile(filePath, options) {
  try {
    const data = fs.readFileSync(filePath, 'utf8');

    const lines = data.split('\n').length;
    const words = data.split(/\s+/).filter(Boolean).length;
    const bytes = Buffer.byteLength(data, 'utf8');

    if (options.lines) {
      console.log(`${lines}\t${filePath}`);
    } else if (options.words) {
      console.log(`${words}\t${filePath}`);
    } else if (options.bytes) {
      console.log(`${bytes}\t${filePath}`);
    } else {
      console.log(`${lines}\t${words}\t${bytes}\t${filePath}`);
    }
  } catch (err) {
    console.error(`wc: ${filePath}: No such file or directory`);
  }
}

function main() {
  const args = process.argv.slice(2);
  const options = {
    lines: false,
    words: false,
    bytes: false,
  };

  const files = [];

  args.forEach((arg) => {
    if (arg === '-l') {
      options.lines = true;
    } else if (arg === '-w') {
      options.words = true;
    } else if (arg === '-c') {
      options.bytes = true;
    } else {
      files.push(arg);
    }
  });

  if (files.length === 0) {
    console.error('Usage: wc [-l | -w | -c] <file>...');
    process.exit(1);
  }

  files.forEach((file) => {
    const filePath = path.resolve(file);
    countFile(filePath, options);
  });
}

main();