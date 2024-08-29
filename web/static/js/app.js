const video = document.getElementById('video');
const canvas = document.getElementById('canvas');
const captureButton = document.getElementById('capture-button');

// Solicita acesso à câmera
navigator.mediaDevices.getUserMedia({ video: true })
    .then((stream) => {
        video.srcObject = stream;
        video.play();
    })
    .catch((err) => {
        console.error('Erro ao acessar a câmera: ', err);
    });

// Captura a imagem da câmera quando o botão é clicado
captureButton.addEventListener('click', () => {
    const context = canvas.getContext('2d');
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;
    context.drawImage(video, 0, 0, canvas.width, canvas.height);

    // Opcional: exibe a foto capturada
    const imgDataUrl = canvas.toDataURL('image/png');
    console.log(imgDataUrl);  // Exibe a URL da imagem capturada
});
