import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
   # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Enter a city: ").lower()
        if city.lower() not in ('chicago','new york city','washington'):
            print("Sorry, that's not a valid city. Please try again.")
        else:
            break
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("Enter a month: ").lower()
        if month.lower() not in ('all','january','february','march','april','may','june'):
            print("Sorry, that's not a valid month. Please try again.")
        else:
            break
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Enter a day of the week: ").lower()
        if day.lower() not in ('all','monday','tuesday','wednesday','thursday','friday','saturday','sunday'):
            print("Sorry, that's not a valid day of the week. Please try again.")
        else:
            break
    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # Used to load data into data frame
    df = pd.read_csv(CITY_DATA[city])

    # Converts Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # This extracts the month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # Used to filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # Creates new dataframe when filtering by month
        df = df[df['month'] == month]

    # Used to filters by day of week if applicable
    if day != 'all':
        # Creates new dataframe when filtering by day of week
        df = df[df['day_of_week'] == day.title()]
    return df
    ### Note: Much of this was taken directly from Practice Problem #3's code solution.

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    month_mode = df['Start Time'].dt.month.mode()[0]
    print("Most common month: "+months[month_mode - 1].title())

    # TO DO: display the most common day of week
    day_of_week_mode = df['Start Time'].dt.weekday_name.mode()[0]
    print("Most common day of the week: "+day_of_week_mode)

    # TO DO: display the most common start hour
    hour_mode = df['Start Time'].dt.hour.mode()[0]
    if hour_mode > 12:
        standard_time = hour_mode - 12
    elif hour_mode < 12 and hour_mode > 0:
        standard_time = hour_mode
    elif hour_mode == 0:
        standard_time == 12
    else:
        standard_time = 99
     #If and elif are used to convert 24 hour clock to 12 hour clock in standard_time_variable
    if hour_mode >= 12:
        am_pm = "PM"
    elif hour_mode < 12:
        am_pm = "AM"
    else:
        am_pm = " - Error: Invalid hour. Can't derive AM vs. PM"
    #If and elif used to populate the am_pm variable representing morning vs. evening
    print("Most common hour: "+str(standard_time)+" "+am_pm)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station_mode = df['Start Station'].mode()[0]
    print("Most Common Start Station: "+start_station_mode)

    # TO DO: display most commonly used end station
    end_station_mode = df['End Station'].mode()[0]
    print("Most Common End Station: "+end_station_mode)

    # TO DO: display most frequent combination of start station and end station trip
    station_combination = df['Start Station']+" to "+df['End Station']
    station_combination_mode = station_combination.mode()[0]
    print("Most Frequent Combination of Start/End Station: "+station_combination_mode)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    travel_times = pd.to_datetime(df['End Time']) - pd.to_datetime(df['Start Time'])
    total_travel_time = str(travel_times.sum()).split(':')
    print("Total Travel Time: {} hours(s) {} minutes(s) and {} second(s)".format(total_travel_time[0],total_travel_time[1],total_travel_time[2]))

    # TO DO: display mean travel time
    mean_travel_time = str(travel_times.mean()).split(':')
    print("Mean Travel Time: {} hour(s) {} minute(s) and {} second(s)".format(mean_travel_time[0],mean_travel_time[1],mean_travel_time[2]))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type_count = pd.DataFrame(df['User Type'].value_counts())
    print("Counts of user types: ")
    print(user_type_count)
    print("\n")

    # TO DO: Display counts of gender
    if 'Gender' in list(df):
        gender_count = pd.DataFrame(df['Gender'].dropna(axis = 0).value_counts())
        print("Counts of gender: ")
        print(gender_count)
    else:
        print("No gender data is available for this city.")
    ## Used if and else statements for gender statistics so calculations only execute when the the Gender column is in the dataframe.
    ## Washington does not have gender data.
    ## Source for list(df): https://stackoverflow.com/questions/19482970/get-list-from-pandas-dataframe-column-headers
    print("\n")

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in list(df):
        birth_year = df['Birth Year'].dropna(axis = 0)

        earliest_yob = int(birth_year.min())
        most_recent_yob = int(birth_year.max())
        most_common_yob = int(birth_year.mode())

        print("Earliest Year of Birth: "+str(earliest_yob))
        print("Most Recent Year of Birth: "+str(most_recent_yob))
        print("Most Common Year of Birth: "+str(most_common_yob))
    else:
        print("No year of birth data is available for this city.")
    ## Used if and else statements for year of birth statistics so calculations only execute when the Birth Year column is in the dataframe.
    ## Washington does not have year of birth data.
    ## Source for list(df): https://stackoverflow.com/questions/19482970/get-list-from-pandas-dataframe-column-headers
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def view_data(df):
    print('\nGathering raw data...\n')
    start_time = time.time()
    starting_row = 5
    while True:
        view_data = input("Would you like to view five rows of data? Enter yes or no. ").lower()
        if view_data.lower() == 'yes':
            print("\n")
            print(df.head(starting_row))
            #Used following source for head method: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.head.html
            starting_row = starting_row + 5
            print("\n")
        else:
            break
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():

    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        view_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
