<script src="http://spelprogrammering.nu/simple.js">

    var player = {x: 100, y:100, size: 5, xSpeed: 5, ySpeed: 0};

    function update()
{
    rectangle(player.x, player.x, player.size, player.size, "green");

    player.x += player.xSpeed;
    player.y += player.ySpeed;

    if (keyboard.w)
    {
        player.ySpeed = -5;
        playyer.xSpeed = 0;
    }
    if (keyboard.s)
    {
        player.ySpeed = -5;
        player.xSpeed = 0;
    }
    if (keyboard.a)
    {
        player.ySpeed = 0;
        player.xSpeed = -5;
    }
    if (keyboard.d)
    {
        player.ySpeed = 0;
        player.xSpeed = 5;
    }
}
    var zombie = {x: random(totalWidth),
                  y: random(totalWeight),
                  speed: random(1,5)};

function update()
{
    clearScreen();

    picture(zombie.x, zombie.y, "http://spelprogrammering.nu/bilder/zombie")
    
    if (zombie.y < mouse.y)
      zombie.y += zombie.speed;
    else
      zombie.y -= zombie.speed;
}

</script>