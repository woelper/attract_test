import configparser


# all this should not be global later, but in a class

#Default values - Recommend changing values in the INI file, not here.
options = {
    "mrapath":"/media/fat/_Arcade/",
    "mrapathvert":"/media/fat/_Arcade/_Organized/_6 Rotation/_Vertical CW 90 Deg/",
    "mrapathhoriz":"/media/fat/_Arcade/_Organized/_6 Rotation/_Horizontal/",
    #declare -a mraexclude
    "timer":120,
    "orientation":"All",
    "mralist":"/media/fat/Scripts/Attract_Arcade.txt",
    "debugmain":False,
    "debugfunc":False,
    "tracemain":False,
    "tracefunc":False,
    "traceparse_ini":False,
    "tracebuild_mralist":False,
    "tracenext_core":False,

}

def parse_ini():
    # if you use a standard format like INI, you can use
    # a standard library to parse it!
    config = configparser.ConfigParser()
    config.read('Attract_Arcade.ini')
    # now you can access variables like this...
    print(config["DEFAULT"]["mrapath"])
    
    # or do something with all of them:
    for entry in config["DEFAULT"]:
        print(entry, config["DEFAULT"][entry])
        # or update our config:
        options[entry] = config["DEFAULT"][entry]

# Even simpler:
def parse_ini_simple():
    config = configparser.ConfigParser()
    config.read('Attract_Arcade.ini')
    options.update(config["DEFAULT"]) #since both are dicts...


def build_mralist():
    with open(options.mralist, "rw") as mrafile:
        for root, subdirs, files in os.walk(options.mrapath):
            # if not exclude in...
            mrafile.write()



def main():
    parse_ini_simple()
    print(options)

main()