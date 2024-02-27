import openai
from openai import OpenAI
import os
from dotenv import load_dotenv
import streamlit as st
from langchain.prompts import PromptTemplate
from classification_prompts import Prompts


client = OpenAI(
  api_key=os.environ['OPENAI_API_KEY'], 
)

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0
    )
    return response.choices[0].message.content


def get_classification(review):
    classification_result = []
    
    #getting prompts string from a file
    prompt_template_sent = PromptTemplate.from_template(Prompts.prompt_sentiment)
    prompt_template_sum = PromptTemplate.from_template(Prompts.prompt_summary)
    prompt_template_topic = PromptTemplate.from_template(Prompts.prompt_topic)
    
    #adding variable review to the prompt
    sentiment = prompt_template_sent.format(review=review)
    summary = prompt_template_sum.format(review=review)
    topic = prompt_template_topic.format(review=review, topics=Prompts.topics)
    
    sentiment_result = get_completion(sentiment)
    classification_result.append(sentiment_result)
    if "negative" in sentiment_result.lower():
        topic_result = get_completion(topic)
        identified_topics = [topic for topic in Prompts.topics if topic.lower() in topic_result.lower()]
        classification_result.append(topic_result)
        if "1 Pricing and Fairness" or "3 Driver behaviour" or "6 Lost things" or "8 Safety & reliability" in identified_topics:
            alert = "ALERT: high priority!"
            classification_result.append(alert)
    else:
        summary = get_completion(summary)
        classification_result.append(summary)
    
    # print("Classification Result:", classification_result)
    return classification_result


#Gets the user input
def get_review():
    input_review = st.text_input("You: ", key="input")
    return input_review


#App UI starts here
st.set_page_config(page_title="Reviews Classification", page_icon=":robot:")
st.header("Reviews Classification") 


review = get_review()
response = get_classification(review)

submit = st.button('Classify')

#If generate button is clicked
if submit:

    st.subheader("Answer:")

    st.write(response)