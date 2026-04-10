import process from "node:process";
import { promises as fs } from "node:fs";

// THis will give an array without the path to node and to the file.
const argv = process.argv.slice(2);

//Get line numbers.
const showNumbers = argv.includes("-n");
const showNonBlankNumbers = argv.includes("-b");

//filter the - from the array argv as it's a flag.
const filePaths = argv.filter((arg) => !arg.startsWith("-"));
let counterLines = 1;

for (const path of filePaths) {
  try {
    const content = await fs.readFile(path, "utf-8");

    //split the text at the new line character.
    const splitLines = content.split("\n");

    splitLines.forEach((line) => {
      if (showNumbers) {
        console.log(`${counterLines++}  ${line}`);
      } else if (showNonBlankNumbers) {
        // increment and show numbers only if the line is not empty.
        if (line.trim() !== "") {
          console.log(`${counterLines++}  ${line}`);
        } else {
          // print empty lines
          console.log(line);
        }
      } else {
        console.log(line);
      }
    });
  } catch (error) {
    console.log(`Could not read: ${path}`);
  }
}
