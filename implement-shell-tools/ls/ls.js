#!/usr/bin/env node

const fs = require('fs');
const path = require('path');

function listFiles(directory, options) {
  try {
    const files = fs.readdirSync(directory, { withFileTypes: true });

    files.forEach((file) => {
      if (!options.all && file.name.startsWith('.')) {
        return; // Skip hidden files unless -a is specified
      }
      console.log(file.name);
    });
  } catch (err) {
    console.error(`ls: cannot access '${directory}': No such file or directory`);
  }
}

function main() {
  const args = process.argv.slice(2);
  const options = {
    all: false,
  };

  let directories = ['.'];

  args.forEach((arg) => {
    if (arg === '-1') {
      // -1 is the default behavior, so no action needed
    } else if (arg === '-a') {
      options.all = true;
    } else {
      directories = [arg];
    }
  });

  directories.forEach((directory) => {
    listFiles(directory, options);
  });
}

main();