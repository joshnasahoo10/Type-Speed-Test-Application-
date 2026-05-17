let startTime;

function startTest(){

startTime = new Date().getTime();

}

let input = document.getElementById("input");

input.addEventListener("keyup",finishTest);

function finishTest(){

let endTime = new Date().getTime();

let totalTime = (endTime-startTime)/1000;

let text = input.value;

let words = text.split(" ").length;

let wpm = Math.round((words/totalTime)*60);

document.getElementById("result").innerHTML = "Speed: "+wpm+" WPM";

}