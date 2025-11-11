import requests as rq

response = rq.get("https://jsonplaceholder.typicode.com/users")

if response.status_code == 200:
    data = response.json()

    for usuario in data:
        print(f"Nombre: {usuario['name']}")
        print(f"Email: {usuario['email']}")
        print("-" * 40)
else:
    print(f"Error: {response.status_code}")