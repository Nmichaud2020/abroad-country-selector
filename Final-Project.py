import geopandas
import matplotlib.pyplot as plt
from restcountries import RestCountryApiV2 as rapi

path_to_data = geopandas.datasets.get_path("nybb")
gdf = geopandas.read_file(path_to_data)

# print(gdf)

def get_language(name):
    country_list = rapi.get_countries_by_name(name, filters = ["languages"])
    country = country_list[0]
    language = (country.languages[0]["name"])
    native_language = (country.languages[0]["nativeName"])
    print(language)
    print(native_language)
get_language("France")

world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))
print(world.name)
with open("Tester.csv", "w") as file:
    for country in world.name:
        file.write(str(country) + "\n")
file.close()
# country_index = world.index[world.name == 'Brazil'].tolist()
#
# print(country_index)
# world = world.drop(country_index[0])
#
#
# # print(world[world.name == "France"])
# world.plot(color='blue', edgecolor='black')
# plt.show()

#Test
c_list = ["Canada", "Antarctica", "Brazil"]
for country in c_list:
    country_index = world.index[world.name == country].tolist()
    world = world.drop(country_index[0])

print(country_index)



# print(world[world.name == "France"])
world.plot(color='blue', edgecolor='black')
plt.show()

# cities = geopandas.read_file(geopandas.datasets.get_path('naturalearth_cities'))
#
# print(world.head()) #data
#
# fig, ax = plt.subplots(1, 1)
#world.plot(column='name'); #plot basic colors
# base = world[world.name == 'Africa'].plot(color='white', edgecolor='black')
# base.plot()
# plt.show()
#
# world['centroid_column'].head()
#
#
# #world.plot(column='pop_est', missing_kwds={'color': 'lightgrey'}); #one can specify the style and label of features containing None or NaN
#
# #world = world[(world.pop_est>0) & (world.name!="Antarctica")]   #gets rid of antarctia
#
# #world['gdp_per_cap'] = world.gdp_md_est / world.pop_est #makes the column to plot countries by
#
# #world.plot(column='gdp_per_cap');    #plots by gdr per capita
#
#
# #creates legend
#
# #fig, ax = plt.subplots(1, 1)
#
# #world.plot(column='pop_est', ax=ax, legend=True)
