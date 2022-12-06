#------------------validation and pattern matching------------------#
#validate a zip code using regex
def validate_zip_code(zip_code):
    pattern = re.compile(r'^\d{5}$')
    return pattern.match(zip_code)
#generate a regex to findall words in the following string: "weight = models.CharField(max_length=70)"
def generate_regex():
    pattern = re.compile(r'\w+')
    return pattern.findall("weight = models.CharField(max_length=70)")

#generate a regex to findall zip codes and mac addresses in a string
def generate_regex():
    pattern = re.compile(r'\d{5}|\w{2}:\w{2}:\w{2}:\w{2}:\w{2}:\w{2}')
    return pattern.findall("zip code: 12345, mac address: 12:34:56:78:90:ab")

#validate mac address format
def validate_mac_address(mac_address):
    pattern = re.compile(r'^\w{2}:\w{2}:\w{2}:\w{2}:\w{2}:\w{2}$')
    return pattern.match(mac_address)

#validate a date
def validate_date(date):
    pattern = re.compile(r'^\d{4}-\d{2}-\d{2}$')
    return pattern.match(date)

#generate a regex to match the following datetime format "2022-12-05 11:42:33.059944"
def generate_regex():
    pattern = re.compile(r'\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2}\.\d{6}')
    return pattern.findall("2022-12-05 11:42:33.059944")

#function to validate a polygon
def validate_polygon(polygon):
    pattern = re.compile(r'^\d+,\d+\    \d+,\d+\    \d+,\d+\    \d+,\d+$')
    return pattern.match(polygon)

#function to validate credit card number
def validate_credit_card_number(credit_card_number):
    pattern = re.compile(r'^\d{4}-\d{4}-\d{4}-\d{4}$')
    return pattern.match(credit_card_number)


#generate regex to findall zip codes
#include hyphenated zip codes
def generate_regex():
    pattern = re.compile(r'\d{5}(-\d{4})?')
    return pattern.findall("zip code: 12345, zip code: 12345-6789")

#function to validate a phone number
def validate_phone_number(phone_number):
    pattern = re.compile(r'^\+?1?\d{9,15}$')
    return pattern.match(phone_number)

#function to scan all files in directory and subdirectories
#match and return all phone numbers
def scan_all_files_in_directory_and_subdirectories():
    pattern = re.compile(r'\+?1?\d{9,15}')
    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith(".txt"):
                with open(file, "r") as file:
                    for line in file:
                        if pattern.match(line):
                            print(line)

#asynchronous function to scan all files in directory and subdirectories
#match and return all ip addresses
async def scan_all_files_in_directory_and_subdirectories():
    pattern = re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith(".txt"):
                with open(file, "r") as file:
                    for line in file:
                        if pattern.match(line):
                            print(line)

#----------------------Geometry----------------------#
#function to calculate the area of a triangle
def area_of_triangle(base, height):
    return base * height / 2

#function to calculate the area of a rectangle
def area_of_rectangle(length, width):
    return length * width

#function to calculate the area of a circle
def area_of_circle(radius):
    return math.pi * radius ** 2

#function to calculate the area of a square
def area_of_square(side):
    return side ** 2

#function to calculate the area of a parallelogram
def area_of_parallelogram(base, height):
    return base * height

#function to calculate the area of a trapezoid
def area_of_trapezoid(base1, base2, height):
    return (base1 + base2) / 2 * height

#function to calculate the area of a polygon
def area_of_polygon(sides):
    return sides * (sides - 3) / 2

#unction to calculate the area of a sector
def area_of_sector(radius, angle):
    return math.pi * radius ** 2 * angle / 360

#---------------------Generative Logic ---------------------#
#function to generate a random number
def generate_random_number():
    return random.randint(0, 100)

#function to generate a random number between a range
def generate_random_number_between_range(start, end):
    return random.randint(start, end)

#function to generate secure token
def generate_secure_token():
    return secrets.token_hex(16)

#function to generate secure token of specified size
def generate_secure_token_of_specified_size(size):
    return secrets.token_hex(size)

#function to generate a random string
def generate_random_string():
    return secrets.token_urlsafe(16)

#function to generate a random string of specified size
def generate_random_string_of_specified_size(size):
    return secrets.token_urlsafe(size)

#function to generate a random color
def generate_random_color():
    return secrets.token_hex(3)

#function to generate random paragraph and create a new file called "paragraph.txt" and write the paragraph to the file
def generate_random_paragraph():
    with open("paragraph.txt", "w") as file:
        file.write(" ".join(lorem.paragraph().split()))

#function to generate a sound wave of specified frequency
def generate_sound_wave_of_specified_frequency(frequency):
    return math.sin(frequency)

