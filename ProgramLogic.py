"""
Study Abroad Country Selector
Program which allows criteria to be selected in order to determine a country to study abroad in with display on a map

Nicholas Michaud, Cailey Sapienza, Charlie Coxon

April 27, 2022
"""
import geopandas
import matplotlib.pyplot as plt
from restcountries import RestCountryApiV2 as rapi
import streamlit as st

#Main Streamlit Title
st.markdown(f"<h2 style='text-align: center; color: black;'>Welcome to study abroad location finder! </h2>",
            unsafe_allow_html=True)

#World country data and map coordinates
global world
world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))

#Main list used to delete non-criteria countries
global c_list
c_list = []

#List of Geopandas countries
geo_world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))
geo_country_list = []
for name in geo_world.name:
    geo_country_list.append(name)
    geo_country_list.sort()

# sidebar
def user_information():
    st.sidebar.header("User Information")
    global country, c_list
    country = st.sidebar.selectbox(label= "What country are you from?", options= geo_country_list)
    c_list.append(country)

#Determine the region person would like to study abroad in
def near_or_far():
    st.sidebar.write("What region would you like?")
    region = st.sidebar.selectbox(label= "Regions", options= ("Africa", "Americas", "Asia", "Antarctic", "Antarctic Ocean", "Europe", "Oceania"), index= 1)
    country_region = rapi.get_countries_by_region(region= region)
    country_region_list = []
    for item in range(len(country_region)):
        x_country = country_region[item]
        country_region_list.append(x_country.name)
    for item in geo_country_list:
        if item not in country_region_list and c_list:
            c_list.append(item)

#Determine the language a person would like to learn while studying abroad
language_list = {"English" : "en", "Mandarin" : "zh", "Hindi" : "hi", "Spanish" : "es", "French" : "fr", "Arabic" : "ar", "Italian" : "it", "Russian" : "ru", "Portuguese" : "pt", "German" : "de"}
def get_language_country():
    st.sidebar.write("What language do you want to learn?")
    l_choice = st.sidebar.selectbox(label="New Language", options=language_list.keys())
    country_language = rapi.get_countries_by_language(language= language_list[l_choice], filters=["name"])
    l_country_list = []
    for item in range(len(country_language)):
        l_country = country_language[item]
        l_country_list.append(l_country.name)
    for item in geo_country_list:
        if item not in l_country_list and c_list:
            c_list.append(item)

#Deletes countries from the map and range of acceptable companies
def delete_countries():
    global world
    for item in c_list:
        country_index = world.index[world.name == item].tolist()
        for number in range(len(country_index)):
            try:
                world = world.drop(country_index[number])
            except:
                st.markdown(f"<h2 style='text-align: center; color: red;'>Invalid Input </h2>",
                            unsafe_allow_html=True)
    fig, ax = plt.subplots(1, 1)
    st.set_option('deprecation.showPyplotGlobalUse', False)
    world_graph = world.plot(color='blue', edgecolor='black')
    world.plot()
    try:
        st.pyplot(fig=None)
        results = []
        for item in geo_country_list:
            if item not in c_list:
                results.append(item)
        result_text = ", ".join(results)
        st.markdown(f"<h2 style='text-align: center; color: black;'>You should study abroad in {result_text}! </h2>",
                    unsafe_allow_html=True)
    except:
        st.markdown(f"<h2 style='text-align: center; color: red;'>Invalid Input </h2>",
                    unsafe_allow_html=True)

#Main function
def main():
    user_information()
    near_or_far()
    get_language_country()
    delete_countries()

if __name__ == "__main__":
    main()
