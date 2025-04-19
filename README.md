# Monitor_Tracker

## Table of Contents
1. [Description](#description)
2. [CSV Formats](#csv-formats)
    - [monitors.csv](#monitorscsv)
    - [students.csv](#studentscsv)
3. [Usage](#usage)
4. [Testing](#testing)
5. [Acknowledgements and Contacts](#acknowledgements-and-contacts)



## Description


This project manages weekly student bookings of computer monitors, following specific rules:

* Students can book monitors once before 10:00 AM per week.

* A week is specified as starting on a Monday and ends on a Friday at 18:00, once the week "ends" time sets to a new weeks Monday.

* After 10:00 AM, students can book a monitor multiple times in a week.

* If a monitor does not have an HDMI Cable, it can be booked once for the entire week (by any one student).

## CSV Formats

### `monitors.csv`

A CSV is used to store the data needed for the program, for monitors information, data is stored using these indicators -Serial Number,Number on Monitor,Brand,Has HDMI,Has Power Cable.

### `students.csv`

Lists all present students that are able to book monitors, student information is stores as follows, Student ID,Name,Surname,Email.


## Usage

## Testing

## Acknowledgements and Contacts

**Author**: Nomawonga Chinna Qwele

**Acknowledgements**: Special thanks to the contributors of the libraries used in this project.
Special Thanks to my training institution who introduced this problem that allowed me to solve it trough code.

For any issues or questions, feel free to contact the me at nomaradebe41@gmail.com or submit an issue on the project’s GitHub repository.
