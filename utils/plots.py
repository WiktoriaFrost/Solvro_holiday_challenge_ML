import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def total_category_drinks(df):
    category_counts = df['category'].value_counts()

    category_df = category_counts.reset_index()
    category_df.columns = ['Category', 'Count']

    plt.figure(figsize=(12, 8))
    ax = sns.barplot(data=category_df, x='Category', y='Count', hue='Category', palette='viridis', legend=False)
    for container in ax.containers:
        ax.bar_label(container)
    plt.title('Number of drinks in the category')
    plt.xlabel('Number of drinks')
    plt.ylabel('Category')
    plt.show()


def tags_in_categories_plot(category_tags_df):
    for category in ('Cocktail', 'Ordinary Drink', 'Punch / Party Drink'):
        top_tags_df = category_tags_df[['Tag', category]].dropna().sort_values(by=category, ascending=False).head(3)
        plt.figure(figsize=(12, 8))
        ax = sns.barplot(data=top_tags_df, x='Tag', y=category, hue='Tag', palette='viridis', legend=False)
        for container in ax.containers:
            ax.bar_label(container)
        plt.title(f'The most fequently used tags in drinks: {category}')
        plt.xlabel('Tag')
        plt.ylabel('Number of drinks')
        plt.show()


def the_most_commonly_ingredients(top_ingredients_df):
    plt.figure(figsize=(12, 8))
    ax = sns.barplot(data=top_ingredients_df, x='Ingredient', y='Count', hue='Ingredient', palette='viridis',
                     legend=False)
    for container in ax.containers:
        ax.bar_label(container)

    plt.title('The 10 most commonly used ingredients')
    plt.xlabel('Ingredients')
    plt.ylabel('Number of drinks')
    plt.show()


def types_of_glass(glass_df):
    plt.figure(figsize=(12, 8))
    ax = sns.barplot(data=glass_df, x='Glass', y='Count', hue='Glass', palette='viridis', legend=False)
    for container in ax.containers:
        ax.bar_label(container)
    plt.title('Number of drinks by glass type')
    plt.xlabel('Type of glass')
    plt.ylabel('Number of drinks')
    plt.xticks(rotation=90)
    plt.show()