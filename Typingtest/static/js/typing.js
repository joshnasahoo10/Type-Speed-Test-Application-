let startTime;
let started = false;

function startTest(){
    startTime = new Date().getTime();
    started = true;
    document.getElementById('result').textContent = 'Test started...';
    document.getElementById('saveButton').disabled = true;
}

document.getElementById('startButton').addEventListener('click', startTest);

document.getElementById('input').addEventListener('keyup', finishTest);

function finishTest(){
    if (!started) return;
    const endTime = new Date().getTime();
    const totalTime = (endTime - startTime) / 1000;
    const typed = document.getElementById('input').value.trim();
    if (!typed) return;
    const words = typed.split(/\s+/).length;
    const wpm = Math.max(0, Math.round((words / totalTime) * 60));
    document.getElementById('result').innerHTML = 'Speed: ' + wpm + ' WPM';
    document.getElementById('wpm').value = wpm;
    document.getElementById('accuracy').value = 100;
    document.getElementById('saveButton').disabled = false;
}