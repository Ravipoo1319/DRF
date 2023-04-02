"""
Sometimes, we don't know in advance that how many number of arguments that we wil be passed to the function.
"""

def display_details(**kwargs):
    print("Details :", kwargs)
    
    
display_details(first_name="Ravindra",last_name="Pawar")