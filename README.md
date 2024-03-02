# Topic_Classification_LLM

### Description
This is the further development of the previous taxi service reviews classification project. 
The aim is to create an efficient system to filter negative reviews, classify them according to the topics, and prioritize for the customer service fast response using LLMs, **gpt** in particular.


### How to use
First of all, you will need to initialize your own .env file, create python virtual environment and install necessary packages:

source venv/bin/activate
pip install -e . --no-deps
pip install -r requirements.txt

To test the classification system on your own examples, remember to add a .env file with your 'OPENAI_API_KEY' or replace 'OPENAI_API_KEY' in `classification.py` with your key.

Then run:
`run streamlit classification.py` to open the app in your browser window and enter your review .

### Project status
The project is completed.