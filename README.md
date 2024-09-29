# Home Pod Voice Assistant - Apps not implmented - WIP

The Home Pod is an LLM voice assistant that runs on a raspberry pi. This applictaion has a display. 

This is a modification (poor one) of the HomePod Project by Concept-Bytes. All the original code can be found on the following github page https://github.com/Concept-Bytes/HomePod

Modifications from the Original Version
Transitioned to a Voice-Only Experience: 
   Removed applications related to stocks, weather, sports, smart home, and news to focus solely on voice interaction.
Eliminated Threading: 
   Removed threading to enhance stability, preventing Pygame from crashing during screen updates after the assistant thread is executed.
Enhanced Voice Options: 
   Replaced the Pygame mixer with the Piper TTS module to provide a wider variety of voice choices.
Updated Visual Elements: 
   Since this is now a voice-only project, the background image has been refreshed, and all application buttons have been removed to streamline the interface.

## Prerequisites

Before you begin, ensure you have the following:
- A Raspberry Pi set up with internet access.
- An OpenAI API key, Assistant ID, and Thread ID. You can obtain these from your OpenAI account on the [OpenAI Platform](https://platform.openai.com/assistants).
- Piper Voice - https://github.com/rhasspy/piper.git  (contains all the resources including ONNX voice files.
- Install all pip packages from the requirements.txt 

## Installation

1. **Clone the Repository**

   Open a terminal on your Raspberry Pi and run the following command to clone the repository:

   ```git clone https://github.com/jdugat/Jarvis-HomePad-Piper.git```

   Navigate into the project directory:

2. **Install Dependencies**

    Install the required Python packages:
	pip install -r ./requirements.txt --break-system-packages

3. **Configuration**

    Open `sample.env` in a text editor of your choice. Fill in your OpenAI API key, Assistant ID, and Thread ID in the designated spots. This information is critical for the AI functionality of the project and can be         obtained from your OpenAI account.

   Rename this to just .env
    
    ```python
    # Example placeholder in .env
    API_KEY = "your_openai_api_key_here"
   ASSISTANT_ID = "your_assistant_id_here"
   THREAD_ID = "your_thread_id_here"

    
## Running the Application

After completing the setup and configuration, run the application with:

```python homescreen.py```

## Contributing
Contributions to the Home Pod are welcome! Please feel free to fork the repository, make your changes, and submit a pull request.

## License
This project is licensed under the MIT License - see the LICENSE file in the repository for details.
# HomePod
