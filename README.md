# Talk To Database App
This project, Talk To Database App, enables users to interact with a database using natural language queries. It converts user input into SQL statements using LLMs, executes them, and retrieves relevant insights, simplifying database access for non-technical users.

## Demo
![Demo of Talk-to-DB](assests/demo.gif)

## Features

- **Natural Language Querying:** Enables users to query databases using plain English, eliminating the need to write complex SQL queries.
- **Instant Insights Retrieval:** Executes queries dynamically and fetches accurate results, providing actionable insights in real-time.
- **User-Friendly Interface:** Provides an intuitive interface for seamless database interaction, making it accessible for both technical and non-technical users.


## Table of Contents

- [Installation](#installation)
- [File Description](#file_description)
- [Usage](#usage)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Installation

Follow these steps to set up the project locally:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
**1. Clone the repository:**
```bash
    git clone https://github.com/saahilshroff/text-to-SQL.git
    cd text-to-SQL
```

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
**2. Create a virtual environment (optional but recommended):**
```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
**3. Install the required dependencies:**
```bash
    pip install streamlit langchain langchain-community langchain-experimental openai chromadb pymysql sqlalchemy
```

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;

**4. Create OpenAI Key:**

>Go to this link https://openai.com/index/openai-api/

To access the Embeddings and GPT model in the app, you'll need to add some OpenAI credits. For personal use, it doesn't require much—you can start with as little as $5-$10, which should be enough to last 2-3 months depending on your usage.

Sign up and create your **OpenAI API Key**. Copy the api key and store it securely.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
**5. Setup environment variables:**

Open the 'secret_key.py' file. Replace the `'sk-<YOUR_OPEN_API_KEY>'` text and store your OPENAI_API_KEY.
    
secret_key.py
```bash
    OPENAI_API_KEY="<YOUR_OPENAI_API_KEY>"
```

## file_description
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;

**1. app.py** The app.py file serves as the Streamlit application file for the Talk to Database App. One would run this to connect and talk to their database.

**2. experiment.ipynb** The experiment.ipynb file serves as a testing ground to explore the underlying LLM's capabilities. Used Few-Shot Prompting, a technique that provides in-context examples within the prompt to guide the model's responses and enhance performance. However, few-shot prompting does not help whatsoever, and would require model fine-tuning.


## Usage
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
**1. Launch the application:**
```bash
    streamlit run app.py
```  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
**2. Connect to the database:** Input the required database credentials (Host, Database Name, Username, and Password) in the sidebar and click Connect to establish a secure connection.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
**3. Ask questions:** Once connected, enter your natural language questions about the database into the input field and click Submit. 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
**4. View Results:** The query results are displayed in an easy-to-read format under the "Answer" section for quick insights.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
**5. Repeat:** Continue asking questions to interact with the database seamlessly without the need to write SQL queries.


## License
This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.

## Acknowledgments
- [Langchain](https://www.langchain.com/) for the framework to manage the AI pipeline.
- [OpenAI](https://openai.com/) GPT for providing the language model.
- Special thanks to all contributors and users for their support and feedback.
