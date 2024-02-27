
class Prompts: 

    topics = ['1 Pricing and Fairness', '2 Driver professionalism', '3 Driver behaviour', '4 Customer Service', '5 Application', '6 Lost things', '7 Vehicle Condition', '8 Safety & reliability', '9 Generally bad']

    prompt_sentiment = """
    Define the sentiment of the following taxi service review, \
    which is delimited with triple backticks.
    Give your answer in such format: "Sentiment: positive" or "Sentiment: negative"

    Review text: ```{review}```
    """

    prompt_summary = """
    Your task is to extract relevant information from a taxi service review \
    to give summary to the Marketing department highlighting the benefits of the service. 
    Limit your summary to 20 words.

    Review text: ```{review}```
    """

    prompt_topic = """
    Define which of the  '''{topics}''' are mentioned in the review.
    Here is the description for each topic:
    1 Pricing and Fairness: fare structure, pricing transparency, fairness in charging, affordability, hidden costs, overcharged, wrongly charged, payment methods, cost and refund issues;
    2 Driver professionalism: driver's performance and professionalism, punctuality, navigation skills, driver's cancellations, late pick-up & drop-off at the wrong place, address-related problems, driver didn't deliver to the door;
    3 Driver behaviour: russian language/music, communication, and friendliness, racist/aggressive behavious, demanding something, driver cheated / stole something;
    4 Customer Service: taxi company, it's responsiveness to queries or complaints, helpfulness of customer support;
    5 Application: ease and efficiency of the booking process, user-friendliness of the booking platform or app, app problems;
    6 Lost things: effectiveness in returning the things left in the vehicle,
    not delivered order;
    7 Vehicle Condition: cleanliness, maintenance, smell, smoke-free environment, safety & reliability, place for luggage, comfort, cold;
    8 Safety & reliability: violation of traffic rules, talking on phone, safety belt, reckless/fast driving, road accident, drink driving
    9 Generally bad: bad experience - nothing from the above mentioned,
    Give your answer in a dictionary format: "Topic" : " ... "
    State all the topics mentioned in the review. If so, write  "Topics" as the key, and all the topics list as the values.

    Review text: ```{review}```
    """
  