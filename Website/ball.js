
var hoop;
var canvas; 


function setup() {
	canvas = createCanvas(800,800);
	hoop = loadImage("hoop.png");
}

function draw() {
	background(220,180,90);
	image(hoop,0,0);

}