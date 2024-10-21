const express = require('express');
const port = 3000;
const app = express();



app.listen(port, function() {
    console.log(`listing on port:${port}`)
})