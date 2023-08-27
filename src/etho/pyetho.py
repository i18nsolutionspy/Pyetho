import json	  
import os

module_path = os.path.dirname(__file__)
data = json.load(open(os.path.join(module_path, "data", "etho.json"), "r", encoding="utf-8"))
    #@staticmethod
def country_list():
         """
        Get a list of all country names in the dataset.

        Returns:
        list: A list of country names.

        Examples
        --------        
        >>> pyetho.country_list()
        ['Afghanistan',
        'Albania',
        'Algeria',
        'Andorra',
        'Angola',
        'Antigua_and_Barbuda',
        'Argentina',
        'Armenia',
        'Australia',
        'Austria',
        'Azerbaijan',
        'Bahamas',
        'Bahrain',
        'Bangladesh',
        'Barbados',
        etc']
        """
         a=[]
         for i in data.keys():
             a.append(i)
         return(a)

def country_summary(country_name="India"):
         """
        Get a summary of the specified country.

        Parameters:
        country_name : str, optional
            The name of the country will be given to retrieve the summary. Default choice is "India".

        Returns:
        str: A summary of the specified country will be returned in a string format.

        Examples
        --------        
        >>> pyetho.country_summary('Sri_Lanka')
        'Sri Lanka is a country in Asia that is home to 22,156,000 people. It is also home to 5 living indigenous languages. Two of these, Sinhala and Tamil, are the official languages of the country. In addition, 2 living non-indigenous languages are established within the country. In formal education, 2 indigenous languages are used as languages of instruction.'
        
        >>> pyetho.country_summary('China')
        'China is a country in Asia that is home to 1,412,600,000 people. It is also home to 281 living indigenous languages. One of these, Mandarin Chinese, is the official language of the country. Others—Central Tibetan, Kyrgyz, and Uyghur—are official languages in parts of the country. China was also home to 2 indigenous languages that are now extinct. In addition, 25 living non-indigenous languages are established within the country. In formal education, 7 indigenous languages are used as languages of instruction.'

        """
         return(data[country_name]['summary'])

def country_officialname(country_name="India"):
         """
        Get the official name of the specified country.

        Parameters:
        country_name : str, optional
            The name of the country will be given to retrieve the official name. Default choice is "India".

        Returns:
        str: The official name of the specified country will be returned in a string format.

        Examples
        --------
        >>> pyetho.country_officialname('Thailand')
        'Kingdom of Thailand'

        >>> pyetho.country_officialname('Algeria')
        'Democratic and Popular Republic of Algeria'
        
        """
         return(data[country_name]['official_name'])

def country_code(country_name="IN"):
         """
        Get the country code (ISO3166) of the specified country.

        Parameters:
        country_name : str, optional
            The name of the country will be given to retrieve the country code. Default choice is "IN".

        Returns:
        str: The country code (ISO3166) of the specified country will be returned in a string format.
        
        Examples:
        --------
        >>> pyetho.country_code("Algeria")
        DZ

        >>> pyetho.country_code("Japan")
        JP
        """
         return(data[country_name]['country_code(ISO3166)'])

def country_area(country_name="India"):
         """
        Get the area of the specified country.

        Parameters:
        country_name : str, optional
            The name of the country will be given to retrieve the area. Default choice is "India".

        Returns:
        str: The area of the specified country will be returned in string format as 'square kilometers'.
        
        Examples:
        --------
        >>> pyetho.country_area("Bangladesh")
        '130170 Square Kilometer'

        >>> pyetho.country_area("Argentina")
        '2736690 Square Kilometer'
        """
         return(str(data[country_name]['area(sq_km)'])+" Square Kilometer")

def country_commencement(country_name="India"):
         """
        Get the commencement year of the specified country.

        Parameters:
        country_name : str, optional
            The name of the country will be given to retrieve the commencement year. Default choice is "India".

        Returns:
        int: The commencement year of the specified country will be returned in integer format.
        
        Examples:
        --------
        >>> pyetho.country_commencement('Pakistan')
        1947

        >>> pyetho.country_commencement('Japan')
        1956

        >>> pyetho.country_commencement('Mexico')
        1945
        """
         return(data[country_name]['commencement'])

