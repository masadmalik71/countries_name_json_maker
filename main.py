import pandas
import json

# deals with input file which have countries and languages
re_countries_dataframe = pandas.read_csv("required Countries.txt")
df_re_countries_dataframe = pandas.DataFrame(re_countries_dataframe)
countries_and_languages = df_re_countries_dataframe.columns.tolist()
countries_and_languages_r = []
languages_r = []
countries_r = []
country_lang_code = countries_and_languages[0]
country_lang_code_li = []

for i in range(0, len(countries_and_languages) - 1):
    country_and_language = countries_and_languages[i]
    if i % 2 != 0:
        country_and_language = country_and_language.split(" / ")
        country = country_and_language[0]
        language = country_and_language[1].replace("]", '')
        language = language.split(" - ")
        language = language[0]
        countries_r.append(country)
        languages_r.append(language)

# deals with input file which have countries code json
countries_code_dataframe = pandas.read_csv("Country Codes.txt")
df_re_countries_code_dataframe = pandas.DataFrame(countries_code_dataframe)
countries_code_list = df_re_countries_code_dataframe.country_code.tolist()
countries_name_list = df_re_countries_code_dataframe.countries.tolist()
countries_code_list_r = []
for country_code in countries_code_list:
    country_code = country_code[:4]
    countries_code_list_r.append(country_code)

# deals with input file which have languages json
languages_code_dataframe = pandas.read_json("LanguageCode.json")
df_re_languages_dataframe = pandas.DataFrame(languages_code_dataframe)

# makes list of language name, code, Id
languages_names = df_re_languages_dataframe.LanguageName.tolist()
languages_codes = df_re_languages_dataframe.LanguageCode.tolist()
CriterionId_list = df_re_languages_dataframe.CriterionId.tolist()

# Main loop
countries_json_li = []
for i in range(len(countries_r) - 1):
    if countries_r[i] in countries_name_list and languages_r[i] in languages_names:
        country_index = countries_name_list.index(countries_r[i])
        language_index = languages_names.index(languages_r[i])
        countries_json_dic = {
            "CountryID": countries_code_list_r[country_index],
            "Name": countries_name_list[country_index],
            "Language": languages_names[language_index],
            "LanguageID": f"{CriterionId_list[language_index]}",
            "CountryLanguage": f"{countries_name_list[country_index]}/{languages_names[language_index]}",
            "CCLC": f"{countries_code_list_r[country_index]}/{CriterionId_list[language_index]}",
            "Image": f"/Images/Flags/{countries_name_list[country_index]}.png",
            "Hl": languages_codes[language_index]
        }
        countries_json_li.append(countries_json_dic)

# Saves the json file into system
with open('data.json', 'w') as f:
    json.dump(countries_json_li, f)
