#Challenge 37
countryPop = {"japan":127000000, "germany":81000000, "iran":7700000, "uk":64000000, "canada":33000000, "australia":23000000, "usa":317000000, "bulgaria":7000000, "sweden":1000000}
#List of countries and their Population
print("Enter a country from the list\nJapan, Germany, Iran, UK, Canada, Australia, USA, Bulgaria, Sweden.")
#Tells user the list of countries
while True:
    fCountry = input("Enter a country: ")
    fCountry = fCountry.lower()
    sCountry = input("Enter another country: ")
    sCountry = sCountry.lower()
    if fCountry in countryPop and sCountry in countryPop:
        break
    print("Do it again")
#User inputs two of them correctly and has capitalisation match
totalPop = countryPop[fCountry] + countryPop[sCountry]
print(f"The total pop is {totalPop}")
#Population is added and printed