def country_continent(country_name="India"):
         """
        Get the continent of the specified country.

        Parameters:
        country_name : str, optional
            The name of the country will be given to retrieve the continent. Default choice is "India".

        Returns:
        str: The continent of the specified country will be returned in a string format.
        
        Examples:
        --------
        >>> pyetho.country_continent('Sri_Lanka')
        'Asia'

        >>> pyetho.country_continent('New_Zealand')
        'Australia'

        """
         return(data[country_name]['continent'])

def country_families(country_name="India"):
         """
        Get the language families present in the specified country.

        Parameters:
        country_name : str, optional
            The name of the country will be given to retrieve the language families. Default choice is "India".

        Returns:
        dict: The language families present in the specified country will be returned in a dict format.
        
        Examples:
        --------
        >>> pyetho.country_families('China')
        dict_keys(['Sino-Tibetan', 'Kra-Dai', 'Hmong-Mien', 'Austro-Asiatic', 'Mongolic', 'Turkic', 'Tungusic', 'Mixed language', 'Sign language', 'Austronesian', 'Indo-European', 'Unclassified'])
        
        >>> pyetho.country_families('Thailand')
        dict_keys(['Austro-Asiatic', 'Kra-Dai', 'Sino-Tibetan', 'Austronesian', 'Sign language', 'Hmong-Mien'])
        """

         return(data[country_name]['families'].keys())

def country_vitality(country_name="India"):
         """
        Get the vitality of languages in the specified country.

        Parameters:
        country_name : str, optional
            The name of the country will be given to retrieve the language vitality. Default choice is "India".

        Returns:
        list: The vitality of languages in the specified country will be returned as a list format.
        
        Examples:
        --------
        >>> pyetho.country_vitality("Mexico")
         ['Institutional', '0', 'Stable', '155', 'Endangered', '129', 'Extinct', '13']

        >>> pyetho.country_vitality("Switzerland")
        ['Institutional', '3', 'Stable', '5', 'Endangered', '2', 'Extinct', '0']

        >>> pyetho.country_vitality("Thailand")
        ['Institutional', '3', 'Stable', '25', 'Endangered', '23', 'Extinct', '0']

        """
         return(data[country_name]['vitality'])

def continent_countries(continent="Asia"):
         """
        Get a list of countries in the specified continent.

        Parameters:
        continent_name : str, optional
            The name of the continent will be given to retrieve the list of countries. Default choice is "Asia".

        Returns:
        list: A list of country names in the specified continent will be returned in list format.
        
        Examples:
        --------
        >>> pyetho.continent_countries('Australia')
        
        ['Australia',
        'Fiji',
        'Kiribati',
        'Marshall_Islands',
        'Micronesia',
        'Nauru',
        'Netherlands',
        'New_Zealand',
        'Palau',
        'Papua_New_Guinea',
        'Samoa',
        'Solomon_Islands',
        'Tonga',
        'Tuvalu',
        'Vanuatu']

        >>>  pyetho.continent_countries('Africa')

        ['Algeria',
        'Angola',
        'Benin',
        'Botswana',
        'Burkina_Faso',
        'Burundi',
        'Côte_dIvoire',
        'Cape_Verde_Islands',
        'Cameroon',
        'Central_African_Republic',
        'Chad',
        'Comoros',
        'Congo',
        'Democratic_Repulic_of_the_Congo',
        'Djibouti',
        'Egypt',
        'Equatorial_Guinea',
        'Eritrea',
        'Eswatini',
        'Ethiopia',
        'Gabon',
        'Gambia',
        'Ghana',
        'Guinea',
        'Guinea-Bissau',
        'Kenya',
        'Lesotho',
        'Liberia',
        'Libya',
        'Madagascar',
        'Malawi',
        'Mali',
        'Mauritania',
        'Mauritius',
        'Morocco',
        'Mozambique',
        'Namibia',
        'Niger',
        'Nigeria',
        'Rwanda',
        'São_Tomé e_Príncipe',
        'Senegal',
        'Seychelles',
        'Sierra_Leone',
        'Somalia',
        'South_Africa',
        'South_Sudan',
        'Sudan',
        'Tanzania',
        'Togo',
        'Tunisia',
        'Zambia',
        'Zimbabwe']
        """
         conti=[]
         for i in data.keys():
             if(data[i]['continent'] == continent):
                 conti.append(i)
         return(conti)

