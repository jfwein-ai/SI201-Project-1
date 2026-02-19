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

def avg_flipper_length_by_year_sex(data):
    # For each year, what is the average flipper length of male and female penguins? (Noam)
	# Columns: “year”, “sex” and “flipper_length_mm”
    result = {}
    
    for row in data:
        year = row["year"]
        sex = row["sex"]
        flipper = row["flipper_length_mm"]
        
        # Skip missing values
        if flipper == "" or sex == "" or flipper is None:
            continue
        
        flipper = float(flipper)
        
        if year not in result:
            result[year] = {}
        
        if sex not in result[year]:
            result[year][sex] = {"total": 0, "count": 0}
        
        result[year][sex]["total"] += flipper
        result[year][sex]["count"] += 1
    
    # Convert totals to averages
    for year in result:
        for sex in result[year]:
            total = result[year][sex]["total"]
            count = result[year][sex]["count"]
            result[year][sex] = total / count
    
    return result


import unittest

def load_test_data(filename):
    with open(filename, "r") as f:
        reader = csv.DictReader(f)
        return list(reader)

class TestAvgBodyMassBySpeciesIsland(unittest.TestCase):

    def test_general_case(self):
        """General case: correct average computed for a known species/island."""
        data = load_test_data("avg_body_mass_by_species_island.csv")
        result = avg_body_mass_by_species_island(data)
        # Chinstrap/Dream: (3700 + 3600 + 3650) / 3 = 3650.0
        self.assertAlmostEqual(result["Chinstrap"]["Dream"], 3650.0)

    def test_edge_case_missing_values(self):
        """Edge case: NA rows are skipped and don't affect the average."""
        data = load_test_data("avg_body_mass_by_species_island.csv")
        result = avg_body_mass_by_species_island(data)
        # Gentoo/Biscoe: (5000 + 4800 + 5200) / 3 = 5000.0 (NA row excluded)
        self.assertAlmostEqual(result["Gentoo"]["Biscoe"], 5000.0)

    def test_avg_flipper_length_general():
        data = load_test_data("avg_body_mass_by_species_island.csv")
        result = avg_flipper_length_by_year_sex(data)
        
        assert round(result["2007"]["Male"], 1) == 181.0
        assert round(result["2009"]["Female"], 1) == 215.0


    def test_avg_flipper_length_edge():
        data = load_test_data("avg_body_mass_by_species_island.csv")
        result = avg_flipper_length_by_year_sex(data)
    
    # Rows with missing sex or flipper length are ignored
    assert "2007" in result

if __name__ == "__main__":
    unittest.main()

