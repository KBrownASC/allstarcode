background(255)
size(400,400)



#car function
def makeCar(colr,wheel):
    if wheel== "Black":
        fill(1)
    if wheel== "Red":
        fill(255,0,0)
    if wheel== "Blue":
        fill(0,0,255)
    if wheel== "White":
        fill(255)
    if wheel== "Green":
        fill(0,255,0)
    if wheel== "Yellow":
        fill(188,188,0)
    if wheel== "Orange":
        fill(200,0,200)    
    ellipse(195,220,40,50)
    if wheel== "Black":
        fill(1)
    if wheel== "Red":
        fill(255,0,0)
    if wheel== "Blue":
        fill(0,0,255)
    if wheel== "White":
        fill(255)
    if wheel== "Green":
        fill(0,255,0)
    if wheel== "Yellow":
        fill(188,188,0)
    if wheel== "Orange":
        fill(200,0,200) 
    ellipse(235,220,40,50)    
    
    
    
    if colr == "Red":
        fill(255,0,0)
    if colr == "Blue":
        fill(0,0,255)
    if colr == "Green":
        fill(0,255,0)
    
    rect(175,200,80,40)
         

   
    
    
    

makeCar("Green","Yellow")