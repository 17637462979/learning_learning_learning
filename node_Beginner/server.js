var http = require("http");
var server = http.createServer(function(request, response){
    // console.log(request.method + ': ' + request.url);
    // response.writeHead(200, {'Content-Type': 'text/html'});
    response.end('hello world!');
})


server.listen(60001)
console.log('Server is running at http://127.0.0.1:60001');