def total_countries():
         """
        Print the total number of countries in the dataset.

        Examples:
        --------
        >>> pyetho.total_countries()
        195 

        """
         print(len(data.keys()))

def continent_length(continent="Asia"):
         """
        Get the total number of countries in the specified continent.

        Parameters:
        continent_name : str, optional
            The name of the continent will be given to retrieve the number of countries. Default choice is "Asia".

        Returns:
        int: The total number of countries in the specified continent will be returned in integer format.
        
        Examples:
        --------
        >>> pyetho.continent_length("Africa")
        53

        >>> pyetho.continent_length("Australia")
        15
        
        """
         conti=[]
         for i in data.keys():
             if(data[i]['continent'] == continent):
                 conti.append(i)
         return(len(conti))

def country_languages(country_name="India"):
        """
        Get a list of languages spoken in the specified country.

        Parameters:
        country_name : str, mandatory
            The name of the country will be given to retrieve the list of languages.

        Returns:
        list: A list of languages spoken in the specified country will be returned in a list format.
    
        Examples:
        --------
        >>> pyetho.country_languages('Namibia')

        ['!Xóõ',
        'Fwe',
        'Gciriku',
        'Hai|ǁom',
        'Herero',
        'Ju hoansi',
        'Khoekhoe',
        'Khwedam',
        'Kuhane',
        'Kung-Ekoka',
        'Kwambi',
        'Kwangali',
        'Kwanyama',
        'Mbalanhu',
        'Mbukushu',
        'Namibian_Sign_Language',
        'Naro',
        'Ndonga',
        'Ngandjera',
        'Northwestern_!Kung',
        'Setswana',
        'Yeyi',
        'Zemba']

         >>> pyetho.country_languages('Japan')
        
        ['Ainu',
        'Amami_Koniya_Sign_Language',
        'Central_Okinawan',
        'Japanese',
        'Japanese_Sign_Language',
        'Kikai',
        'Kunigami',
        'Miyako',
        'Miyakubo_Sign_Language',
        'Northern_Amami-Oshima',
        'Oki-No-Erabu',
        'Southern_Amami-Oshima',
        'Toku-No-Shima',
        'Yaeyama',
        'Yonaguni',
        'Yoron']
        """

        x = []
        for i in data[country_name]['languages']:
            x.append(i)
        return x
  
def language_summary( country_name="India", lang="Tamil"):
        """
        Get the summary of the specified language spoken in the country.

        Parameters:
        country_name : str, mandatory
            The name of the country will be given to retrive the specified country's language.
        
        lang : str, mandatory
            The name of the language will be given to retrieve the specified language's summary.

        Returns:
        str: A summary of the specified language spoken in the country will be returned in a string format.
        
        Examples:
        --------
        >>> pyetho.language_summary('India','Tamil')
        'Tamil is an official language in the parts of India where it is spoken. It belongs to the Dravidian language family. Direct evidence is lacking, but the language is thought to be used as a first language by all in the ethnic community. It is used as a language of instruction in education.'

        >>> pyetho.language_summary('Namibia','Fwe')
        'Fwe is a stable indigenous language of Namibia and Zambia. It belongs to the Niger-Congo language family. The language is used as a first language by all in the ethnic community. It is not known to be taught in schools.'
        """
        return (data[country_name]['languages'][lang]['summary'])

def language_code(country_name="India", lang="Tamil"):
        """
        Get the language code (ISO639) of the specified language spoken in the country.

        Parameters:
        country_name : str, mandatory
            The name of the country will be given to retrive the specified country's language.

        lang : str, mandatory
            The name of the language will be given to retrieve the specified language's code.

        Returns:
        str: The language code (ISO639) of the specified language spoken in the country will be returned in a string format.
        
        Examples:
        --------
        >>> pyetho.language_code('India','Tamil')
        'tam'

        >>> pyetho.language_code('Argentina','Lule')
        'ule'
        """
        return (data[country_name]['languages'][lang]['language_code(ISO639)'])

