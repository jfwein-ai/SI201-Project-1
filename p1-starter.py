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
file_path = os.path.join(current_dir, "penguins.csv")

with open(file_path, "r") as data:
    reader = csv.DictReader(data)
    rows = list(reader)



for row in rows:
    species = row['species']
    print(species)

def avg_body_mass_by_species_island(data):
    # For each species, what is the average body mass on each island? (Noam)
	# Columns: “species”, “Island”, and “body_mass_g”

    result = {}

    for row in data:
        species = row["species"]
        island = row["island"]
        mass = row["body_mass_g"]

        if mass == "" or mass == "NA":
            continue

        mass = float(mass)

        if species not in result:
            result[species] = {}
            
        if island not in result[species]:
            result[species][island] = {"total": 0, "count": 0}

        result[species][island]["total"] += mass
        result[species][island]["count"] += 1

    for species in result:
        for island in result[species]:
            total = result[species][island]["total"]
            count = result[species][island]["count"]
            result[species][island] = total / count

    return result

result = avg_body_mass_by_species_island(rows)
print(result)

