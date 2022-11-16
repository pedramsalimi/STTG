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
    x = template.substitute(template_dict)
    print(random_sentence(x))
    return random_sentence(x)
    
def main(): 

# Loan application example:
    
    #Your loan application {can|could|would} be successful if you {$CHANGE} your $FEATURE and {$CHANGE2} your $FEATURE2

    # template_dict = {
    # "CHANGE":"increase|raise|make an increase to",
    # "FEATURE":"loan amount",
    # "CHANGE2":"decrease", "FEATURE2":"Salary"
    # }

# Weather forcasting example:

    # The temperature for $day, {$date} in $year is predicted to be $temperature

    template_dict = {
    "day":"Saturday",
    "date":"16 Nov|16th of November",
    "year":"2022", "temperature":"22.4 degree"
    }

    template = getting_template()
    x= inference(template_dict, template)
    print(x)


if __name__ == "__main__":
    main()