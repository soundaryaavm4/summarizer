📝 Groq Text Summarizer (Streamlit)

    A beginner-friendly single-file Streamlit app that summarizes text using the Groq LLM API.
    API keys are safely hidden using `.env`.

✅ Features

    * Text summarization with custom instructions (ex: 50 words)
    * Secure API key handling (`.env`)
    * Single Python file
    * Simple Streamlit UI
    * Beginner friendly


📁 Project Structure

```
project-folder/
│
├── app.py
├── requirements.txt
└── .env
```

🔧 Installation

     1. Install dependencies

      ```bash
          pip install -r requirements.txt
      ```

     2. Create `.env` file

      Inside your project folder:

      ```
        GROQ_API_KEY=your_groq_api_key_here
      ```

      ⚠️ Never hardcode your API key.

     ▶ Run Application

      ```bash
          streamlit run app.py
      ```

      Your browser will open automatically.

  📦 requirements.txt

    ```
    streamlit
    requests
    python-dotenv
    ```
    
 🛠 Tech Used

    * Python
    * Streamlit
    * Groq API
    * Requests
    * Dotenv

🚀 How It Works

    1. Enter text
    2. Enter instruction (example: `50 words`)
    3. Click Summarize
    4. Get AI summary instantly




