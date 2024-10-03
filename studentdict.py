student_info=[
{
    "name":"ABHI",
    "age":11,
    "class":"classII",
},
{
    "name":"RUHI",
    "age":12,
    "class":"classIII",
},
{
    "name":"Goli",
    "age":11,
    "class":"class10",
}
]

print(student_info[1]["name"])


for i,dictionary in enumerate(student_info):
    print(f"keys in dictionary {i + 1}: {dictionary.keys()} ")
    print(f"keys in dictionary {i + 1}: {dictionary.values()} ")


all_keys = set()
for dictionary in student_info:
    all_keys.update(dictionary.keys())
print("all unique keys:",all_keys)

