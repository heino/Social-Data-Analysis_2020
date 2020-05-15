from bokeh.transform import factor_cmap

continent_colors = {
    'AS': '#90d595',
    'EU': '#adb0ff', 
    'AF': '#e48381', 
    'OC': '#aafbff',
    'AN': '#ffb3ff',
    'SA': '#f7bb5f'#,
    #np.NaN: '#999999'
}

region_colors = {
    'Asia': '#90d595',
    'Europe': '#adb0ff',
    'Africa': '#e48381',
    'Oceania': '#aafbff',
    'Americas': '#ffb3ff'#,
#     np.NaN: '#999999'
}


focus_countries ={
    'DNK': '#d62728',
    'SWE': '#1f77b4',
    'DEU': '#7f7f7f',
    'FRA': '#ff7f0e',
    'GBR': '#9467bd',
    'BEL': '#17becf',
    'ITA': '#e377c2',
    'ESP': '#bcbd22',
    'USA': '#2ca02c',
    'CHN': '#8c564b'
}

subregion_colors = {
    'Southern Europe': '#adb0ff',
    'Western Europe': '#adb0ff',
    'Northern Europe': '#adb0ff',
    'Eastern Europe': '#adb0ff',

    'Northern America': '#ffb3ff',
    'Latin America and the Caribbean': '#ffb3ff',

    'Central Asia': '#90d595',
    'Southern Asia': '#90d595',
    'South-eastern Asia': '#90d595',
    'Eastern Asia': '#90d595',
    'Western Asia': '#90d595',

    'Northern Africa': '#e48381',
    'Sub-Saharan Africa': '#e48381',

    'Australia and New Zealand': '#aafbff',

    'Polynesia': '#aafbff',
    'Micronesia': '#aafbff',
    'Melanesia': '#aafbff'#,

#     np.NaN: '#999999'        
}
# '#30123b', '#4584f9', '#1ae4b6', '#a1fc3d', '#f9ba38', '#e5460a', '#7a0402'
economy_colors = {
'5. Emerging region: G20' : '#f9ba38',
'2. Developed region: nonG7' : '#4584f9', 
'7. Least developed region' : '#7a0402', 
# '1. Developed region: G7' : '#003366', 
'1. Developed region: G7' : '#30123b', 
'6. Developing region' : '#e5460a', 
'4. Emerging region: MIKT' : '#a1fc3d', 
'3. Emerging region: BRIC' : '#1ae4b6'
}

def subregion_color_map(column_name):
    return factor_cmap(column_name,
                            list(subregion_colors.values()), 
                            factors = list(subregion_colors.keys())
                            )

def region_color_map(column_name):
    return factor_cmap(column_name,
                        list(region_colors.values()), 
                        factors = list(region_colors.keys())
                        )

def continent_color_map(column_name):
    return factor_cmap(column_name,
                        list(continent_colors.values()), 
                        factors = list(continent_colors.keys())
                        )


stock_country_colors = {
    'AUS': subregion_colors['Australia and New Zealand'],
    'AUT': subregion_colors['Western Europe'],
    'BEL': subregion_colors['Western Europe'],
    'BRA': subregion_colors['Latin America and the Caribbean'],
    'CAN': subregion_colors['Northern America'],
    'CHE': '#000000',
    'CHN': '#000000',
    'DEU': subregion_colors['Western Europe'],
    'DNK': subregion_colors['Northern Europe'],
    'ESP': subregion_colors['Southern Europe'],
    'FIN': subregion_colors['Northern Europe'],
    'FRA': subregion_colors['Western Europe'],
    'GBR': subregion_colors['Western Europe'],
    'GRC': '#000000',
    'IND': '#000000',
    'IRL': subregion_colors['Western Europe'],
    'ISL': '#000000',
    'ISR': '#000000',
    'ITA': subregion_colors['Southern Europe'],
    'JPN': '#000000',
    'KOR': '#000000',
    'MEX': subregion_colors['Latin America and the Caribbean'],
    'NLD': subregion_colors['Western Europe'],
    'NZL': subregion_colors['Australia and New Zealand'],
    'POL': subregion_colors['Eastern Europe'],
    'PRT': subregion_colors['Southern Europe'],
    'RUS': '#000000',
    'SGP': '#000000',
    'SWE': subregion_colors['Northern Europe'],
    'TWN': '#000000',
    'USA': subregion_colors['Northern America'],
    'ZAF': '#90d595'
}