def language_population(country_name="India", lang="Tamil"):
        """
        Get the population estimate of speakers for the specified language in the country.

        Parameters:
        country_name : str, mandatory
            The name of the country will be given to retrive the specified country's language.

        lang : str, mandatory
            The name of the language will be given to retrieve the specified language's population.

        Returns:
        str: The population estimate of speakers for the specified language in the country will be returned in a string format.
        
        Examples:
        --------
        >>> pyetho.language_population('India','Tamil')
        '1M to 1B'

        >>> pyetho.language_population('Mexico','Yaqui')
        '10K to 1M'
        """
        return (data[country_name]['languages'][lang]['population'])

def language_family(country_name="India", lang="Tamil"):
        """
        Get the language family to which the specified language belongs in the country.

        Parameters:
        country_name : str, mandatory
            The name of the country will be given to retrive the specified country's language.

        lang : str, mandatory
            The name of the language will be given to retrieve the specified language's family.

        Returns:
        str: The language family to which the specified language belongs in the country will be returned in a string format.
        
        Examples:
        --------
        >>> pyetho.language_family('India','Tamil')
        'It belongs to the Dravidian language family.'

        >>> pyetho.language_family('China','Zhaba')
        'It belongs to the Sino-Tibetan language family.'

        >>> pyetho.language_family('Mexico','Yaqui')
        'It belongs to the Uto-Aztecan language family.'
        """
        return (data[country_name]['languages'][lang]['family'])

def lang_to_country(lang="Tamil"):

        """
        Get the names of countries where a specific language is spoken and its language family.

        Parameters:
        lang : str, optional
             The name of the language for which you want to find countries. Default is "Tamil".

        Returns:
        list: A list of country names where the specified language is spoken.

        Examples:
        --------
        >>> pyetho.lang_to_country('Tamil')
        India
        Sri_Lanka

        >>> pyetho.lang_to_country('Spanish')
        Andorra
        Spain
        """

        for i in data.keys():
            a=[]
            for j in data[i]['languages'].keys():
                a.append(j)
            for k in a:
                l=str(lang).capitalize()
                if(l == k):
                    print(i)
                    break
def languagecode_to_country(code):
        """
        Get the names of countries where a specific language code (ISO 639) is associated.

        Parameters:
        code : str, mandatory
            The ISO 639 language code for which you want to find countries.

        Returns:
        list: A list of country names where the specified language_code is associated.

        Examples:
        --------
        >>> pyetho.languagecode_to_country('eng')
        Ireland
        United_Kingdom
        
        >>> pyetho.languagecode_to_country('spa')
        Andorra
        Spain
        """
        for i in data.keys():
            for j in data[i]["languages"]:
                a=[]
                a.append(data[i]["languages"][j]["language_code(ISO639)"])
                for k in  a:
                    if (code == k):
                        print(i)
    
