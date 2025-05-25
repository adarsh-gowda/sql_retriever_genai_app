# sql_retriever_genai_app

# How to run this app
## In gitbash Run the following commands

```bash
git clone https://github.com/adarsh-gowda/sql_retriever_genai_app.git
cd sql_retriever_genai_app
```
```bash
conda create -p venv python = 3.12 -y

conda activate venv/
```

create a dot env file and add bellow 
```bash
GOOGLE_API_KEY=your_google_api_key_here
```

```bash
pip install -r requirements.txt
```

```bash
python sqlLite.py
```

```bash
streamlit run sql.py
```
