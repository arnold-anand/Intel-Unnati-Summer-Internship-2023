import requests
from bs4 import BeautifulSoup
import pandas as pd

# List of URLs
f = open('url.txt','r')
urls = f.readlines()

data = []

# Iterate through the URLs
for url in urls:
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    print(url)
    ram = soup.find('td', string='RAM').find_next_sibling('td').text.strip()
    processor = soup.find('td', string='Processor').find_next_sibling('td').text.strip()
    battery = soup.find('td', string='Battery').find_next_sibling('td').text.strip()
    rear_camera = soup.find('td', string='Rear Camera').find_next_sibling('td').text.strip()
    front_camera = soup.find('td', string='Front Camera').find_next_sibling('td').text.strip()
    display = soup.find('td', string='Display').find_next_sibling('td').text.strip()
    launch_date = soup.find('td', string='Launch Date').find_next_sibling('td').text.strip()
    operating_system = soup.find('td', string='Operating System').find_next_sibling('td').text.strip()
    chipset = soup.find('td', string='Chipset').find_next_sibling('td').text.strip()
    fabrication  = soup.find('td', string='Fabrication').find_next_sibling('td').text.strip() 
    graphics  = soup.find('td', string='Graphics').find_next_sibling('td').text.strip()
    display_type  = soup.find('td', string='Display Type').find_next_sibling('td').text.strip()
    pixel_density  = soup.find('td', string='Pixel Density').find_next_sibling('td').text.strip()
    s2b_ratio  = soup.find('td', string='Screen to Body Ratio (claimed by the brand)').find_next_sibling('td').text.strip()
    brightness  = soup.find('td', string='Brightness').find_next_sibling('td').text.strip()
    refresh_rate = soup.find('td', string='Refresh Rate').find_next_sibling('td').text.strip()
    capacity  = soup.find('td', string='Capacity').find_next_sibling('td').text.strip()
    fast_charging  = soup.find('td', string='Quick Charging').find_next_sibling('td').text.strip()
    type_c  = soup.find('td', string='USB Type-C').find_next_sibling('td').text.strip()
    internal_memory  = soup.find('td', string='Internal Memory').find_next_sibling('td').text.strip()
    expandable_memory  = soup.find('td', string='Expandable Memory').find_next_sibling('td').text.strip()
    wifi  = soup.find('td', string='Wi-Fi').find_next_sibling('td').text.strip()
    bluetooth  = soup.find('td', string='Bluetooth').find_next_sibling('td').text.strip()
    GPS  = soup.find('td', string='GPS').find_next_sibling('td').text.strip()
    audio_jack  = soup.find('td', string='Audio Jack').find_next_sibling('td').text.strip()
    sim_slot  = soup.find('td', string='SIM Slot(s)').find_next_sibling('td').text.strip()
    fingerprint_sensor  = soup.find('td', string='Fingerprint Sensor').find_next_sibling('td').text.strip()

    # Create a dictionary for the current phone's data
    phone_data = {
        'RAM': ram,
        'Processor': processor,
        'Battery': battery,
        'Rear Camera': rear_camera,
        'Front Camera': front_camera,
        'Display': display,
        'Launch Date': launch_date,
        'Operating System': operating_system,
        'Chipset': chipset,
        'Fabrication': fabrication,
        'Graphics': graphics,
        'Display Type': display_type,
        'Pixel Density': pixel_density,
        'Screen to Body Ratio': s2b_ratio,
        'Brightness': brightness,
        'Refresh Rate': refresh_rate,
        'Capacity': capacity,
        'Quick Charging': fast_charging,
        'USB Type-C': type_c,
        'Internal Memory': internal_memory,
        'Expandable Memory': expandable_memory,
        'Wi-Fi': wifi,
        'Bluetooth': bluetooth,
        'GPS': GPS,
        'Audio Jack': audio_jack,
        'SIM Slot(s)': sim_slot,
        'Fingerprint Sensor': fingerprint_sensor
    }

    data.append(phone_data)

# Create a DataFrame from the collected data
df = pd.DataFrame(data)
df.to_csv('mobile_data.csv', index=False)
# Print the DataFrame
# print(df)
