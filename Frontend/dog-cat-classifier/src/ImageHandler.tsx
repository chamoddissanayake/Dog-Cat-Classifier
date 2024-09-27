import React, {useState} from 'react';
import './ImageHandler.css';

const ImageHandler: React.FC = () => {
    const [imageSrc, setImageSrc] = useState('');
    const [identified, setIdentified] = useState<any>();

    const [selectedFile, setSelectedFile] = useState<File | null>(null);
    const [uploadMessage, setUploadMessage] = useState<string>('');

    const handleFileChange = (event: React.ChangeEvent<HTMLInputElement>) => {
        const file = event.target.files ? event.target.files[0] : null;
        if (file) {
            setSelectedFile(file);
            setUploadMessage('');
        } else {
            setSelectedFile(null);
            setUploadMessage('Please select a valid image file.');
        }
    };

    const convertPath = (a: any) => a.replace('./uploads\\', 'http://localhost:5005/uploads/');

    const handleUpload = async () => {
        if (!selectedFile) {
            setUploadMessage('No file selected');
            return;
        }

        const formData = new FormData();
        formData.append('image', selectedFile);

        try {
            const response = await fetch('http://localhost:5005/upload', {
                method: 'POST',
                body: formData,
            });

            if (!response.ok) {
                const errorData = await response.json();
                setUploadMessage(`Error uploading image: ${errorData.error}`);
            } else {
                const data = await response.json();
                convertPath(convertPath(data.image_path))

                setImageSrc(convertPath(data.image_path));

                fetch("http://127.0.0.1:5005/classify", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify(data),
                })
                    .then(response => {
                        if (!response.ok) {
                            throw new Error('Network response was not ok');
                        }
                        return response.json();
                    })
                    .then(data => {
                        console.log('Success:', data);
                        setIdentified(data);
                    })
                    .catch(error => {
                        console.error('Error:', error);
                    });
                setUploadMessage(`Image uploaded successfully`);
            }
        } catch (error) {
            console.error('Error uploading image:', error);
            setUploadMessage('Unexpected error occurred during upload.');
        }
    };

    return (
        <div className="upload-container">

            <h1 className="title">Dog and Cat Classifier</h1>
            <input type="file" className="file-input" accept="image/*" onChange={handleFileChange} />
            <button className="upload-button" onClick={handleUpload}>Upload</button>
            {uploadMessage && <p className="upload-message">{uploadMessage}</p>}

            {imageSrc && (
                <img src={imageSrc} alt="Uploaded" style={{width: '300px', height: 'auto'}}/>
            )}
            {identified &&
                <div>
                    <div>This is a image of a <label><b>{identified.predictedState}</b></label></div>
                    <div><label><b>Confidence:</b>&nbsp;&nbsp;</label>{identified.confidence.toFixed(5) }</div>
                </div>
            }
        </div>
    );
};

export default ImageHandler;
