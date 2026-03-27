import process, { exit } from "node:process";
import fs from "node:fs";

const argv = process.argv.slice(2);

const showWords = argv.includes("-w");
const showLines = argv.includes("-l");
const showBytes = argv.includes("-c");
const showCharacters = argv.includes("-m");

//  filter flags, and getting the string of filename
const filePaths = argv.filter((arg) => !arg.startsWith("-"));

const noFlags = !showLines && !showCharacters && !showWords && !showCharacters;
if (!filePaths) {
  console.error("PLease provide a file path");
  process.exit(1);
}
// loop trough the array to get each file path.
filePaths.forEach((filePath) => {
  const content = fs.readFileSync(filePath, "utf-8");

  const lines = content.split("\n").length - 1;
  const words = content
    .trim()
    .split(/\s+/)
    .filter((word) => word != "").length;
  // here I used Buffer.byteLength even if characters and bytes can be the same number .length, however sometimes an emoji or special characters can be heavier 2b or 4b
  const bytes = Buffer.byteLength(content);
  const characters = content.length;

  let output = "";

  if (showLines || noFlags) output += `${lines} `;
  if (showWords || noFlags) output += `${words} `;
  if (showBytes || noFlags) output += `${bytes} `;
  if (showCharacters || noFlags) output += `${characters} `;

  console.log(`${output} ${filePath}`);
});
