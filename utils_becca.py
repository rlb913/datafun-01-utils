''' ITERATION 4

Module: Banning Analytics - Reusable Module for My Data Analytics Projects

This module provides a simple, reusable foundation for my analytics projects. 

Process:
In this fourth iteration, I introduce some basic statistics using Python.
    - min() is a built in function to find the smallest value passed in
    - max() is a built in function to find the largest value passed in
    - The statistics module offered methods to calculate mean and standard deviation.
'''

#####################################
# Import Modules at the Top
#####################################

# In Python, we can import modules to add extra tools and fuctions.
# Below, we're importing:
# - 'statistics': This gives us tools to calculate things like averages.

import statistics

#####################################
# Declare global variables
#####################################

# Boolean variable to indicate if the company has international clients
has_international_clients: bool = True

# Additional boolean variable to indicate if the company has a hybrid work schedule
has_hybrid_work_schedule: bool = True

# Integer variable for the number of years in operation
years_in_operation: int = 10

# Additional integer variable for the company size
company_size: int = 10000

# List of strings representing the skills offered by the company
skills_offered: list = ["Data Analytics", "Machine Learning", "Business Intelligence"]

# Additional list of strings representing the office locations
office_locations: list = ["New York", "Chicago", "Los Angeles"]

# List of floats representing individual clients satisfaction scores
client_satisfaction_scores: list = [4.8, 4.6, 4.9, 5.0, 4.7]

# Additional list of floats representing individual employee satisfaction scores
employee_satisfaction_scores: list = [3.9, 4.2, 4.8, 3.0, 4.4]

#####################################
# Calculate Basic Statistics
#   Do this BEFORE we declare the byline
#   so the values have been calculated
#   and are ready for use in the byline.
#####################################

# Calculate basic stats using built-in functions min(), max() and statistics module functions mean() and stdev().
min_client_score: float = min(client_satisfaction_scores)
max_client_score: float = max(client_satisfaction_scores)
mean_client_score: float = statistics.mean(client_satisfaction_scores)
stdev_client_score: float = statistics.stdev(client_satisfaction_scores)

min_employee_score: float = min(employee_satisfaction_scores)
max_employee_score: float = max(employee_satisfaction_scores)
mean_employee_score: float = statistics.mean(employee_satisfaction_scores)
stdev_employee_score: float = statistics.stdev(employee_satisfaction_scores)

#####################################
# Declare a global variable named byline.
# Make it a multiline f-string to show our information.
#####################################

byline: str = f"""
-------------------------------------------------------
Banning Analytics: Delivering Professional Insights
-------------------------------------------------------
Has International Clients:    {has_international_clients}
Has Hybrid Work Schedule:     {has_hybrid_work_schedule}
Years in Opperation:          {years_in_operation}
Company Size:                 {company_size}
Skills Offered:               {skills_offered}
Office Locations:             {office_locations}
Client Satisfaction Scores:   {client_satisfaction_scores}
Employee Satisfaction Scores: {employee_satisfaction_scores}
"""

#####################################
# Define the get_byline() function.
#####################################

def get_byline() -> str:
    '''Return a byline for my analytics projects.'''
    return byline

#####################################
# Define a main() function for this module.
#####################################

# The main function now calls get_byline() to retrieve the byline.

def main() -> None:
    '''Print the byline to the console when this function is called.'''
    print(get_byline())

#####################################
# Conditional Execution
#####################################

if __name__ == '__main__':
    main()
