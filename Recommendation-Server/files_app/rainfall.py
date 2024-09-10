# Example data
# Complete data will be made available upon request

rainfall_data = [{'State': 'andaman and nicobar islands',
  'Cities': [{'Area': 'nicobar',
    'Jan_Feb': 16.52,
    'March_May': 54.07,
    'June_September': 120.72,
    'October_December': 89.21,
    'Annual': 280.52},
   {'Area': 'n & m andaman',
    'Jan_Feb': 4.86,
    'March_May': 40.56,
    'June_September': 188.44,
    'October_December': 57.47,
    'Annual': 291.33}]}]


def rainfall_info(state_name, city_name, month_name):
    # State name
    for state in rainfall_data:
        if state['State'] == state_name.lower():
            
            # Area name
            for city in state['Cities']:
                if city['Area'] == city_name.lower():
                    
                    # Match month to the category
                    if month_name in ['January', 'February']:
                        return city['Jan_Feb']
                    elif month_name in ['March', 'April', 'May']:
                        return city['March_May']
                    elif month_name in ['June', 'July', 'August', 'September']:
                        return city['June_September']
                    elif month_name in ['October', 'November', 'December']:
                        return city['October_December']
                    
    return None