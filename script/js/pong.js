var player = document.querySelector('.player');
	websocket = new WebSocket("ws://" + window.location.hostname + ":6789/");

function upPressed() {
	websocket.send(JSON.stringify({action: "up"}));
}

function downPressed() {
	websocket.send(JSON.stringify({action: "down"}));
}

function mouseReleased() {
	websocket.send(JSON.stringify({action: "none"}));
}

function startPressed() {
	websocket.send(JSON.stringify({action: "start"}));
}

websocket.onmessage = function (event) {
	data = JSON.parse(event.data);
	player.textContent = data.player;
};

document.getElementsByClassName("start")[0].addEventListener("mousedown", startPressed);
document.getElementsByClassName("start")[0].addEventListener("touchstart", startPressed);
document.getElementsByClassName("up")[0].addEventListener("mousedown", upPressed);
document.getElementsByClassName("down")[0].addEventListener("mousedown", downPressed);
document.getElementsByClassName("up")[0].addEventListener("touchstart", upPressed);
document.getElementsByClassName("down")[0].addEventListener("touchstart", downPressed);
document.getElementsByClassName("buttons")[0].addEventListener("mouseup", mouseReleased);
document.getElementsByClassName("buttons")[0].addEventListener("touchend", mouseReleased);
