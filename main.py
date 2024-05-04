from recepies import recipes
import pandas as pd
import streamlit as st
ingridient = input("What ingridient: ")
data={

}
max=0
for i in recipes.keys():
    if ingridient in recipes[i]:
        data[i] = recipes[i]
        if len(recipes[i]) > max:
            max =len(recipes[i])
for recipe_name in data.keys():
    if len(data[recipe_name]) < max:
        while len(data[recipe_name]) < max:
            data[recipe_name].append(" ")

df = pd.DataFrame(data)
pd.set_option('display.max_columns', None)

st.(df)