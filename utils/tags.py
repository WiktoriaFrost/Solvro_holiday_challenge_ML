from collections import defaultdict
import pandas as pd
from collections import defaultdict


def count_tags(df):
    """ the function counts the occurrences of each tag
    in the 'tags' column"""
    tag_count = defaultdict(int)

    for tags in df['tags'].dropna():
        if isinstance(tags, list):
            for tag in tags:
                tag_count[tag] += 1

    return tag_count


def tags_in_categories(df):
    """This function counts occurrences of tags within each category
    and return the result as a dataframe"""
    category_tag_count = defaultdict(lambda: defaultdict(int))

    for _, row in df[['category', 'tags']].dropna().iterrows():
        # only the row variable is used
        category = row['category']
        tags = row['tags']

        if isinstance(tags, list):
            for tag in tags:
                category_tag_count[category][tag] += 1

    category_tag_count_df = pd.DataFrame(category_tag_count).fillna(0)
    # this method replaces any NaN values with 0

    category_tag_count_df = category_tag_count_df.reset_index()
    category_tag_count_df = category_tag_count_df.rename(columns={'index': 'Tag'})

    return category_tag_count_df