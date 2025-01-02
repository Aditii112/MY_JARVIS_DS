# Jarvis AI - A Virtual Desktop Assistant

## Overview
Jarvis AI is a Python-based virtual Desktop assistant that performs a variety of tasks such as:
- Web browsing
- Managing applications (e.g., Notepad, Paint)
- Speech recognition and response
- Drawing shapes in Paint
- Using OpenAI for conversational responses
- Searching Wikipedia
- Accessing the system camera

## Features
1. **Speech Recognition**
   - Listens to user commands via the microphone.
   - Recognizes voice input using the `speech_recognition` library.

2. **Speech Output**
   - Uses `pyttsx3` for text-to-speech conversion to provide audio feedback.

3. **Web Browsing**
   - Opens websites such as YouTube, Wikipedia, and Google based on voice commands.

4. **Application Management**
   - Opens system applications like Notepad and Paint.
   - Draws shapes (e.g., circles) in Paint using `pyautogui`.

5. **Wikipedia Search**
   - Searches for a topic on Wikipedia and summarizes results.

6. **Camera Access**
   - Accesses the system camera to capture and display live video.

7. **AI Interaction**
   - Utilizes OpenAI's GPT model for conversational responses.
   - Saves responses to text files for later reference.

8. **Dynamic Commands**
   - Types user-specified text dynamically.
   - Retrieves and announces the current time.

## Libraries Used
- `pyttsx3`: Text-to-speech conversion
- `datetime`: Fetching current date and time
- `speech_recognition`: Speech-to-text conversion
- `wikipedia`: Accessing Wikipedia for information
- `pyaudio`: Audio processing
- `webbrowser`: Opening web URLs
- `openai`: Integration with OpenAI's GPT model
- `cv2` (OpenCV): Camera access
- `numpy`: Array handling (used by OpenCV)
- `subprocess`: Running system-level processes
- `os`: Operating system interactions
- `pyautogui`: Automating GUI actions

## How to Use
1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd <repository_folder>
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Replace `apikey` in the `config.py` file with your OpenAI API key.
4. Run the main script:
   ```bash
   python JarvisDA.py
   ```
5. Speak into the microphone and provide commands to Jarvis, such as:
   - "Open YouTube"
   - "What is the time?"
   - "Search Wikipedia for Python programming."
   - "Open Notepad"
   - "Draw a circle."

## Command Examples
- **Web Browsing:**
  - "Open YouTube"
  - "Open Google"
- **Application Management:**
  - "Open Paint"
  - "Draw a circle"
  - "Open Notepad"
- **Wikipedia Search:**
  - "Search Wikipedia for Machine Learning"
- **AI Chat Interaction:**
  - "Using AI, write a poem about technology."
- **Dynamic Typing:**
  - "Type Hello, how are you?"

## Project Structure
```
JarvisAI/
|-- JarvisDA.py           # Main script
|-- config.py             # Configuration file for API keys
|-- requirements.txt      # List of required Python libraries
|-- Openai/               # Folder for saving AI response files
```

## Notes
- Ensure that your microphone and speakers are functional for the assistant to work effectively.
- An OpenAI API key is required for AI-based interactions.
- Customize the `draw_circle` function or add more shapes as needed using `pyautogui`.

## Dependencies
Install the following Python libraries:
- `pyttsx3`
- `datetime`
- `speech_recognition`
- `wikipedia`
- `pyaudio`
- `webbrowser`
- `openai`
- `opencv-python`
- `numpy`
- `pyautogui`

## Future Enhancements
- Adding more voice commands and functionalities.
- Enhancing the AI interaction using GPT-4 or higher models.
- Integration with third-party APIs for additional features.
- Improved error handling and user feedback.

## License
This project is licensed under the MIT License. Feel free to use, modify, and distribute it as needed.

