const express = require("express");
const http = require("http");
const socketIo = require("socket.io");
const axios = require("axios");
const port = process.env.PORT || 4001;
const index = require("./routes/index");
const app = express();
app.use(index);
const server = http.createServer(app);
const io = socketIo(server); // < Interesting!


var idx = 0;

const MULTIPLE_SOURCES = [
  { src: 'http://clips.vorwaerts-gmbh.de/big_buck_bunny.mp4', type: 'video/mp4' },
  { src: 'https://www.youtube.com/watch?v=2kKIksV1aAw', type: 'video/ogv' },
  { src: 'http://clips.vorwaerts-gmbh.de/big_buck_bunny.webm', type: 'video/webm' }
]


const getApiAndEmit = async socket => {
    try {
      idx = (idx+1) % MULTIPLE_SOURCES.length
      res = MULTIPLE_SOURCES[idx].src
      socket.emit("FromAPI", res); // Emitting a new message. It will be consumed by the client
      console.log(res)
    } catch (error) {
      console.error(`Error: ${error.code}`);
    }
  };

io.on("connection", socket => {
    console.log("New client connected"), setInterval(
      () => getApiAndEmit(socket),
      10000
    );
    socket.on("disconnect", () => console.log("Client disconnected"));
  });

server.listen(port, () => console.log(`Listening on port ${port}`));
