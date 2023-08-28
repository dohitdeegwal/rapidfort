const fileInput = document.getElementById('fileInput');
const metadataDisplay = document.getElementById('metadataDisplay');
const uploadMessage = document.getElementById('uploadMessage');
const uploadProgress = document.getElementById('uploadProgress');

// Function to format a timestamp
function formatTimestamp(timestamp) {
    const date = new Date(timestamp * 1000); // Convert seconds to milliseconds
    return date.toLocaleString(); // Format the date as a user-friendly string
}

// Function to display metadata in a user-friendly format
function displayMetadata(metadata) {
    metadataDisplay.innerHTML = ''; // Clear any previous metadata

    // Create a <ul> element to hold the metadata items
    const list = document.createElement('ul');

    for (const key in metadata) {
        if (metadata.hasOwnProperty(key)) {
            // Check if the key matches a pattern for timestamp keys
            if (key.toLowerCase().includes('time') && typeof metadata[key] === 'number') {
                metadata[key] = formatTimestamp(metadata[key]);
            }

            // Create a <li> element for each metadata item
            const listItem = document.createElement('li');
            listItem.innerHTML = `<strong>${key}:</strong> ${metadata[key]}`;

            // Append the <li> element to the <ul>
            list.appendChild(listItem);
        }
    }

    // Append the <ul> to the metadataDisplay div
    metadataDisplay.appendChild(list);
}

// Send POST request to server to upload file and get metadata
fileInput.addEventListener('change', (event) => {
    const file = event.target.files[0];
    const formData = new FormData();
    formData.append('file', file);

    // Show the uploading message and progress bar
    uploadMessage.style.display = 'block';
    uploadProgress.style.display = 'block';

    // Clear any previous metadata
    metadataDisplay.innerHTML = '';

    const xhr = new XMLHttpRequest();

    xhr.upload.addEventListener('progress', (e) => {
        if (e.lengthComputable) {
            const percentComplete = (e.loaded / e.total) * 100;
            uploadProgress.value = percentComplete;
        }
    });

    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4) {
            if (xhr.status === 200) {
                const data = JSON.parse(xhr.responseText);
                displayMetadata(data);
            } else {
                console.error('Error:', xhr.statusText);
            }

            // Hide the uploading message and progress bar when the response is received
            uploadMessage.style.display = 'none';
            uploadProgress.style.display = 'none';
            // Reset the progress bar value
            uploadProgress.value = 0;
        }
    };

    xhr.open('POST', '/upload', true);
    xhr.send(formData);
});
