# Name:
# Student ID:
# Email:
# Who or what you worked with on this homework (including generative AI like ChatGPT):
# If you worked with generative AI also add a statement for how you used it.
# e.g.: Used ChatGPT to learn how to import a CSV file into my code and to gaurantee Python always looks for the csv file in the same folder as my script. 
# Asked ChatGPT hints for debugging and suggesting the general structure of the code
# Did your use of GenAI on this assignment align with your goals and guidelines in 
#    your Gen AI contract? If not, why?

import csv
import os

current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, "data.csv")

with open("penguins.csv", "r") as file:
    reader = csv.DictReader(file)