let startTime = Date.now();
function updateTime() {
    let timeElapsed = Math.floor((Date.now() - startTime) / 1000);
    document.getElementById("timer").innerText = "Time: " + timeElapsed + "s";
}
setInterval(updateTime, 1000);