def country_family_languages(country_name="India",family_name="Dravidian"):
        """
        Retrieve the languages associated with a specific language family in a given country.

        Parameters:
        country_name : str, mandatory 
            The name of the country to search for the specified family.
        family_name : str, mandatory 
            The name of the language family to get the list of languages inside that specific family.
        

        Returns:
        - list : A list of languages and its language code associated with the provided 'country_name' in the specified 'family_name'.

        Examples:
        --------
        >>> pyetho.country_family_languages('Japan','Japonic')
        ["Japanese 'Language Code':jpn",
        "Amami-Oshima, Southern 'Language Code':ams",
        "Kikai 'Language Code':kzg",
        "Amami-Oshima, Northern 'Language Code':ryn",
        "Toku-No-Shima 'Language Code':tkn",
        "Oki-No-Erabu 'Language Code':okn",
        "Okinawan, Central 'Language Code':ryu",
        "Kunigami 'Language Code':xug",
        "Yoron 'Language Code':yox",
        "Miyako 'Language Code':mvi",
        "Yaeyama 'Language Code':rys",
        "Yonaguni 'Language Code':yoi"]

        >>> pyetho.country_family_languages('India','Dravidian')
        ["Kolami, Northwestern 'Language Code':kfb",
        "Kolami, Southeastern 'Language Code':nit",
        "Gadaba, Mudhili 'Language Code':gau",
        "Gadaba, Pottangi Ollar 'Language Code':gdb",
        "Duruwa 'Language Code':pci",
        "Kumarbhag Paharia 'Language Code':kmj",
        "Kurux 'Language Code':kru",
        "Sauria Paharia 'Language Code':mjt",
        "Kisan 'Language Code':xis",
        "Maria, Dandami 'Language Code':daq",
        "Muria, Eastern 'Language Code':emu",
        "Gondi, Aheri 'Language Code':esg",
        "Muria, Far Western 'Language Code':fmu",
        "Gondi, Northern 'Language Code':gno",
        "Khirwar 'Language Code':kwx",
        "Maria 'Language Code':mrr",
        "Muria, Western 'Language Code':mut",
        "Nagarchal 'Language Code':nbg",
        "Pardhan 'Language Code':pch",
        "Gondi, Adilabad 'Language Code':wsg",
        "Konda-Dora 'Language Code':kfc",
        "Mukha-Dora 'Language Code':mmk",
        "Kui, Dawik 'Language Code':dwk",
        "Koya 'Language Code':kff",
        "Kuvi 'Language Code':kxv",
        "Kui 'Language Code':uki",
        "Manda 'Language Code':mha",
        "Pengo 'Language Code':peg",
        "Chenchu 'Language Code':cde",
        "Manna-Dora 'Language Code':mju",
        "Telugu 'Language Code':tel",
        "Waddar 'Language Code':wbq",
        "Kurichiya 'Language Code':kfh",
        "Kurumba, Attapady 'Language Code':pkr",
        "Pathiya 'Language Code':pty",
        "Muduga 'Language Code':udg",
        "Kumbaran 'Language Code':wkb",
        "Kalanadi 'Language Code':wkl",
        "Kunduvadi 'Language Code':wku",
        "Badaga 'Language Code':bfq",
        "Holiya 'Language Code':hoy",
        "Kannada 'Language Code':kan",
        "Urali 'Language Code':url",
        "Kodava 'Language Code':kfa",
        "Kurumba, Kannada 'Language Code':kfi",
        "Kurumba, Mullu 'Language Code':kpb",
        "Kurumba, Alu 'Language Code':xua",
        "Kurumba, Jennu 'Language Code':xuj",
        "Mannan 'Language Code':mjv",
        "Aranadan 'Language Code':aaf",
        "Kadar 'Language Code':kej",
        "Malayalam 'Language Code':mal",
        "Malapandaram 'Language Code':mjp",
        "Malaryan 'Language Code':mjq",
        "Malavedan 'Language Code':mjr",
        "Paliyan 'Language Code':pcf",
        "Paniya 'Language Code':pcg",
        "Ravula 'Language Code':yea",
        "Eravallan 'Language Code':era",
        "Irula 'Language Code':iru",
        "Kaikadi 'Language Code':kep",
        "Kanikkaran 'Language Code':kev",
        "Muthuvan 'Language Code':muv",
        "Sholaga 'Language Code':sle",
        "Tamil 'Language Code':tam",
        "Kurumba, Betta 'Language Code':xub",
        "Yerukula 'Language Code':yeu",
        "Kota 'Language Code':kfe",
        "Toda 'Language Code':tcx",
        "Chetti, Wayanad 'Language Code':ctt",
        "Bellari 'Language Code':brw",
        "Kudiya 'Language Code':kfg",
        "Tulu 'Language Code':tcy",
        "Koraga, Korra 'Language Code':kfd",
        "Koraga, Mudu 'Language Code':vmd",
        "Mala Malasar 'Language Code':ima",
        "Thachanadan 'Language Code':thn",
        "Ullatan 'Language Code':ull",
        "Malasar 'Language Code':ymr",
        "Allar 'Language Code':all",
        "Bharia 'Language Code':bha",
        "Malankuravan 'Language Code':mjo",
        "Pattapu 'Language Code':ptq",
        "Vishavan 'Language Code':vis"]

        """

        b = []
        for i in data[country_name]['families'][family_name]:
            modified_string = i[:-4] + " 'Language Code':" + i[-3:]
            b.append(modified_string)

        return b

