import fs from "node:fs";
import process from "node:process";

// This will give an array without the path to node and to the file.
const argv = process.argv.slice(2);

// filter the flag to find the target folder.
const filePaths = argv.filter((arg) => !arg.startsWith("-"));
const showHiddenFiles = argv.includes("-a");

// if no folder provide we use the current one
const target = filePaths[0] || ".";
// read the file.
const files = fs.readdirSync(target);

// save the result into the variable.
let filteredFIles = files;
if (!showHiddenFiles) {
  filteredFIles = files.filter((file) => !file.startsWith("."));
} else {
  // we use spread operator to merge the paths.
  filteredFIles = [".", "..", ...files];
}

// Print using -1 .
filteredFIles.forEach((file) => {
  console.log(file);
});
