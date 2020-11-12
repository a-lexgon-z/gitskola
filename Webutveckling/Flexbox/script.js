setInterval(showTime, 1000); 
function showTime() { 
    let time = new Date(); 
    let hour = time.getHours(); 
    let min = time.getMinutes(); 
    let sec = time.getSeconds(); 
    am_pm = "AM"; 
// Första raderna är bara för att få sek, min och timmarna påbörjar funktionen
    if (hour > 12) { 
        hour -= 12; 
        am_pm = "PM"; 
    } 
    if (hour == 0) { 
        hr = 12; 
        am_pm = "AM"; 
    } 
// Det här behövs bara för att få AM och PM fungera
    hour = hour < 10 ? "0" + hour : hour; 
    min = min < 10 ? "0" + min : min; 
    sec = sec < 10 ? "0" + sec : sec; 

    let currentTime = hour + ":" 
            + min + ":" + sec + am_pm; 
// Får själva klockan att fungera får den att regristrera nuvarande tiden
    document.getElementById("clock") 
            .innerHTML = currentTime; // hämtar klockan från html
} 
showTime(); // visar tiden