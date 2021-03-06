var canvas = document.getElementById("game");
var scoreElement = document.getElementById("score")
var highScore = document.getElementById("highscore")
var currentScore = document.getElementById("currentscore")
var title = document.getElementById("title")
var ctx=canvas.getContext('2d');
var square=400
var scale=square/40
canvas.width = square;
canvas.height = square;
scoreElement.style.width = `${square}px`;
scoreElement.style.height = `${square / 10}px`;

var points = 0
var highPoints =0;
var tail = 2

title.innerHTML = "SnakeGame"
highScore.innerHTML = `High Score : ${highPoints}`

var dx=scale;
var dy=0;
document.addEventListener('keydown', (event) => {
    if (event.keyCode == 37 && dx != scale){
        dx = -scale;
        dy = 0;
    }
    else if (event.keyCode == 38 && dy != scale){
        dx = 0;
        dy = -scale;
    }
    else if (event.keyCode == 39 && dx != -scale){
        dx = scale;
        dy = 0;
    }
    else if (event.keyCode == 40 && dy != -scale){
        dx = 0;
        dy = scale;
    }
})

var snakeHead = {
    x: Math.floor(Math.random() * square/scale)*scale,
    y: Math.floor(Math.random() * square/scale)*scale
};
var snakeTail = [
    {
        x:snakeHead.x-scale,
        y:snakeHead.y
    },
    {
        x:snakeHead.x-scale*2,
        y:snakeHead.y
    }
]

    
function snakeDraw(){
    if (snakeHead.x >= canvas.width) {
        snakeHead.x = 0;
    }
    if (snakeHead.x < 0) {
        snakeHead.x = canvas.width + dx;
    }
    if (snakeHead.y >= canvas.height) {
        snakeHead.y = 0;
    }
    if (snakeHead.y < 0) {
        snakeHead.y = canvas.height + dy;
    }

    snakeTail.unshift({
        x: snakeHead.x,
        y: snakeHead.y
    })
     snakeHead.x += dx;
     snakeHead.y += dy;

    for (var i = 0; i < snakeTail.length; i++) {
        if (snakeTail[i].x === snakeHead.x && snakeTail[i].y === snakeHead.y) {
            gameOver()
            break;
        }
    }
    
    while (snakeTail.length > tail) {
        snakeTail.pop()
    }
    ctx.fillStyle = "#d9d5ca";
    ctx.fillRect(snakeHead.x, snakeHead.y, scale, scale);
    snakeTail.forEach(tail => {
        ctx.fillRect(tail.x, tail.y, scale, scale)
    })
}


let foodAvailable = false
var food;
function generateFood(){
    if (!foodAvailable){
        food = {
            x: Math.floor(Math.random() * square/scale)*scale,
            y: Math.floor(Math.random() * square/scale)*scale
        };
        foodAvailable=true
    }
    else if (snakeHead.x === food.x && snakeHead.y === food.y) {
        points += 1;
        tail +=1;
        foodAvailable = false;
        console.log(points)
    };
    ctx.fillStyle = "#bab8f2";
    ctx.fillRect(food.x, food.y, scale, scale)
}

function gameOver(){
    tail=2;
    if (points>highPoints){
        highPoints=points;
    }
    highScore.innerHTML = `High Score : ${highPoints}`;
    points = 0;
    snakeHead = {
        x: Math.floor(Math.random() * square / scale) * scale,
        y: Math.floor(Math.random() * square / scale) * scale
    };
    snakeTail = [
        {   
            x: snakeHead.x - scale,
            y: snakeHead.y
        },
        {
            x: snakeHead.x - scale * 2,
            y: snakeHead.y
        }
    ];
    setInterval(function(){
        ctx.font = "40px Comic Sans MS";
        ctx.fillStyle = "red";
        ctx.textAlign = center;
        ctx.fillText("Game Over", canvas.width / 2, canvas.height / 2);
    },1000)
}


function animate() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    snakeDraw();
    generateFood();
    currentScore.innerHTML = `Score : ${points}`;
}

setInterval(animate, 1000 / 15)