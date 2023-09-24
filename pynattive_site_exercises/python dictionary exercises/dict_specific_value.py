# Exercise 3: Print the value of key ‘history’ from the below dict

sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}

'''
unpacking values
sample_dict['class']['student']['marks']['history']
'''

print(sampleDict['class']['student']['marks']['history'])
