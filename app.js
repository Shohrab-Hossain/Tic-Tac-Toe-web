// Node Module
var bodyParser       = require('body-parser'),
    express          = require('express'),
    app              = express();

// Customized Module
var landingRoutes   = require('./modules/routes/landing_routes'),               // ----- route
    TicTacToeRoutes = require('./modules/routes/tic-tac-toe_routes'),           // ----- route
    allOtherRoutes  = require('./modules/routes/all-other_routes');             // ----- route

// Initializig app.js
app.set('view engine', 'ejs');
app.use(express.static(__dirname + '/public'));
app.use(bodyParser.json());                          // the bodyParser is required while using POST request, for parsing values and application/json
app.use(bodyParser.urlencoded({ extended: true }));  // for parsing application/x-www-form-urlencoded



// |-------------------------------------------------------------------|
// |    ROUTE                                                          |
// |-------------------------------------------------------------------

app.use(landingRoutes);
app.use(TicTacToeRoutes);
app.use(allOtherRoutes);



// |-------------------------------------------------------------------|
// |    server is listenning to localhost:3000                         |
// |-------------------------------------------------------------------|

const port = process.env.PORT || 3000;        // the server will listen to this Port or 3000
const ip   = process.env.IP || '127.0.0.1';   // the server will listen to this IP or 127.0.0.1

app.listen(port, ip, function(){
    console.log(serverIsListening);  // the variable "serverIsListeningTO" is declared and defined below
});

var serverIsListening = '\n' +
                        '\t' + '|----- Status ----------------------------------------|' + '\n' +
                        '\t' + '|                                                     |' + '\n' +
                        '\t' + '|             1. Server has been started.             |' + '\n' +
                        '\t' + '|                                                     |' + '\n' +
                        '\t' + '|-----------------------------------------------------|' + '\n' ;

