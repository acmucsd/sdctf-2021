// dependencies
const express = require('express')
const bodyParser = require('body-parser')
const sqlite3 = require('sqlite3').verbose()
const md5 = require('md5')
const bcrypt = require('bcrypt')

// initial configs
const app = express()
const db = new sqlite3.Database('./users.db', err => {
	if (err)
		console.log(err)
	else 
		console.log('connected to users database')
})

app.use(bodyParser.urlencoded({extended: true}))

// corresponding login endpoint
app.post('/login', (req, res) => {
    const email = req.body.email
    const password = md5(req.body.password)
    const sql = `SELECT email, password FROM users WHERE email = ?`

    console.log("email: " + email)
    
    db.get(sql, [email], (err, row) => {
        if(err) {
            console.log('ERROR', err)
            res.sendStatus(401)
        } else if (!row) {
            res.sendStatus(401)
        } else {
            bcrypt.compare(password, row.password, (err, result) => {
                if(err) {
                    console.log(err)
                    res.sendStatus(401)
                } else if (!result)
                    res.sendStatus(401)
                else
                    res.sendFile( __dirname + '/secret.flag')
            })
        }
    })
})

// gotta make sure we don't leak important stuff!
app.all('/users.db', (req, res) => res.sendStatus(403))
app.all('/secret.flag', (req, res) => res.sendStatus(403))
app.all('/app.js', (req, res) => res.sendStatus(403))

// lastly, include all of our assets with zero side effects! :)
app.use(express.static('.'))

// now listen carefully...
app.listen(1337, err => {
	if (err)
		console.log(err)
	else
		console.log('web server now listening on port 1337...')
})