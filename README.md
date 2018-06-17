# Uvec-Programming-Challenge-Summer-2018
Max and I entered the programming challenge and won it. On June 9,2018 University of Victoria (Uvic) Engineering held the Uvec competition. Winners from each category get to represent Uvic at the Western Engineering Conference (WEC). The challenge was to create a scheduling system for the labs, assignments, midterms, and finals for a school semester (see ProgrammingChallengeOutline.pdf for more) in a time frame of 5 hours.

# Overview of solution
The main goal we set for ourselves was to create a working product in the 5 hours allotted. Python was chosen due to its speed of development. The program parses the input file into an array, creates a schedule by attempting to space each school work item as far apart as possible, and prints that schedule to a CSV file (googleCalendar.csv) that can be imported into Google calendar (see UploadedToGoogleCalendar.png). Writeup.txt attempts to document our planning process. The further on into the competition we got the less documentation was done because we really wanted a working product. The product did work on all but two design criteria. Many values were hard coded but could easily be turned into variables to accommodate different school semesters. course.py is in the exact same state that was submitted for the challenge and presented to the judging panel.

