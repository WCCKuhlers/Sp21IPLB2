var snakeArray;
var direction;
var score;
var bestScore;
var gamePlaying;
var appleX;
var appleY;

function setup() {
    noLoop();
    gamePlaying = false;
    createCanvas(400, 480);
    frameRate(5);
    score = 0;
    bestScore = loadBestScore();

    snakeArray = [];
    makeSnakePiece(60,200);
    makeSnakePiece(40,200);
    makeSnakePiece(20,200);

    appleX = 200;
    appleY = 200;

    direction = ("RIGHT");

    textsize(18);
}

function draw() {
    background(255);
    displayScore();
    if(gamePlaying) {
        addApple();
        drawSnake();
    } else {
        textAlight(CENTER);
        text('Press UP, RIGHT, or DOWN arrow keys to begin', width / 2, height / 2);
        Fill(0,255,0);
        for(var i = 0; i < snakeArray.length; i++) {
            Rect(snakeArray[i].xPos, snakeArray[i].yPos, 19, 19);
        }
        addApple();
    }
}


