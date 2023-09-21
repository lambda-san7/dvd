//////////////////////////
// CANVAS
//////////////////////////
var running = true
    
canvas = document.getElementById("canvas")
var ctx = canvas.getContext("2d");

var speed = document.getElementById("speed")

logo = document.getElementById("logo")

width = 1366
height = 385

function render(fill=player2.fill){
    ctx.fillStyle = fill;
    ctx.fillRect(player2.x, player2.y, player2.size, player2.size);
    ctx.stroke();
}

flipped_x = false
flipped_y = false

corners = 0

var dvd = {
    x: 50,
    y: 50,
    w: 92,
    h: 21,
    horizontal: 10,
    vertical: 10,
    handle: function(){
        flipped_x = false
        flipped_y = false
        dvd.x += dvd.horizontal
        dvd.y += dvd.vertical
        if(dvd.x + dvd.horizontal <= 0){
            dvd.horizontal += dvd.horizontal * -2
            flipped_x = true
        }
        if(dvd.y + dvd.vertical <= 0){
            dvd.vertical += dvd.vertical * -2
            flipped_y = true
        }
        if((dvd.x + dvd.horizontal) + dvd.w >= width){   
            dvd.horizontal -= dvd.horizontal * 2
            flipped_x = true
        }
        if((dvd.y + dvd.vertical) + dvd.h >= height){
            dvd.vertical -= dvd.vertical * 2
            flipped_y = true
        }
        if(flipped_x && flipped_y){
            corners += 1
        }
        ctx.drawImage(logo,dvd.x,dvd.y,dvd.w,dvd.h)
        ctx.stroke()
    }
}

function inc_speed(amount){
    speed.innerHTML = amount
    console.log(dvd.horizontal,dvd.vertical)
    if(dvd.horizontal < 0){
        dvd.horizontal -= amount
    }
    if(dvd.horizontal >= 0){
        dvd.horizontal += amount
    }
    if(dvd.vertical < 0){
        dvd.vertical -= amount
    }
    if(dvd.vertical >= 0){
        dvd.vertical += amount
    }
    
}

function dec_speed(amount){
    console.log(dvd.horizontal,dvd.vertical)
    if(dvd.horizontal < 0){
        dvd.horizontal += amount
    }
    if(dvd.horizontal >= 0){
        dvd.horizontal -= amount
    }
    if(dvd.vertical < 0){
        dvd.vertical += amount
    }
    if(dvd.vertical >= 0){
        dvd.vertical -= amount
    }
}

function change_speed(amount){
    console.log(dvd.horizontal,dvd.vertical)
    dvd.horizontal = amount
    dvd.vertical = amount
}

//////////////////////////
// LOOP
//////////////////////////
    
function loop(){
    setTimeout(function(){
        ctx.clearRect(0, 0, 99999, 99999);
        dvd.handle(dvd.x,dvd.y,dvd.w,dvd.h)
        speed.innerHTML = dvd.horizontal
        loop()
    }, 16);
}
      
loop()
  