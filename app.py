import streamlit as st
from langchain import OpenAI
from langchain.sql_database import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain
from sqlalchemy.exc import SQLAlchemyError
from secret_key import OPENAI_API_KEY

# Initialize LLM with API key
llm = OpenAI(temperature=0.5, max_tokens=100, api_key=OPENAI_API_KEY)

# Streamlit Page Configuration
st.set_page_config(page_title="Talk To Database", page_icon="💬")

# Sidebar for Database Connection
st.sidebar.header("Database Connection")
db_host = st.sidebar.text_input("Host", value="localhost", placeholder="Enter database host")
db_name = st.sidebar.text_input("Database Name", value="pizzastore", placeholder="Enter database name")
db_user = st.sidebar.text_input("Username", placeholder="Enter username")
db_password = st.sidebar.text_input("Password", type="password", placeholder="Enter password")
db_button = st.sidebar.button("Connect", type="primary")

# Function to connect to the database
def connect_to_database(user, password, host, database):
    try:
        db_uri = f"mysql+pymysql://{user}:{password}@{host}/{database}"
        db = SQLDatabase.from_uri(db_uri, sample_rows_in_table_info=5)
        return db, None
    except SQLAlchemyError as e:
        return None, str(e)

# Main Section
st.title("💬 Talk To Database App")
st.write("Ask questions about your data to your database and get answers instantly!")

# Initialize session state for database connection
if "db" not in st.session_state:
    st.session_state.db = None
    st.session_state.error = None

# Connect to the database on button click
if db_button:
    if db_user and db_password and db_host and db_name:
        db, error = connect_to_database(db_user, db_password, db_host, db_name)
        if error:
            st.sidebar.error(f"Error connecting to database: {error}")
        else:
            st.session_state.db = db  # Store DB in session state
            st.sidebar.success("✅ Successfully connected to the database!")
    else:
        st.sidebar.warning("Please fill in all database credentials.")

# Question Answer Section
if st.session_state.db:
    st.success("Database connected. Ask a question below!")

    # Initialize SQLDatabaseChain for LLM
    db_chain = SQLDatabaseChain.from_llm(llm=llm, db=st.session_state.db, verbose=True)

    # User input for questions
    question = st.text_input("Enter your question about the database:", key="inp", autocomplete="False")
    submit_btn = st.button("Submit", type="primary")

    # Process the question
    if submit_btn:
        if question.strip():  # Check if the question is not empty
            with st.spinner("Fetching the answer..."):
                try:
                    # Run the query through the chain
                    answer = db_chain.run(question)
                    st.subheader("**Answer:**")
                    st.info(answer)
                except Exception as e:
                    st.error(f"Error: {str(e)}")
        else:
            st.warning("⚠️ Please enter a question before submitting.")
