"""
Goal :
- To transform data into desired format that can be used in dashboard
- Append all csv inside same directory
"""

import pandas as pd
import glob
import os

# Defining the home directory on our Device
HOME = os.path.expanduser("~")

# To append all csv, this function is not read in another python file
def __append_all_files(extension, directory):
    # read all object files in the data directory
    all_filenames = [i for i in glob.glob(
        '{directory}/*.{ext}'.format(directory=directory, ext=extension))]

    # append all files into one dataframe
    combined_csv = pd.concat([pd.read_csv(f)
                             for f in all_filenames], ignore_index=True)

    # cleaning the Quantity Ordered column with an invalid value
    combined_csv.drop(
        combined_csv[combined_csv["Quantity Ordered"] == "Quantity Ordered"].index, inplace=True)

    return combined_csv

# data transformation, group by can be filled with product or month
def run_transform(group_by):
    data = __append_all_files(
        'csv', 'data/sales_product_data')

    # group by product and summarize by quantity * price

    data["total_price"] = data["Quantity Ordered"].astype(
        float) * data["Price Each"].astype(float)
    data["Order Date"] = pd.to_datetime(data["Order Date"])

    # drop Date which has a null value
    data.drop(
        data[data["Order Date"].isna()].index, inplace=True)

    if group_by.lower().strip() == 'product':
        # group by product
        data_transformed = data.groupby('Product').agg({"total_price": "sum"}).reset_index()
    elif group_by.lower().strip() == 'month':
        # group by month
        data_transformed = data.groupby(pd.Grouper(key='Order Date', freq='M')).agg({"total_price": "sum"}).reset_index()

    print(data_transformed)

    return data_transformed


if __name__ == '__main__':
    run_transform('product')