#function to generate hydrodynamic pressure
def generate_hydrodynamic_pressure(density, velocity, area):
    return density * velocity ** 2 / 2 * area

#function to generate electric field
def generate_electric_field(charge, distance):
    return charge / distance ** 2

#funtion to generate mechanical energy
def generate_mechanical_energy(mass, velocity):
    return mass * velocity ** 2 / 2

#function to generate gravitational field
def generate_gravitational_field(mass, distance):
    return mass / distance ** 2

#function to generate magnetic field
def generate_magnetic_field(magnetic_flux, area):
    return magnetic_flux / area

#function to convert celsius to fahrenheit
def convert_celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

#function to generate a shell script
def generate_shell_script():
    with open("script.sh", "w") as file:
        file.write("#!/bin/bash")
        file.write("echo 'hello world'")

#function to generate a shell script
#shell script should cat first available file in current directory
def generate_shell_script():
    with open("script.sh", "w") as file:
        file.write("#!/bin/bash")
        file.write("cat $(ls -t | head -1)")

#generate a shell script
#install npm and nodejs
def generate_shell_script():
    with open("script.sh", "w") as file:
        file.write("#!/bin/bash")
        file.write("sudo apt install npm")
        file.write("sudo apt install nodejs")

#generate a shell script
#install python3, npm, nodejs, mySQL, mongodb, redis, docker, kubernetes, and docker-compose
#activate an environment and install requirements.txt
def generate_shell_script():
    with open("script.sh", "w") as file:
        file.write("#!/bin/bash")
        file.write("sudo apt install python3")
        file.write("sudo apt install npm")
        file.write("sudo apt install nodejs")
        file.write("sudo apt install mysql")
        file.write("sudo apt install mongodb")
        file.write("sudo apt install redis")
        file.write("sudo apt install docker")
        file.write("sudo apt install kubernetes")
        file.write("sudo apt install docker-compose")
        file.write("python3 -m venv env")
        file.write("source env/bin/activate")
        file.write("pip install -r requirements.txt")

#generate a shell script
#launch a docker container
def generate_shell_script():
    with open("script.sh", "w") as file:
        file.write("#!/bin/bash")
        file.write("docker run -p 80:80 -d nginx")

#generate a shell script
#launch 3 docker containers
#one on 80:80 for nginx and the other two on 8080:80 for django and angular, respectively
def generate_shell_script():
    with open("script.sh", "w") as file:
        file.write("#!/bin/bash")
        file.write("docker run -p 80:80 -d nginx")
        file.write("docker run -p 8080:80 -d django")
        file.write("docker run -p 8080:80 -d angular")

#generate a python script to launch a docker container
def generate_python_script_to_launch_docker_container():
    with open("script.py", "w") as file:
        file.write("import os")
        file.write("os.system('docker run -d -p 80:80 nginx')")

#generate a python script to launch angular and django containers
def generate_python_script_to_launch_angular_and_django_containers():
    with open("script.py", "w") as file:
        file.write("import os")
        file.write("os.system('docker run -d -p 80:80 nginx')")
        file.write("os.system('docker run -d -p 8000:8000 django')")
        file.write("os.system('docker run -d -p 4200:4200 angular')")


#---------------------Computation and Optimization---------------------#
#create a class using multithreading
class Multithreading:
    def __init__(self, function, *args):
        self.function = function
        self.args = args
        self.thread = threading.Thread(target=self.function, args=self.args)
        self.thread.start()

#create a class using multiprocessing
class Multiprocessing:
    def __init__(self, function, *args):
        self.function = function
        self.args = args
        self.process = multiprocessing.Process(target=self.function, args=self.args)
        self.process.start()

#function to return time taken to execute a function
def time_taken_to_execute_function(function):
    start = time.time()
    function()
    end = time.time()
    return end - start

#function to return time taken to execute a function using multithreading
def time_taken_to_execute_function_using_multithreading(function):
    start = time.time()
    Multithreading(function)
    end = time.time()
    return end - start

#function to return time taken to execute a function using multiprocessing
def time_taken_to_execute_function_using_multiprocessing(function):
    start = time.time()
    Multiprocessing(function)
    end = time.time()
    return end - start

#function to return time taken to execute a function using asyncio
def time_taken_to_execute_function_using_asyncio(function):
    start = time.time()
    asyncio.run(function)
    end = time.time()
    return end - start

#class showing asnychronous programming
class Asyncio:
    def __init__(self, function, *args):
        self.function = function
        self.args = args
        self.loop = asyncio.get_event_loop()
        self.loop.run_until_complete(self.function(*self.args))

    async def function(self, *args):
        pass

#function to return time taken to execute a function using asyncio
def time_taken_to_execute_function_using_asyncio(function):
    start = time.time()
    Asyncio(function)
    end = time.time()
    return end - start

