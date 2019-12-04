function send_config() {
  let req = new XMLHttpRequest();
  const config = {
    top_left: parseInt(document.getElementById("top-left").value),
    top_right: parseInt(document.getElementById("top-right").value),
    bot_left: parseInt(document.getElementById("bot-left").value),
    bot_right: parseInt(document.getElementById("bot-right").value),
  };

  req.open('POST', 'http://127.0.0.1:8080');
  req.setRequestHeader("Content-Type", "application/json");
  req.send(JSON.stringify(config));
}
