# StreamMind AI 🤖

A streamlined application that leverages OpenAI's language models through LangChain and Streamlit to create an interactive chat interface.

## Overview

This application provides a simple web interface for interacting with OpenAI's language models. Users can input text prompts and receive AI-generated responses in real-time.

## Features

- Clean, user-friendly Streamlit interface
- Integration with OpenAI's powerful language models
- Secure API key handling through environment variables
- Flexible input options for API credentials

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/StreamMind-AI.git
   cd Simple-LLM-App
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv .venv
   
   # On Windows
   .venv\Scripts\activate
   
   # On macOS/Linux
   source .venv/bin/activate
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Required Packages

- streamlit
- langchain-openai
- langchain
- python-dotenv
- openai

## Configuration

1. Create a `.env` file in the root directory with your OpenAI API key:
   ```
   OpenAI_API_KEY=sk-your-api-key-here
   ```

2. Alternatively, you can input your API key directly in the application's sidebar.

## Usage

1. Start the application:
   ```
   streamlit run app.py
   ```

2. Open your web browser to the provided local URL (typically http://localhost:8501).

3. If you haven't set up a `.env` file, enter your OpenAI API key in the sidebar.

4. Type your prompt in the text area and click "Submit" to generate a response.

## API Key Security

This application provides two methods for handling your OpenAI API key:

- **Environment Variable**: More secure for personal use, avoiding the need to enter the key each time
- **UI Input**: Convenient for shared deployments or when testing with different API keys

## Troubleshooting

### Common Errors

- **ModuleNotFoundError: No module named 'langchain_community'**: 
  Install the required package: `pip install langchain-community`

- **ModuleNotFoundError: No module named 'langchain_openai'**: 
  Install the required package: `pip install langchain-openai`

- **OpenAI API Rate Limit Error (429)**:
  You've exceeded your quota. Check your OpenAI account billing status and add credits as needed.

## License

[MIT](LICENSE)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
