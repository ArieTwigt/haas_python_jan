import requests
import pandas as pd
import os


def get_cars_by_brand(brand: str, type_output="list", export_csv=False):
    available_types = [str]

    if type(brand) not in available_types:
        raise TypeError(f"Brand should be of type 'str' \n\n Got'{type(brand)}'")

    brand_upper = brand.upper()
    endpoint = f"https://opendata.rdw.nl/resource/m9d7-ebf2.json?merk={brand_upper}"
    
    response = requests.get(endpoint)
    
    car_list = response.json()

    if len(car_list) == 0:
        raise ValueError(f"No cars for brand {brand}\n\nPlease refer to:\n\nhttps://dev.socrata.com/foundry/opendata.rdw.nl/m9d7-ebf2 to show available brands")
    
    cars_df = pd.DataFrame(car_list)

    if export_csv:
        export_cars(cars_df, f"export_{brand}")
    else: 
        if type_output == 'list':
            return car_list
        elif type_output == 'df':
            return cars_df
        elif type_output == "both":
            return car_list, cars_df
        else:
            raise ValueError("Please select 'list, df, or 'both'")
      
        
def export_cars(cars_df, file_name):
    dir_name = file_name
    files_dirs = os.listdir()

    if dir_name not in files_dirs:
        os.mkdir(dir_name)

    cars_df.to_csv(f"{dir_name}/{file_name}.csv", sep=";")
    print(f"Exported to {file_name}")

