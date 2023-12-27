import overpy
import csv

api = overpy.Overpass()

query = """
[out:json];
(
area["ISO3166-1"="PL"]->.searchArea;
  node["place"="city"]["population"](area.searchArea);
  node["place"="town"]["population"](area.searchArea);
  node["place"="village"]["population"](area.searchArea);
);
out body;
"""

result = api.query(query)


with open('data/poland_places.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(["ID", "name", "population", "latitude", "longitude"])  # Write the header


    for i, node in enumerate(result.nodes):
        name = node.tags.get('name', 'n/a')
        population = node.tags.get('population', 'n/a')
        lat, lon = node.lat, node.lon
        writer.writerow([i, name, population, lat, lon])
