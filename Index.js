const PORT = 8000;
const express = require("express");
const cors = require("cors");
const path = require("path");
const bodyParser = require("body-parser");
const mongoose = require("mongoose");

const app = express();
app.use(cors());
app.use(express.json());

const staticPath = path.join("C:\\Thejas\\Hackathon");
app.use(express.static(staticPath));

// MongoDB Atlas connection string
const mongoURI = 'mongodb+srv://Thejas:pNRrNxnPA9sZeavr@cluster0.z2gkx0c.mongodb.net/mydb?retryWrites=true&w=majority&appName=Cluster0';

mongoose.connect(mongoURI, { useNewUrlParser: true, useUnifiedTopology: true });
const db = mongoose.connection;

db.on('error', (err) => {
    console.error('Error in connecting to database:', err);
});

db.once('open', () => {
    console.log('Connected to MongoDB');
});

// POST endpoint for user signup
app.post('/Signup', async (req, res) => {
    var email = req.body.email;
    var password = req.body.password;
    var confirm_password = req.body.confirm_password;

    // Check if password matches confirm_password
    if (password !== confirm_password) {
        return res.status(400).send("Passwords do not match");
    }

    var userData = {
        "email": email,
        "password": password,
    };

    try {
        const result = await db.collection('users').insertOne(userData);
        console.log("Record inserted successfully:", result.insertedId);
        return res.redirect('Signup.html');
    } catch (err) {
        console.error('Error inserting record:', err);
        return res.status(500).send('Internal Server Error');
    }
});

// Middleware to parse JSON bodies
app.use(bodyParser.json());

// Serve static files from the 'public' directory
app.use(express.static('public'));

// Middleware to parse URL-encoded bodies
app.use(bodyParser.urlencoded({ extended: true }));

// Redirect root URL to index.html
app.get("/", (req, res) => {
    res.set({
        "Allow-access-Allow-Origin": '*'
    });
    const indexPath = path.join(staticPath, 'index.html');
    return res.sendFile(indexPath);
});

// Start the server
app.listen(PORT, () => {
    console.log("Server is running on PORT", PORT);
});
