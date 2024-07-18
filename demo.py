import randomdata
import json

languages = ["English", "German", "Spanish"]

data = {
    "string": randomdata.String(10), # generate random string of size 10
    "string_number": randomdata.StringNumber(12), # generate random string/number of size 12
    "number": randomdata.Number(5), # generate random number of size 10
    "version": randomdata.Version(), # generate random version without .0
    "version_dotzero": randomdata.Version(True), # generate random version with .0
    "datetime": randomdata.DateTime(2000), # generate random datetime between year 2000 and now
    "language": randomdata.EntryOfArray(languages) # get random value from array
}

print(json.dumps(data, indent=4))