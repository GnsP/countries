const pug = require('pug');
const fs = require('fs');

fs.readFile('./countries.json', 'utf8', (err, data) => {
    const countries = JSON.parse(data);
    console.log(pug.renderFile('./index.pug', { countries }));
});