#---------------------Automation---------------------#

#function to display mechanical energy on matplotlib
def display_mechanical_energy_on_matplotlib():
    x = np.linspace(0, 10, 1000)
    y = np.sin(x)
    plt.plot(x, y)
    plt.show()

#function to launch jupyter notebook in a browser
def launch_jupyter_notebook_in_browser():
    os.system("jupyter notebook")

#function to launch jupyter notebook in a browser
#using subprocess shell
def launch_jupyter_notebook_in_browser():
    subprocess.run("jupyter notebook", shell=True)

#function to periodically scan for devices on a network
#and display the results on matplotlib
def periodically_scan_for_devices_on_network_and_display_results_on_matplotlib():
    x = []
    y = []
    while True:
        x.append(datetime.now())
        y.append(len(scapy.all.arping("             ")[0]))
        plt.plot(x, y)
        plt.show()
        time.sleep(1)

#function to periodically scan for devices on a network using nmap
#launch jupyter notebook in a browser
#and display the results on matplotlib
def periodically_scan_for_devices_on_network_using_nmap_launch_jupyter_notebook_in_browser_and_display_results_on_matplotlib():
    x = []
    y = []
    while True:
        x.append(datetime.now())
        y.append(len(nmap.PortScanner().scan("             ")[0]))
        plt.plot(x, y)
        plt.show()
        time.sleep(1)
        os.system("jupyter notebook")

#function to scrape webpages and display the results on matplotlib
#use scrapy
def scrape_webpages_and_display_results_on_matplotlib():
    x = []
    y = []
    while True:
        x.append(datetime.now())
        y.append(len(scrapy.Spider()))
        plt.plot(x, y)
        plt.show()
        time.sleep(1)




#function to find index using pandas
def find_index_using_pandas():
    df = pd.DataFrame({"A": [1, 2, 3, 4, 5], "B": [6, 7, 8, 9, 10]})
    df.set_index("A", inplace=True)
    return df.index.get_loc(3)

#function to retrieve dictionary using input key
#use pandas
def retrieve_dictionary_using_input_key():
    df = pd.DataFrame({"A": [1, 2, 3, 4, 5], "B": [6, 7, 8, 9, 10]})
    df.set_index("A", inplace=True)
    return df.to_dict()["B"][3]

#generate a class named SearchDB
#input key value, database name, table name
#read in mongodb database
#create a function to retrieve dictionary using input key
#create function to output dictionary to file named 'output.json'
#use pymongo
#include name == main
class SearchDB:
    def __init__(self, key, database_name, table_name):
        self.key = key
        self.database_name = database_name
        self.table_name = table_name
        self.client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.db = self.client[self.database_name]
        self.table = self.db[self.table_name]

    def retrieve_dictionary_using_input_key(self):
        return self.table.find_one({self.key: self.key})

    def output_dictionary_to_file(self):
        with open("output.json", "w") as file:
            file.write(json.dumps(self.retrieve_dictionary_using_input_key()))


if __name__ == "__main__":
    SearchDB(1, "test", "test").output_dictionary_to_file()


#generate a class named SearchDB
#input key value, database name, table name
#read in mongodb database
#create a function to retrieve dictionary using input key
#create function to output dictionary to file named 'output.json'
#use pymongo
#include name == main
#use asyncio
class SearchDB:
    def __init__(self, key, database_name, table_name):
        self.key = key
        self.database_name = database_name
        self.table_name = table_name
        self.client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.db = self.client[self.database_name]
        self.table = self.db[self.table_name]

    async def retrieve_dictionary_using_input_key(self):
        return self.table.find_one({self.key: self.key})

    async def output_dictionary_to_file(self):
        with open("output.json", "w") as file:
            file.write(json.dumps(await self.retrieve_dictionary_using_input_key()))

if __name__ == "__main__":
    Asyncio(SearchDB(1, "test", "test").output_dictionary_to_file())



#function to recrusively build dictionary from input data
def recursively_build_dictionary_from_input_data(data):
    if isinstance(data, dict):
        return {key: recursively_build_dictionary_from_input_data(value) for key, value in data.items()}
    elif isinstance(data, list):
        return [recursively_build_dictionary_from_input_data(value) for value in data]
    else:
        return data

