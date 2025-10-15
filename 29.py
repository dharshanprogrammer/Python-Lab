import pandas as pd

data = {
    'Taluk': ['Coimbatore North', 'Coimbatore North', 'Coimbatore South', 'Coimbatore South', 'Coimbatore Central'],
    'Area': ['Gandhipuram', 'RS Puram', 'Podanur', 'Singanallur', 'Town Hall'],
    'Street': ['Sathy Road Main', 'DB Road', 'Podanur Main St', 'Trichy Road', 'Big Bazaar Street'],
    'Wet_Waste_Tons': [5.5, 3.2, 7.8, 6.1, 4.9],
    'Dry_Waste_Tons': [3.5, 1.8, 2.2, 2.9, 1.1]
}

df = pd.DataFrame(data)

df['Total_Waste_Tons'] = df['Wet_Waste_Tons'] + df['Dry_Waste_Tons']

street_max_collection = df.loc[df['Total_Waste_Tons'].idxmax()]
street_min_collection = df.loc[df['Total_Waste_Tons'].idxmin()]

area_summary = df.groupby('Area')['Total_Waste_Tons'].sum().reset_index()
area_max_collection = area_summary.loc[area_summary['Total_Waste_Tons'].idxmax()]
area_min_collection = area_summary.loc[area_summary['Total_Waste_Tons'].idxmin()]

taluk_summary = df.groupby('Taluk')['Total_Waste_Tons'].sum().reset_index()
taluk_max_collection = taluk_summary.loc[taluk_summary['Total_Waste_Tons'].idxmax()]
taluk_min_collection = taluk_summary.loc[taluk_summary['Total_Waste_Tons'].idxmin()]

print('Coimbatore City Corporation Garbage Collection Report')
print('-' * 60)
print('Simulated Daily Collection Data')
print(df)
print('-' * 60)
print('Maximum and Minimum Collection Analysis')
print('\nStreet-wise Collection:')
print(f'Maximum Collection: {street_max_collection["Total_Waste_Tons"]:.2f} Tons in {street_max_collection["Street"]} ({street_max_collection["Area"]}, {street_max_collection["Taluk"]})')
print(f'Minimum Collection: {street_min_collection["Total_Waste_Tons"]:.2f} Tons in {street_min_collection["Street"]} ({street_min_collection["Area"]}, {street_min_collection["Taluk"]})')
print('\nArea-wise Collection:')
print(f'Maximum Collection: {area_max_collection["Total_Waste_Tons"]:.2f} Tons in {area_max_collection["Area"]}')
print(f'Minimum Collection: {area_min_collection["Total_Waste_Tons"]:.2f} Tons in {area_min_collection["Area"]}')
print('\nTaluk-wise Collection:')
print(f'Maximum Collection: {taluk_max_collection["Total_Waste_Tons"]:.2f} Tons in {taluk_max_collection["Taluk"]}')
print(f'Minimum Collection: {taluk_min_collection["Total_Waste_Tons"]:.2f} Tons in {taluk_min_collection["Taluk"]}')
print('-' * 60)