# this will define a list of dogs in the shelter
dogs_in_shelter = [
    {"name": "nube", "age": 2, "breed": "poodle mix", "medical_records": {"vaccination": "up to date"}, "behavior_assessments": {"temperament": "friendly"}, "available": True},
    {"name": "star", "age": 5, "breed": "labrador golden retreiver mix", "medical_records": {"vaccination": "up to date"}, "behavior_assessments": {"temperament": "shy"}, "available": True}
]
# this will collect the users preferences
user_preferences = {"age": "young", "breed": "poodle mix"}

# this will define a function to calculate a match score
def calculate_match_score(dog, preferences):
    match_score = 0
    if dog["age"] <= 3:  
        match_score += 1
    if dog["breed"] == preferences["breed"]:  
        match_score += 1
    return match_score

# this will find matches or a match based on the users preferences
matches = []
for dog in dogs_in_shelter:
    if dog["available"]:
        match_score = calculate_match_score(dog, user_preferences)
        matches.append((dog, match_score))

# this will sort matches depending on their scores
matches.sort(key=lambda x: x[1], reverse=True)

# this will show top matches
print("Top Matches:")
for i, match in enumerate(matches[:5]):
    print(f"{i+1}. {match[0]['name']} - Match Score: {match[1]}")

# this will display users interest in the dog
interested_dog = matches[0][0]
print(f"\nUser is interested in adopting {interested_dog['name']}!")

# this will update dog's adoption status
interested_dog["available"] = False
print(f"{interested_dog['name']} is no longer available for adoption.")

# when it comes to post adoption support, it will not be implemented here due to the fact this code is just a simple/simplified version of the over all possible one.