#----------------------Data Structures----------------------#
#dictionary of dictionaries of country codes and their corresponding country
#and their corresponding phone number formats
phone_formats = {
    'AF': { 'country': 'Afghanistan', 'format': '(\d{4})-(\d{6})' },
    'AX': { 'country': 'Aland Islands', 'format': '(\d{4})-(\d{6})' },
    'AL': { 'country': 'Albania', 'format': '(\d{4})-(\d{6})' },
    'DZ': { 'country': 'Algeria', 'format': '(\d{4})-(\d{6})' },
    'AS': { 'country': 'American Samoa', 'format': '(\d{4})-(\d{6})' },
    'AD': { 'country': 'Andorra', 'format': '(\d{4})-(\d{6})' },
}
#dictionary of dictionaries of 2 letter ISO state codes
#with their capitals, their corresponding polygons
state_codes = {
    'AL': {
        'capital': 'Montgomery',
        'polygon': [
            [32.361538, -86.279118],
            [32.360258, -86.174011],
            [32.362489, -86.174011],
            [32.362489, -86.279118]
        ],
    },
    'AK': {
        'capital': 'Juneau',
        'polygon': [
            [58.301935, -134.419708],
            [58.301935, -134.419708],
            [58.301935, -134.419708],
            [58.301935, -134.419708]
        ],
    },
    'AZ': {
        'capital': 'Phoenix',
        'polygon': [
            [33.448457, -112.073844],
            [33.448457, -112.073844],
            [33.448457, -112.073844],
            [33.448457, -112.073844]
        ],
    },
}

#dictionary of dictionaries of 2 letter ISO state codes
#with their capitals, their corresponding polygons and a dictionary of the remaining cities
#ignore duplicate cities

state_codes = {
    'AL': {
        'capital': 'Montgomery',
        'polygon': [ [32.361538, -86.279118], [32.360258, -86.174011], [32.362489, -86.174011], [32.362489, -86.279118] ],
        'cities': { 'Birmingham': [33.520661, -86.80249], 'Mobile': [30.695365, -88.039891], 'Montgomery': [32.366805, -86.299969] }
    },
    'AK': {
        'capital': 'Juneau',
        'polygon': [ [58.301935, -134.419708], [58.301935, -134.419708], [58.301935, -134.419708], [58.301935, -134.419708] ],
        'cities': { 'Anchorage': [61.218056, -149.900278], 'Fairbanks': [64.837778, -147.716389], 'Juneau': [58.301935, -134.419708] }
    },
    'AZ': {
        'capital': 'Phoenix',
        'polygon': [ [33.448457, -112.073844], [33.448457, -112.073844], [33.448457, -112.073844], [33.448457, -112.073844] ],
        'cities': { 'Flagstaff': [35.198284, -111.651302], 'Phoenix': [33.448457, -112.073844], 'Tucson': [32.221743, -110.926479] }
    }
}


#dictionary of dictionaries of 2 letter ISO state codes
#with their capitals, their corresponding polygons and a dictionary of the remaining non-capital cities
#ignore duplicate cities

state_codes = {
    'AL': {
        'capital': 'Montgomery',
        'polygon': [ [32.361538, -86.279118], [32.360258, -86.174011], [32.362489, -86.174011], [32.362489, -86.279118] ],
        'cities': { 'Birmingham': [33.520661, -86.80249], 'Mobile': [30.695365, -88.039891] }
    },
    'AK': {
        'capital': 'Juneau',
        'polygon': [ [58.301935, -134.419708], [58.301935, -134.419708], [58.301935, -134.419708], [58.301935, -134.419708] ],
        'cities': { 'Anchorage': [61.218056, -149.900278], 'Fairbanks': [64.837778, -147.716389] }
    },
    'AZ': {
        'capital': 'Phoenix',
        'polygon': [ [33.448457, -112.073844], [33.448457, -112.073844], [33.448457, -112.073844], [33.448457, -112.073844] ],
        'cities': { 'Flagstaff': [35.198284, -111.651302], 'Tucson': [32.221743, -110.926479] }
    }
}

#function to generate a tree of randomized data
def generate_tree_of_randomized_data():
    #generate a tree of randomized data
    tree_of_randomized_data = {}
    #iterate over the keys in the state_codes dictionary
    for state_code in state_codes.keys():
        #initialize the dictionary for the state
        tree_of_randomized_data[state_code] = {}
        #iterate over the keys in the state_codes dictionary
        for key in state_codes[state_code].keys():
            #if the key is not the cities key
            if key != 'cities':
                #set the value for the key in the tree_of_randomized_data dictionary
                tree_of_randomized_data[state_code][key] = state_codes[state_code][key]
            #if the key is the cities key
            else:
                #initialize the cities dictionary
                tree_of_randomized_data[state_code][key] = {}
                #iterate over the keys in the cities dictionary
                for city in state_codes[state_code][key].keys():
                    #set the value for the key in the tree_of_randomized_data dictionary
                    tree_of_randomized_data[state_code][key][city] = state_codes[state_code][key][city]
    #return the tree of randomized data
    return tree_of_randomized_data





