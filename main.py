import random
import re
from string import Template


def randomize(match):
    res = match.group(1).split('|')
    random.shuffle(res)
    return res[0]

def random_sentence(tpl):
    return re.sub(r'{(.*?)}', randomize, tpl)

def getting_template():
    print("Welcome to the Smart Text Template Generator (STTG).\nBefore start, see the instruction below:\n\n\t1.If you want to have options for a specific term put it into a curly brace and divide options with pipe. Checkout the below example:\n\t\te.g. {can|could|would}\n\t2.For your important keywords place a $before it (Consider that you can apply the first instruction here as well.) Take a look at below example:\n\t\te.g. if you {$CHANGE} your $FEATURE\n\nLet's start!\n")
    temp = input("Please provide your template based on the provided instructions:\n")
    t = Template(temp)
    return t 

template_dict = {
    "CHANGE":"increase|raise|make an increase to",
    "FEATURE":"loan amount"
}

def inference(template_dict, template):
    x = template.substitute(CHANGE="increase|raise|make an increase to", FEATURE="loan amount", CHANGE2="decrease", FEATURE2="Salary")
    print(random_sentence(x))
    return random_sentence(x)
    
#Your loan application {can|could|would} be successful if you {$CHANGE} your $FEATURE and {$CHANGE2} your $FEATURE2
 
def main():

    template_dict = {
    "CHANGE":"increase|raise|make an increase to",
    "FEATURE":"loan amount",
    "CHANGE2":"decrease", "FEATURE2":"Salary"
    }
    template = getting_template()
    x= inference(template_dict, template)
    print(x)
    # x = t.substitute(CHANGE="inc")
    # x = t.substitute(**template_dict)

if __name__ == "__main__":
    main()