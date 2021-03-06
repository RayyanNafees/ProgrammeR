const express = require('express');
const app = express();
const port = 3000;

app.use(express.static('static'));

app.use(express.json()); // for parsing application/json
app.use(express.urlencoded({ extended: true })); // for parsing application/x-www-form-urlencoded

app.get('/',
    (request, res) => res.send('Hello World!')
);

app.listen(port, () => console.log(`Example app listening at http://localhost:${port}`));