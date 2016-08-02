
var hoop;
var canvas; 


function setup() {
	canvas = createCanvas(800,800);
	
}

function draw() {
	background(220,180,90);
	hoop = loadImage("hoop.png");
	image(hoop,0,0);

}