def language_to_family(language_name="Tamil"):
        """
        Retrieve the family name associated with a specific language.

        Parameters:
        language_name : str, mandatory 
            The name of the language given to search for the specified family.
    
        Returns:
        - str : The family name associated with the provided 'language_name'.

        Examples:
        --------
        >>> pyetho.language_to_family('Tamil')
        'Dravidian'

        >>> pyetho.language_to_family('Japanese')
        'Japonic'

        >>> pyetho.language_to_family('English')
        'Creole'

        """
        a=[]
        for i in data.keys():
            for j,k in data[i]["families"].items():
                a.append(k)
                for l in range(len(a)):
                    for m in range(len(a[l])):
                        if language_name in (a[l][m][:-4:]):
                            return j       
        
def all_families_list():
        """
        Retrieve all the family names associated with all the countries.
    
        Returns:
        - list : A list of all families associated with all the countries.

        Examples:
        --------
        >>> pyetho.all_families_list()
        ['Eskimo-Aleut', 'Comecrudan', 'Nimboran', 'Yukian', 'Sepik', 'Uralic', 
        'South-Central Papuan', 'Katukinan', 'Aymaran', 'Coosan', etc.,]

        """
        a=[]
        for i in data.keys():
            for j in data[i]['families'].keys():
                a.append(j)
        unique_list = list(set(a))
        print (unique_list)

def total_families():
        """
        Retrieve the number of unique family names associated with all the countries.
    
        Returns:
        - int : The number of unique family names associated with all the countries.

        Examples:
        --------
        >>> pyetho.total_families()
        153

        """
        a=[]
        for i in data.keys():
            for j in data[i]['families'].keys():
                a.append(j)
        unique_list = list(set(a))
        print (len(unique_list))

def family_to_country(family_name="Dravidian"):
        """
        Retrieve the country names associated with a specific family_name.

        Parameters:
        family_name : str, mandatory 
            The name of the family to search for the associated countries.
    
        Returns:
        - list or str : A list of country names associated with the provided 'family_name'.

        Examples:
        --------
        >>> pyetho.family_to_country('Dravidian')
        Afghanistan
        Bangladesh
        India
        Nepal
        Pakistan
        Sri_Lanka

        >>> pyetho.family_to_country('Japonic')
        Japan
        """
        for i in data.keys():
            a=[]
            for j in data[i]['families'].keys():
                a.append(j)
            for k in a:
                l=str(family_name).capitalize()
                if(l in k):
                    print(i)
                    break

def all_family_languages(family):
            """
            Retrieve all languages within a specific language family across all countries.

            Parameters:
            family : str
                The name of the language family to retrieve languages from the family name.

            Returns:
            list : A list of languages within the specified 'family' across all countries.

             >>> pyetho.family_to_country('Japonic')
             [['Japanese jpn',
            'Amami-Oshima, Southern ams',
            'Kikai kzg',
            'Amami-Oshima, Northern ryn',
            'Toku-No-Shima tkn',
            'Oki-No-Erabu okn',
            'Okinawan, Central ryu',
            'Kunigami xug',
            'Yoron yox',
            'Miyako mvi',
            'Yaeyama rys',
            'Yonaguni yoi']]

            >>> pyetho.family_to_country(')
            [[],
            [],
            ['Kolami, Northwestern kfb',
            'Kolami, Southeastern nit',
            'Gadaba, Mudhili gau',
            'Gadaba, Pottangi Ollar gdb',
            'Duruwa pci',
            'Kumarbhag Paharia kmj',
            'Kurux kru',
            'Sauria Paharia mjt',
            'Kisan xis',
            'Maria, Dandami daq',
            'Muria, Eastern emu',
            etc.,]

            """
            result = []
            for i in data.keys():
                if family in data[i]['families']:
                    result.append(data[i]['families'][family])
            return result

    
