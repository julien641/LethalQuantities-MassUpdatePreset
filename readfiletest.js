
console.log(JSON.parse("{}"))

const fs = require('node:fs');
fs.readFile("C:\\Users\\Placeholder1\\Desktop\\lethalconfiged\\LethalQuantities-MassUpdatePreset\\output\\Presetsupdated.json",
 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(JSON.parse(data));
});