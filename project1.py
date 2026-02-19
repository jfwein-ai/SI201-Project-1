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
	# Columns: “year”, “sex” and “flipper_length_mm"
    result = {}
    
    for row in data:
        year = row["year"]
        sex = row["sex"]
        flipper = row["flipper_length_mm"]
        
        # Skip missing values
        if flipper == "" or sex == "" or flipper is None or flipper == "NA" or sex == "NA" :
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

def male_flipper_length_Adelie(data):
    # What is the average flipper length of male Adelie penguins? (Jared)
    # Columns: “species,” “flipper_length_mm,” and “sex”

    total = 0
    count = 0

    for row in data:
        species = row['species']
        flipper = row['flipper_length_mm']
        sex = row['sex']

        if flipper == "NA" or flipper == "" or sex == "NA" or sex == "":
            continue
        
        if species != "Adelie" or sex != "MALE":
            continue
            
        total += float(flipper)
        count += 1

    return total / count

def over_50_bill_biscoe(data):
    # For penguins that live on Biscoe island, how many have a bill length of at least 50 mm for each species? (Jared)
    # Columns: “island,” “bill_length_mm,” and “species”
    result = {}

    for row in data:
        island = row['island']
        bill = row['bill_length_mm']
        species = row['species']

        if bill == "" or bill == "NA":
            continue
        
        if island != "Biscoe":
            continue

        bill = float(bill)

        if bill < 50:
            continue


        if species not in result:
            result[species] = 0

        result[species] += 1

    return result
def count_species_sex_by_island(data):
    result = {}

    for row in data:
        species = row["species"]
        island = row["island"]
        sex = row["sex"]

        if "" in (species, island, sex) or "NA" in (species, island, sex):
            continue

        if species not in result:
            result[species] = {}
        
        if island not in result[species]:
            result[species][island] = {}
            
        if sex not in result[species][island]:
            result[species][island][sex] = 0

        result[species][island][sex] += 1

    return result
def most_common_flipper_and_bill_by_island(data):
    # For each Island, what is the most common flipper length and bill length (Elliot)
    # Columns: “island,” “flipper_length_mm”, “bill_length_mm”
    freqs = {}

    for row in data:
        island = row["island"]
        flipper = row["flipper_length_mm"]
        bill = row["bill_length_mm"]

        if "" in (island, flipper, bill) or "NA" in (island, flipper, bill):
            continue

        flipper = float(flipper)
        bill = float(bill)

        if island not in freqs:
            freqs[island] = {'flipper': {}, 'bill': {}}

        if flipper not in freqs[island]['flipper']:
            freqs[island]['flipper'][flipper] = 0
        freqs[island]['flipper'][flipper] += 1

        if bill not in freqs[island]['bill']:
            freqs[island]['bill'][bill] = 0
        freqs[island]['bill'][bill] += 1

    result = {}
    for island, counts in freqs.items():
        
        most_common_flipper = None
        max_flipper_count = 0
        for val, count in counts['flipper'].items():
            if count > max_flipper_count:
                most_common_flipper = val
                max_flipper_count = count

        most_common_bill = None
        max_bill_count = 0
        for val, count in counts['bill'].items():
            if count > max_bill_count:
                most_common_bill = val
                max_bill_count = count

        result[island] = {
            "most_common_flipper_length": most_common_flipper,
            "most_common_bill_length": most_common_bill
        }

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

class TestAvgFlipperLengthByYearSex(unittest.TestCase):

    def test_general_case(self):
        """General case: correct average flipper length computed for a known year/sex."""
        data = load_test_data("avg_flipper_length_by_year_sex.csv")
        result = avg_flipper_length_by_year_sex(data)
        # 2007/MALE: (181 + 178) / 2 = 179.5
        self.assertAlmostEqual(result["2007"]["MALE"], 179.5)

    def test_edge_case_missing_values(self):
        """Edge case: rows with NA or empty sex/flipper are skipped and don't affect the average."""
        data = load_test_data("avg_flipper_length_by_year_sex.csv")
        result = avg_flipper_length_by_year_sex(data)
        # 2009/FEMALE: (216 + 222) / 2 = 219.0 (NA row and empty string row excluded)
        self.assertAlmostEqual(result["2009"]["FEMALE"], 219.0)

class TestAvgMaleFlipperlengthOnAdelie(unittest.TestCase):

    def test_general_case(self):
        # General case: correct average flipper length for male Adelie penguins.
        data = load_test_data("avg_flipper_length_male_adelie.csv")
        result = male_flipper_length_Adelie(data)
        # Male Adelie rows: (181 + 179 + 185 + 183) / 4 = 182.0
        self.assertAlmostEqual(result, 182.0)

    def test_edge_case_missing_values(self):
        # Edge case: NA and empty string rows are excluded from the average.
        data = load_test_data("avg_flipper_length_male_adelie.csv")
        result = male_flipper_length_Adelie(data)
        # NA flipper row and empty sex row are excluded — result is still 182.0, not skewed
        self.assertAlmostEqual(result, 182.0)

class TestNumBiscoeBillLengthAtLeastFifty(unittest.TestCase):

    def test_general_case(self):
        #General case: correct count of bill >= 50mm Biscoe penguins per species.
        data = load_test_data("count_long_bill_biscoe_by_species.csv")
        result = over_50_bill_biscoe(data)
        # Gentoo/Biscoe with bill >= 50: rows 1 (51.3) and 2 (50.0) = 2
        self.assertEqual(result["Gentoo"], 2)
        # Adelie/Biscoe with bill >= 50: rows 5 (50.6) and 10 (50.1) = 2
        self.assertEqual(result["Adelie"], 2)

    def test_edge_case_missing_values(self):
        # Edge case: NA bills, empty bills, and non-Biscoe rows are excluded.
        data = load_test_data("count_long_bill_biscoe_by_species.csv")
        result = over_50_bill_biscoe(data)
        # Chinstrap only appears on Dream island, so it should not exist in result
        self.assertNotIn("Chinstrap", result)

if __name__ == "__main__":
    unittest.main()

