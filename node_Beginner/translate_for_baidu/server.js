
var http = require('http')
var querystring= require('querystring');
var s = require('./transapi_sign')
var url = require('url');
var server = http.createServer(function(request, respsone){
    var params = url.parse(request.url, true).query;
    query = querystring.stringify(params.query)
    sign = get_sign(query)
    // console.log(sign)
    // respsone.end('translate for baidu is running')
    respsone.end(sign)
})
function get_sign(query){
    sign =s.e(query)
    console.log(sign)
    return sign
}
server.listen('60002')

