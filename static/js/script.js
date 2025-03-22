// 🎵 Audio Setup
let buttonSound = new Audio('/static/sounds/video-game-bio-gun-sfx-203965.mp3');
let wrongGuessSound = new Audio('/static/sounds/080047_lose_funny_retro_video-game-80925.mp3');
let hintSound = new Audio('/static/sounds/in-game-level-uptype-2-230567.mp3');
let winSound = new Audio('/static/sounds/you-win-sequence-2-183949.mp3');
let loseSound1 = new Audio('/static/sounds/calm-god-dammit-82692.mp3');
let loseSound2 = new Audio('/static/sounds/game-over-38511.mp3');

let backgroundMusic;

// 🎥 Dynamic Background Video and Audio Setup
function playBackgroundMusic(page) {
    if (backgroundMusic) {
        backgroundMusic.pause();
    }

    if (page === 'index') {
        backgroundMusic = new Audio('/static/sounds/low-energy-197725.mp3');
        changeBackgroundVideo('/static/video/3130182-uhd_3840_2160_30fps.mp4');
    } else if (page === 'game') {
        backgroundMusic = new Audio('/static/sounds/low-energy-197725.mp3');
        changeBackgroundVideo('/static/video/3141207-uhd_3840_2160_25fps.mp4');
    } else if (page === 'result-win') {
        backgroundMusic = new Audio('/static/sounds/you-win-sequence-2-183949.mp3');
        changeBackgroundVideo('/static/video/6265099-uhd_2160_3840_30fps.mp4');
    } else if (page === 'result-lose') {
        loseSound1.play();
        setTimeout(() => {
            loseSound2.play();
        }, 2000);
        changeBackgroundVideo('/static/video/7915046-hd_1080_1920_30fps.mp4');
        return; // Prevent background music for loss
    }

    backgroundMusic.loop = true;
    backgroundMusic.play();
}

// 🎥 Change Background Video Dynamically
function changeBackgroundVideo(videoPath) {
    let bgVideo = document.getElementById('bg-video');
    if (bgVideo) {
        bgVideo.src = videoPath;
        bgVideo.load();
        bgVideo.play();
    }
}

// 🎮 Button Sound Effects
function playButtonSound() {
    buttonSound.play();
}

// ❌ Wrong Guess Sound
function playWrongGuessSound() {
    wrongGuessSound.play();
}

// 💡 Play Hint Sound
function playHintSound() {
    hintSound.play();
}

// 🏆 Play Win Sound
function playWinSound() {
    winSound.play();
}

// 🕹️ Page Load Initialization
window.onload = function () {
    let page = document.body.getAttribute('data-page');
    playBackgroundMusic(page);
};
