import requests
from bs4 import BeautifulSoup
import pandas as pd

# List of URLs
f = open('url.txt','r')
urls = f.readlines()


data = []
count = 0
for url in urls:
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    name = soup.find('h1', {'class': 'h1_pro_head'}).text.strip()
    price = soup.find('span', {'class': 'store_prc'}).text.strip() if soup.find('span', {'class': 'store_prc'}) else soup.find('span', {'class': 'big_prc'}).text.strip()
    brand = name.split() 
    brandname = brand[0]
    ram = soup.find('td', string='RAM').find_next_sibling('td').text.strip() if soup.find('td', string='RAM') else None
    processor = soup.find('td', string='Processor').find_next_sibling('td').text.strip() if soup.find('td', string='Processor') else None
    battery = soup.find('td', string='Battery').find_next_sibling('td').text.strip() if soup.find('td', string='Battery') else None
    rear_camera = soup.find('td', string='Rear Camera').find_next_sibling('td').text.strip() if soup.find('td', string='Rear Camera') else None
    front_camera = soup.find('td', string='Front Camera').find_next_sibling('td').text.strip() if soup.find('td', string='Front Camera') else None
    display = soup.find('td', string='Display').find_next_sibling('td').text.strip() if soup.find('td', string='Display') else None
    launch_date = soup.find('td', string='Launch Date').find_next_sibling('td').text.strip() if soup.find('td', string='Launch Date') else None
    operating_system = soup.find('td', string='Operating System').find_next_sibling('td').text.strip() if soup.find('td', string='Operating System') else None
    chipset = soup.find('td', string='Chipset').find_next_sibling('td').text.strip() if soup.find('td', string='Chipset') else None
    fabrication = soup.find('td', string='Fabrication').find_next_sibling('td').text.strip() if soup.find('td', string='Fabrication') else None
    graphics = soup.find('td', string='Graphics').find_next_sibling('td').text.strip() if soup.find('td', string='Graphics') else None
    display_type = soup.find('td', string='Display Type').find_next_sibling('td').text.strip() if soup.find('td', string='Display Type') else None
    pixel_density = soup.find('td', string='Pixel Density').find_next_sibling('td').text.strip() if soup.find('td', string='Pixel Density') else None
    s2b_ratio = soup.find('td', string='Screen to Body Ratio (claimed by the brand)').find_next_sibling('td').text.strip() if soup.find('td', string='Screen to Body Ratio (claimed by the brand)') else None
    brightness = soup.find('td', string='Brightness').find_next_sibling('td').text.strip() if soup.find('td', string='Brightness') else None
    refresh_rate = soup.find('td', string='Refresh Rate').find_next_sibling('td').text.strip() if soup.find('td', string='Refresh Rate') else None
    capacity = soup.find('td', string='Capacity').find_next_sibling('td').text.strip() if soup.find('td', string='Capacity') else None
    fast_charging = soup.find('td', string='Quick Charging').find_next_sibling('td').text.strip() if soup.find('td', string='Quick Charging') else None
    type_c = soup.find('td', string='USB Type-C').find_next_sibling('td').text.strip() if soup.find('td', string='USB Type-C') else None
    internal_memory = soup.find('td', string='Internal Memory').find_next_sibling('td').text.strip() if soup.find('td', string='Internal Memory') else None
    expandable_memory = soup.find('td', string='Expandable Memory').find_next_sibling('td').text.strip() if soup.find('td', string='Expandable Memory') else None
    wifi = soup.find('td', string='Wi-Fi').find_next_sibling('td').text.strip() if soup.find('td', string='Wi-Fi') else None
    bluetooth = soup.find('td', string='Bluetooth').find_next_sibling('td').text.strip() if soup.find('td', string='Bluetooth') else None
    GPS = soup.find('td', string='GPS').find_next_sibling('td').text.strip() if soup.find('td', string='GPS') else None
    audio_jack = soup.find('td', string='Audio Jack').find_next_sibling('td').text.strip() if soup.find('td', string='Audio Jack') else None
    sim_slot = soup.find('td', string='SIM Slot(s)').find_next_sibling('td').text.strip() if soup.find('td', string='SIM Slot(s)') else None
    fingerprint_sensor = soup.find('td', string='Fingerprint Sensor').find_next_sibling('td').text.strip() if soup.find('td', string='Fingerprint Sensor') else None
    price = soup.find('span', class_='store_prc').text.strip() if soup.find('span', class_='store_prc') else None

    phone_data = {
        'Brand': brandname,
        'Name': name,
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
        'Fingerprint Sensor': fingerprint_sensor,
        'Price' : price
    }
    count+=1
    print(count)
    data.append(phone_data)

df = pd.DataFrame(data)

df.to_csv('mobile_data.csv', index=False)

print(df)
