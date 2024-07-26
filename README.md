# OCR - Convert Image to Text

"OCR - Convert Image to Text" is a powerful web application that leverages the capabilities of Optical Character Recognition (OCR) to extract text from images. Built using Flask, and PaddleOCR, this tool provides an intuitive and efficient solution for converting image content into editable text.

## Features

- **Accurate Text Extraction**: Utilizes PaddleOCR for high-precision text recognition.
- **User-Friendly Interface**: Simple and attractive UI for easy interaction.
- **Image Upload**: Supports various image formats for uploading.
- **Text Output**: Displays extracted text in a scrollable container.
- **Copy to Clipboard**: One-click copy button to quickly copy the extracted text.
- **Responsive Design**: Ensures a seamless experience across different devices.

## Usage

1. **Upload Image**: Select and upload an image containing text.
2. **Extract Text**: Click on the "Upload and Extract Text" button to process the image.
3. **View and Copy**: The extracted text is displayed in a text container with an option to copy it to the clipboard.

## Installation

To set up the application locally, follow these steps:

1. **Clone the repository**:
    ```sh
    git clone https://github.com/HussainNasirKhan/OCR-Convert-Image-to-Text.git
    cd OCR-Convert-Image-to-Text
    ```

2. **Install dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

3. **Run the application**:
    ```sh
    python app.py
    ```

4. **Open your browser** and navigate to `http://127.0.0.1:5000` to use the application.

## Technologies Used

- **Flask**: For backend and server-side logic.
- **PaddleOCR**: For optical character recognition.
- **HTML/CSS**: For the front-end interface.
- **JavaScript**: For interactivity and copy-to-clipboard functionality.

## Contributions

Contributions are welcome! Feel free to open issues or submit pull requests for any enhancements or bug fixes.
