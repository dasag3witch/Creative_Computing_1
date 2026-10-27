let socket;
let sensorValue = 0;

function setup() {
  createCanvas(600, 400);

  socket = new WebSocket("ws://localhost:8765");

  socket.onopen = () => {
    console.log("Connected to Python bridge");
  };

  socket.onmessage = (event) => {
    sensorValue = Number(event.data);
  };
}

function draw() {
  background(240);

  let diameter = map(sensorValue, 0, 1023, 20, 300);

  circle(width / 2, height / 2, diameter);
}
