This project implements a speech-to-text assistant named David that interacts with OpenAI's GPT-3.5-turbo model. The assistant can recognize speech, generate responses, capture the screen, and extract text from images. 

## Features

- Recognizes speech using Google's speech recognition API.
- Generates text responses using OpenAI's GPT-3.5-turbo model.
- Captures the screen and extracts text using OCR.
- Converts text to speech using OpenAI's text-to-speech API.

## Prerequisites

- Python 3.6+
- OpenAI API Key
- Google Cloud Speech-to-Text API (for speech recognition)
- Tesseract OCR

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/yourusername/david-assistant.git
    cd david-assistant
    ```
2. **Create and activate a virtual environment:**

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```
3. **Install the required packages:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Install Tesseract OCR:**

    - On macOS: brew install tesseract
    - On Ubuntu: sudo apt-get install tesseract-ocr
    - On Windows: Download and install from the official site.

5. **Create an .env file and add your OpenAI API key:**

    ```sh
    touch .env
    ```
    ```
    Plain text
    API_KEY=<your_openai_api_key>
    ```

6. **Edit the chatbot.txt file:**

    ```
    Hello, my name is <your_name>. You are my assistant, <assistant_name>.
    ```


