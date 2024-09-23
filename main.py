import requests

while True:
    response = input("continue? type 'y' to continue else enter any key : ")

    if response.lower() == 'y':

        class Test:

            def __init__(self):
                pass

            def identity(self):
                id = input("Enter your name: ")
                data = requests.get(f"https://api.nationalize.io/?name={id}")
                data1 = data.json()

                for each in data1["country"]:
                    print(f"Country: {each['country_id']} | Probability: {each['probability']} \n")

                    with open("national.txt", "a") as n:
                        n.write(
                            f"Name: {id} \n Country: {each['country_id']} | Probability: {each['probability']}\n ------- \n ")

                with open("national.txt", "a") as n:
                    n.write("\n \n")


        obj = Test()
        obj.identity()

    else:
        break