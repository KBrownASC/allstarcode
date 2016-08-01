
var ballx = 20
var bally = 20

function setup(){
	createCanvas(500, 500);
}
function draw(){
	background(0);


	fill(0,255,0)
	stroke(0,255,0)
	rect(-1,-1,502,50)
	stroke(0,255,0)
	rect(-1,150,502,50)
	stroke(0,255,0)
	rect(-1,250,502,50)
	stroke(0,255,0)
	rect(450,-1,50,200)
	stroke(0,255,0)
	rect(0,200,50,100)
	stroke(0,255,0)
	rect(450,300,50,150)
	stroke(0,255,0)
	rect(0,450,500,50)

	fill(0,180,180)
	rect(0,450,50,50)
	
	fill(0,0,0)
	ellipse(ballx,bally,30,30)
	if (keyIsDown(RIGHT_ARROW))
		ballx+=5;
	if (keyIsDown(LEFT_ARROW))
		ballx-=5;
	if (keyIsDown(UP_ARROW))
		bally-=5;
	if (keyIsDown(DOWN_ARROW))
		bally+=5;
}