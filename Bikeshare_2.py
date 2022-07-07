import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv', 'New York City': 'new_york_city.csv', 'washington': 'washington.csv'}


def get_filters():
    """Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter"""

    print('Hello! Let\"s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    cities = ('chicago', 'new york city', 'washington')
    while True:
        city = input('\nWould you like to see data for Chicago, New York City, or Washington?\n').lower()
        if city not in cities:
            print('\nInvalid, please try again.')
            continue
        else:
            break

    # get user input for month (all, january, february, ... , june)
    months = ('all', 'january', 'february', 'march', 'april', 'may', 'june')
    while True:
        month = input('\nWhich month: January, February, March, April, May, or June?\n').lower()
        if month not in months:
            print('Invalid, please try again.')
            continue
        else:
            break

    # Creating a list to store all the days including the 'all' option
    days = ('all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday')
    while True:
        day = input('\nWhich day: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?\n').lower()
        if day not in days:
            print('Invalid, please try again.')
            continue
        else:
            break

    print('-'*40)
    return city, month, day

    # Returning the city, month and day selections
    return city, month, day


# Function to load data from the .csv files
def load_data(city, month, day):
    """Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter

    Returns:
        df - Pandas DataFrame containing city data filtered by month and day"""

    # Load data for city
    df = pd.read_csv(CITY_DATA[city])


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating...\n')
    start_time = time.time()

    # display the most common month
    month = ["January", "February", "March", "April", "May", "June", "all", "aLL"]
    month = month[(df['month'].mode()[0])-1]
    print(f"Common start month: {month}")

    # display the most common day of week
    print(f"Common day of week: {df['day_of_week'].mode()[0]}")

    # display the most common start hour
    common_hour = df['hour'].mode()[0]

    print(f'\nMost common Start Hour: {common_hour}')

    print(f'\nThis took {(time.time() - start_time)} seconds.')
    print('_'*80)

# Function to calculate station related statistics


def station_stats(df):

    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print(f'The most common start station is: {common_start_station}')

    # display most commonly used end station
    common_end_station = df['End Station'].mode()[0]

    print(f'The most common end station is: {common_end_station}')

    # of start and end stations
    df['Start To End'] = df['Start Station'].str.cat(df['End Station'], sep=' to ')
    combo = df['Start To End'].mode()[0]

    print(f"\nThe most frequent combination of trips are from {combo}.")

    print(f"\nThis took {(time.time() - start_time)} seconds.")
    print('_'*80)

# Function for trip duration related statistics


def trip_duration_stats(df):

    print('\nCalculating...\n')
    start_time = time.time()

    # Uses sum method to calculate the total trip duration
    print(f"The Total Travel Time: {df['Trip Duration'].sum()}")

    # Calculating the average trip duration using mean method
    print(f"The Mean Travel Time: {df['Trip Duration'].mean()}")

# Function to calculate user statistics


def user_stats(df):

    print('\nCalculating...\n')
    start_time = time.time()

    # display counts of user types
    user_type = df['User Type'].value_counts()

    print(f"\nThe types of users by number are given below:\n\n{user_type}")

    # display counts of gender
    try:
        gender = df['Gender'].value_counts()
        print(f"\nThe types of users by gender are given below:\n\n{gender}")
    except (ValueError, Exception):
        print("\nNo Gender")

    # Display earliest, most recent, and most common year of birth
    try:
        earliest = int(df['Birth Year'].min())
        recent = int(df['Birth Year'].max())
        common_year = int(df['Birth Year'].mod()[0])
        print(f"\nThe earliest year of birth: {earliest}\n\nThe most recent year of birth: {recent}\n\nThe most common year of birth: {common_year}")
    except (ValueError, Exception):
        print("No birth year")

    print(f"\nThis took {(time.time() - start_time)} seconds.")
    print('_'*80)

def display_data(df):
    show_data = input('\nWould you like to see 5 rows of raw data? yes or no:\n').lower()
    if show_data != 'no':
        i = 0
        while i < df['Start Time'].count() and show_data != 'no':
            print(df.iloc[i:i + 5])
            i += 5
            more_data = input('\nWould you like to see 5 more rows of data? yes or no:\n').lower()
            if more_data != 'yes':
                break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input("\nWould you like to restart? Enter yes or no.\n")
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
