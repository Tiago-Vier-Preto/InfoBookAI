const videoElement = document.getElementById('videoElement');
const canvasElement = document.getElementById('canvasElement');
const photoElement = document.getElementById('photoElement');
const startButton = document.getElementById('startButton');
const captureButton = document.getElementById('captureButton');

let stream;

async function startWebcam() {
    try {
        stream = await navigator.mediaDevices.getUserMedia({ video: true });
        videoElement.srcObject = stream;
        startButton.disabled = true;
        captureButton.disabled = false;
    } catch (error) {
        console.error('Error accessing webcam:', error);
    }
}

startButton.addEventListener('click', startWebcam);

function capturePhoto() {
    canvasElement.width = videoElement.videoWidth;
    canvasElement.height = videoElement.videoHeight;
    canvasElement.getContext('2d').drawImage(videoElement, 0, 0);
    const photoDataUrl = canvasElement.toDataURL('image/jpeg');
    photoElement.src = photoDataUrl;
    photoElement.style.display = 'block';

    // Envia a imagem para o servidor
    fetch('/process-image', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ image: photoDataUrl })
    })
    .then(response => response.json())
    .then(data => {
        console.log('Resultado do OCR:', data.text);
        // Atualiza o conteúdo do elemento HTML com o texto do OCR
        document.getElementById('ocrResult').innerText = data.text;
    })
    .catch(error => {
        console.error('Erro ao enviar a imagem:', error);
    });
}

captureButton.addEventListener('click', capturePhoto);

