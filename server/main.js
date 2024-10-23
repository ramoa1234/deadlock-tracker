const express = require('express');
const port = 3000;
const app = express();
const axios = require('axios')
require('dotenv').config()

import { MongoClient } from "mongodb"
import { createClient } from 'redis';

const characters_collection = process.env.characters_collection;
const items_collection = process.env.items_collection;


const client = createClient()
await client.connect()


//connect to database lookup character info and store in redis
function store_in_cache() {



}



app.get('/characters/:name', (req, res) => {

})


async function api_fetch(species) {
    const api_response = await axios.get(
        `http://localhost:3000/api`
    )
    console.log(`api call has been made${api_response}`)
    return api_response
}



app.listen(port, function() {
    console.log(`listing on port:${port}`)
})