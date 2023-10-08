import pandas as pd
import csv

df = pd.read_csv('diningScraper.csv')

df["hasPeanut"] = False
df["hasGluten"] = False
df["notVegan"] = False
df["notVeg"] = False
df["hasSesame"] = False
df["hasDairy"] = False
df["hasSoy"] = False
df["hasEgg"] = False
df["hasFish"] = False
df["withAlcohol"] = False
df['ingredients'] = df['ingredients'].str.lower()

for ind in df.index:    
    if (str(df.loc[ind, 'ingredients']).find("peanut") > -1):
        df.loc[ind, 'hasPeanut'] = True
    if (str(df.loc[ind, 'ingredients']).find("gluten") > -1):
        df.loc[ind, 'hasGluten'] = True
    if (str(df.loc[ind, 'ingredients']).find("bread") > -1):
        df.loc[ind, 'hasGluten'] = True
    if (str(df.loc[ind, 'ingredients']).find("flour") > -1):
        df.loc[ind, 'hasGluten'] = True
    if (str(df.loc[ind, 'ingredients']).find("bagel") > -1):
        df.loc[ind, 'hasGluten'] = True
    if (str(df.loc[ind, 'ingredients']).find("barley") > -1):
        df.loc[ind, 'hasGluten'] = True
    if (str(df.loc[ind, 'ingredients']).find("whey") > -1):
        df.loc[ind, 'hasGluten'] = True
    if (str(df.loc[ind, 'ingredients']).find("yeast") > -1):
        df.loc[ind, 'hasPeanut'] = True
    if (str(df.loc[ind, 'ingredients']).find("wheat") > -1):
        df.loc[ind, 'hasPeanut'] = True
    if (str(df.loc[ind, 'ingredients']).find("sodium stearoyl lactylate") > -1):
        df.loc[ind, 'notVegan'] = True
    if (str(df.loc[ind, 'ingredients']).find("d3") > -1):
        df.loc[ind, 'notVegan'] = True
    if (str(df.loc[ind, 'ingredients']).find("b12") > -1):
        df.loc[ind, 'notVegan'] = True
    if (str(df.loc[ind, 'ingredients']).find("bacon") > -1):
        df.loc[ind, 'notVegan'] = True
        df.loc[ind, 'notVeg'] = True
    if (str(df.loc[ind, 'ingredients']).find("beef") > -1):
        df.loc[ind, 'notVegan'] = True
        df.loc[ind, 'notVeg'] = True
    if (str(df.loc[ind, 'ingredients']).find("ham") > -1):
        df.loc[ind, 'notVegan'] = True
        df.loc[ind, 'notVeg'] = True
    if (str(df.loc[ind, 'ingredients']).find("turkey") > -1):
        df.loc[ind, 'notVegan'] = True
        df.loc[ind, 'notVeg'] = True
    if (str(df.loc[ind, 'ingredients']).find("meat") > -1):
        df.loc[ind, 'notVegan'] = True
        df.loc[ind, 'notVeg'] = True
    if (str(df.loc[ind, 'ingredients']).find("pork") > -1):
        df.loc[ind, 'notVegan'] = True
        df.loc[ind, 'notVeg'] = True
    if (str(df.loc[ind, 'ingredients']).find("duck") > -1):
        df.loc[ind, 'notVegan'] = True
        df.loc[ind, 'notVeg'] = True
    if (str(df.loc[ind, 'ingredients']).find("sesame") > -1):
        df.loc[ind, 'hasSesame'] = True
    if (str(df.loc[ind, 'ingredients']).find("cheese") > -1):
        df.loc[ind, 'hasDairy'] = True
    if (str(df.loc[ind, 'ingredients']).find("milk") > -1):
        df.loc[ind, 'hasDairy'] = True
    if (str(df.loc[ind, 'ingredients']).find("butter") > -1):
        df.loc[ind, 'hasDairy'] = True
    if (str(df.loc[ind, 'ingredients']).find("cream") > -1):
        df.loc[ind, 'hasDairy'] = True
    if (str(df.loc[ind, 'ingredients']).find("pasteurized") > -1):
        df.loc[ind, 'hasDairy'] = True
    if (str(df.loc[ind, 'ingredients']).find("yogurt") > -1):
        df.loc[ind, 'hasDairy'] = True
    if (str(df.loc[ind, 'ingredients']).find("egg") > -1):
        df.loc[ind, 'hasEgg'] = True
    if (str(df.loc[ind, 'ingredients']).find("tuna") > -1):
        df.loc[ind, 'hasFish'] = True
    if (str(df.loc[ind, 'ingredients']).find("salmon") > -1):
        df.loc[ind, 'hasFish'] = True
    if (str(df.loc[ind, 'ingredients']).find("tilapia") > -1):
        df.loc[ind, 'hasFish'] = True
    if (str(df.loc[ind, 'ingredients']).find("fish") > -1):
        df.loc[ind, 'hasFish'] = True
    if (str(df.loc[ind, 'ingredients']).find("shrimp") > -1):
        df.loc[ind, 'hasFish'] = True
    if (str(df.loc[ind, 'ingredients']).find("alcohol") > -1):
        df.loc[ind, 'withAlcohol'] = True
    if (str(df.loc[ind, 'ingredients']).find("wine") > -1):
        df.loc[ind, 'withAlcohol'] = True
    if (str(df.loc[ind, 'ingredients']).find("vodka") > -1):
        df.loc[ind, 'withAlcohol'] = True
    
df.to_csv('diningInfo.csv')
