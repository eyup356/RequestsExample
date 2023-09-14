import requests


get_url= "https://jsonplaceholder.typicode.com/todos/11"

#get_response = requests.get(get_url)

#print(get_response.json())


#PUT

to_do_item_11= {"userId": 1, "title": "put title", "completed": False}

#put_response= requests.put(get_url, json=to_do_item_11)
#print(put_response.json())

#Patch
to_do_item_patch_11= {"title": "Patch xd"}
#patch_response = requests.patch(get_url, json=to_do_item_patch_11)
#print(patch_response.json())

#Delete
delete_response = requests.delete(get_url)
print(delete_response.json())
print(delete_response.status_code)