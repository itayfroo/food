import streamlit as st
import pandas as pd
from recepies import recipes

def main():
    st.title("Recipe Finder")

    # Create a list of all ingredients
    all_ingredients = set(ingredient for ingredients in recipes.values() for ingredient in ingredients)

    # Multiselect widget for selecting ingredients
    selected_ingredients = st.multiselect("Select ingredients:", list(all_ingredients))

    # Filter recipes based on selected ingredients
    data = []
    for recipe_name, ingredients in recipes.items():
        if all(ingredient in ingredients for ingredient in selected_ingredients):
            data.append([recipe_name] + ingredients)

    if data:
        # Determine the number of columns dynamically
        num_columns = max(len(recipe) for recipe in data)

        # Create DataFrame
        df = pd.DataFrame(data, columns=["Dish Name"] + [f"Ingredient {i+1}" for i in range(num_columns - 1)])
        st.table(df)
    else:
        st.write("No recipes found containing the selected ingredients.")

if __name__ == "__main__":
    main()
