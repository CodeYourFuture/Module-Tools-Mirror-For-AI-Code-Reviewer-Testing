#!/usr/bin/env node

const fs = require('fs');
const path = require('path');

function cat(files, options) {
  let lineNumber = 1;

  files.forEach((file) => {
    const filePath = path.resolve(file);

    try {
      const data = fs.readFileSync(filePath, 'utf8');
      const lines = data.split('\n');

      lines.forEach((line) => {
        if (options.numberNonEmpty && line.trim()) {
          console.log(`${lineNumber}\t${line}`);
          lineNumber++;
        } else if (options.numberLines) {
          console.log(`${lineNumber}\t${line}`);
          lineNumber++;
        } else {
          console.log(line);
        }
      });
    } catch (err) {
      console.error(`cat: ${file}: No such file or directory`);
    }
  });
}

function main() {
  const args = process.argv.slice(2);
  const options = {
    numberLines: false,
    numberNonEmpty: false,
  };

  const files = [];

  args.forEach((arg) => {
    if (arg === '-n') {
      options.numberLines = true;
    } else if (arg === '-b') {
      options.numberNonEmpty = true;
    } else {
      files.push(arg);
    }
  });

  if (files.length === 0) {
    console.error('Usage: node cat.js [-n | -b] <file>...');
    process.exit(1);
  }

  cat(files, options);
}

main();