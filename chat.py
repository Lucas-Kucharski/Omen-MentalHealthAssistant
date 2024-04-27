import random
import json

import torch

from model import NeuralNet
from nltk_utils import bag_of_words, tokenize

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open('intents.json', 'r') as json_data:
    intents = json.load(json_data)

FILE = "data.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

bot_name = "Omen"

responses = [
    "How does that make you feel?",
    "Can you tell me more about that?",
    "What do you think is the root of the issue?",
    "Have you discussed this with anyone else?",
    "It sounds like you're experiencing a lot.",
    "Do you think this has affected other areas of your life?",
    "Have you considered seeking professional help?",
    "Let's delve deeper into that.",
    "How do you cope with these feelings?",
    "What do you hope to achieve by discussing this?"
]

info_responses = {
    "depression": ["Depression is a mental health condition that affects millions every year.\n During a depressive episode, the person experiences depressed mood (feeling sad,\n irritable, empty) or a loss of pleasure or interest in activities, for most of the day, nearly every day, for at least two weeks.\n Several other symptoms are also present, which may include poor concentration, feelings of \nexcessive guilt or low self-worth, hopelessness about the future, thoughts about dying or \nsuicide disrupted sleep, changes in appetite or weight, and feeling especially \ntired or low in energy.\n People with depression are at an increased risk of suicide. And if you or a loved one are \nthought to have depression you should seek medical attention.\n If you are feeling distressed and need to talk to a counselor, call 1-800-273-TALK (8255).\n" ],
    "anxiety": ["Anxiety disorders are characterised by excessive fear and worry and related \nbehavioural disturbances.\n Symptoms are severe enough to result in significant distress or significant\n impairment in functioning.\n There are several different kinds of anxiety disorders, such as: \ngeneralised anxiety disorder (characterised by excessive worry), \npanic disorder (characterised by panic attacks), \nsocial anxiety disorder (characterised by excessive fear and worry in social situations), \nseparation anxiety disorder (characterised by excessive fear or anxiety about separation from \nthose individuals to whom the person has a deep emotional bond), and others.\n Effective psychological treatment exists, and depending on the age and severity, medication may also be considered.\n If you are feeling distressed and need to talk to a counselor, call 1-800-273-TALK (8255).\n"],
    "bipolar": ["People with bipolar disorder experience alternating depressive episodes with periods of manic symptoms.\n During a depressive episode, the person experiences depressed mood (feeling sad, \nirritable, empty) or a loss of pleasure or interest in activities, for most of the day,\n nearly every day.\n Manic symptoms may include euphoria or irritability, increased activity or energy, and other \nsymptoms such as increased talkativeness, racing thoughts, increased self-esteem, \ndecreased need for sleep, distractibility, and impulsive reckless behaviour.\n People with bipolar disorder are at an increased risk of suicide. And if you or a loved one are \nthought to have depression you should seek medical attention.\n If you are feeling distressed and need to talk to a counselor, call 1-800-273-TALK (8255).\n"],
    "ptsd": ["PTSD may develop following exposure to an extremely threatening or horrific event or series of events.\n It is characterised by all of the following: \n1) re-experiencing the traumatic event or events in the present (intrusive memories, \nflashbacks, or nightmares); \n2) avoidance of thoughts and memories of the event(s), or avoidance of activities, situations,\n or people reminiscent of the event(s); \n3) persistent perceptions of heightened current threat.\n These symptoms persist for at least several weeks and cause significant impairment\n in functioning. Effective psychological treatment exists.\n If you are feeling distressed and need to talk to a counselor, call 1-800-273-TALK (8255).\n"],
    "eating disorder": ["Eating disorders, such as anorexia nervosa and bulimia nervosa, involve abnormal \neating and preoccupation with food as well as prominent body weight and shape concerns. \nThe symptoms or behaviours result in significant risk or damage to health, significant distress, or significant impairment of functioning.\n Anorexia nervosa often has its onset during adolescence or early adulthood and is \nassociated with premature death due to medical complications or suicide. \nIndividuals with bulimia nervosa are at a significantly increased risk for substance use,\n suicidality, and health complications.\n If you are feeling distressed and need to talk to a counselor, call 1-800-273-TALK (8255).\n"]
}

def get_response(msg):
    sentence = tokenize(msg)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)
    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]
    if prob.item() > 0.75:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                return random.choice(intent['responses'])
    
    return "I do not understand..."

def therapist(msg):
    def therapist_response(msg):
        return random.choice(responses)
    
    while True:
            response = therapist_response(msg)
            return response


# Function to generate a response to user input
def generate_response(msg):
    # Check if input matches any predefined responses
    for key in info_responses:
        if msg in key:
            return random.choice(info_responses[key])
    # If no predefined response matches, return a default response
    return "I'm sorry, I didn't understand that."           