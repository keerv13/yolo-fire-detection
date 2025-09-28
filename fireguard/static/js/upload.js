document.addEventListener("DOMContentLoaded", () => {
    console.log("upload.js is running!");

    const imageUpload = document.getElementById('imageUpload');
    const detectBtn = document.getElementById('detectBtn');
    const selectedFile = document.getElementById('selectedFile');
    const uploadBox = document.getElementById('uploadBox');
    const reuploadBtn = document.getElementById('reuploadBtn');
    const uploadText = document.getElementById('uploadText');
    const chooseBtn = document.getElementById('chooseBtn');
    const buttonRow = document.getElementById('buttonRow');

    function handleFileSelected(file) {
        if (file) {
            detectBtn.disabled = false;

            // Hide instructions + choose file button
            uploadText.style.display = "none";
            chooseBtn.style.display = "none";

            // Show Detect + Reupload buttons
            buttonRow.style.display = "flex";

            // Disable drag & drop
            uploadBox.style.pointerEvents = "none";

            // Show image preview in same position
            const reader = new FileReader();
            reader.onload = function(e) {
                selectedFile.innerHTML = `<img src="${e.target.result}" class="preview-image">`;
            };
            reader.readAsDataURL(file);
        }
    }



    if (imageUpload) {
        // File chosen via click
        imageUpload.addEventListener('change', (e) => {
            if (e.target.files.length > 0) {
                handleFileSelected(e.target.files[0]);
            }
        });
    }

    if (uploadBox) {
        // Drag & drop
        uploadBox.addEventListener('dragover', (e) => {
            e.preventDefault();
            uploadBox.classList.add('dragover');
        });
        uploadBox.addEventListener('dragleave', (e) => {
            e.preventDefault();
            uploadBox.classList.remove('dragover');
        });
        uploadBox.addEventListener('drop', (e) => {
            e.preventDefault();
            uploadBox.classList.remove('dragover');
            const files = e.dataTransfer.files;
            if (files.length > 0) {
                imageUpload.files = files;
                handleFileSelected(files[0]);
            }
        });
    }

    if (reuploadBtn) {
        // Reupload resets everything
        reuploadBtn.addEventListener('click', () => {
            imageUpload.value = "";
            selectedFile.innerHTML = "";
            detectBtn.disabled = true;

            // Show instructions + choose file again
            uploadText.style.display = "block";
            chooseBtn.style.display = "inline-block";

            // Hide Detect/Reupload
            buttonRow.style.display = "none";

            document.getElementById('uploadForm').reset();

            // Re-enable drag & drop
            uploadBox.style.pointerEvents = "auto";

            // Remove old results if they exist
            const resultsWrapper = document.getElementById('resultsWrapper');
            if (resultsWrapper) {
                resultsWrapper.remove();
            }
        });
    }
});
