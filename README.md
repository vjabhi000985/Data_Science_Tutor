# 🤖 Data Science Tutor Chat

This Streamlit application provides an interactive data science tutor powered by Google's Gemini 1.5 Pro language model. You can ask questions about data science concepts, request code examples, and receive explanations in a conversational format.

## Deployment URL :
https://data-science-tutor-zen.streamlit.app

## Features

- **Interactive Chat Interface:** Engage in a natural conversation with the AI tutor.
- **Data Science Concepts:** Get explanations of various data science topics.
- **Code Examples:** Request and receive Python code examples.
- **Contextual Memory:** The tutor remembers previous conversations, providing contextually relevant answers.
- **Customizable Sidebar:** Settings and information are displayed in a sidebar.
- **Custom CSS:** The application is styled with custom CSS for an improved user experience.
- **Page Title and Logo:** The browser tab displays a custom title and logo.
- **GitHub and LinkedIn Links:** Links to the developer's profiles are provided in the sidebar.

## Getting Started

### Prerequisites

- Python 3.7+
- Streamlit
- `langchain`
- `langchain-google-genai`
- `google-generativeai`
- `python-dotenv` (for local development)

### Installation

1.  Clone the repository:

    ```bash
    git clone <YOUR_REPOSITORY_URL>
    cd your_app
    ```

2.  Create a virtual environment (recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On macOS/Linux
    venv\Scripts\activate  # On Windows
    ```

3.  Install the required packages:

    ```bash
    pip install streamlit langchain-google-genai google-generativeai python-dotenv
    ```

4.  **Local Development:**

    - Create a `.env` file in the root directory of your project and add your Google Generative AI API key:

      ```
      GOOGLE_API_KEY=YOUR_API_KEY
      ```

5.  **Streamlit Cloud (Recommended):**

    - Add your Google Generative AI API key as a secret named `GOOGLE_API_KEY` in your Streamlit Cloud app settings.

6.  Run the Streamlit application:

    ```bash
    streamlit run app.py
    ```

7.  Open your browser to view the application at `http://localhost:8501`.

### Folder Structure

```
Data_Science_Tutor/
├── app.py
├── utils/
│   ├── init.py
│   ├── session_manager.py
│   ├── llm_utils.py
│   └── data_classes.py
├── components/
│   ├── init.py
│   ├── sidebar.py
│   └── chat_interface.py
└── static/
└── .streamlit/
└── MIT License
└── .env (for local development)
└── README.md
```

### Deployment

To deploy this application to Streamlit Cloud:

1.  Create a GitHub repository for your project.
2.  Push your code to the repository.
3.  Go to [Streamlit Cloud](https://streamlit.io/cloud).
4.  Click "New app".
5.  Select your GitHub repository, branch, and `app.py` file.
6.  Add your Google Generative AI API key as a secret.
7.  Click "Deploy".

### Customization

- **`static/style.css`:** Modify this file to customize the application's appearance.
- **`components/sidebar.py`:** Add or modify sidebar elements.
- **`utils/llm_utils.py`:** Adjust the LLM prompt or model settings.
- **`static/logo.png`:** Replace with your own logo.
- Replace `YOUR_GITHUB_PROFILE_URL` and `YOUR_LINKEDIN_PROFILE_URL` in `components/sidebar.py` with your own profile URLs.

### Author

- Pandey Abhishek Nath Roy
- [GitHub](https://github.com/vjabhi000985/)
- [LinkedIn](https://www.linkedin.com/in/pandey-abhishek-nath-roy/)

### License

This project is licensed under the [MIT License](LICENSE).
