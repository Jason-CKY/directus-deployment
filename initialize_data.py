import requests
import csv

web_url = 'http://localhost:8055'

def create_collection():
    resp = requests.post(f"{web_url}/collections?access_token=admin", 
                    json={
                        "collection": "iris",
                        "fields": [
                            {
                                "field": "id",
                                "type": "integer",
                                "schema": {
                                    "has_auto_increment": True,
                                    "is_primary_key": True
                                },
                                "meta": {}
                            },
                            {
                                "field": "SepalLengthCm",
                                "type": "float",
                                "meta": {}
                            },
                            {
                                "field": "SepalWidthCm",
                                "type": "float",
                                "meta": {}
                            },
                            {
                                "field": "PetalLengthCm",
                                "type": "float",
                                "meta": {}
                            },
                            {
                                "field": "PetalWidthCm",
                                "type": "float",
                                "meta": {}
                            },
                            {
                                "field": "Species",
                                "type": "string",
                                "meta": {}
                            },
                        ]
                    })

    print(resp.text)

def main():
    create_collection()
    with open("Iris.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            del row["Id"]
            print(row)

            requests.post(f"{web_url}/items/iris?access_token=admin", json=row)

if __name__ == '__main__':
    main()