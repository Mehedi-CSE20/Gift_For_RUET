// const http = require('http')
// const fs = require('fs')
// const port = 3000

// const server = http.createServer(function(req, res) {
//     res.writeHead(200, { 'Content-Type': 'text/html' })
//     fs.readFile('Project_Ruet_Raven\\transition_login_and_signup\\raven.html', function(error, data) {
//         if (error) {
//             res.write('Error 404')
//             res.write('Error: File Not Found')
//         } else {
//             res.write(data)
//         }
//         res.end()
//     })
// })

// server.listen(port, function(error) {
//     if (error) {
//         console.log('Can\'t connect to server', error)
//     } else {
//         console.log('Server online. Listening to port ' + port)
//     }

// })


const http = require('http');
const fs = require('fs');

http.createServer(function(req, res) {
    if (req.url === "/raven.html" || req.url === "/") {
        fs.readFile('raven.html', function(err, data) {
            res.writeHead(200, { 'Content-Type': 'text/html' });
            res.write(data);
            res.end();
        });
    } else if (req.url === "/feathers_of_raven.css") {
        fs.readFile('feathers_of_raven.css', function(err, data) {
            res.writeHead(200, { 'Content-Type': 'text/css' });
            res.write(data);
            res.end();
        });
    } else if (req.url === "/raven_cript.js") {
        fs.readFile('raven_cript.js', function(err, data) {
            res.writeHead(200, { 'Content-Type': 'text/js' });
            res.write(data);
            res.end();
        });
    }
}).listen(8080);


//else if (req.url === "/page/index.html") {
//     fs.readFile('index.html', function(err, data) {
//         res.writeHead(200, { 'Content-Type': 'text/html' });
//         res.write(data);
//         res.end();
//     });
// } else if (req.url === "/page/style.css") {
//     fs.readFile('style.css', function(err, data) {
//         res.writeHead(200, { 'Content-Type': 'text/css' });
//         res.write(data);
//         res.end();
//     });
// } else if (req.url === "/page/theme.js") {
//     fs.readFile('theme.js', function(err, data) {
//         res.writeHead(200, { 'Content-Type': 'text/js' });
//         res.write(data);
//         res.end();
//     });
// }