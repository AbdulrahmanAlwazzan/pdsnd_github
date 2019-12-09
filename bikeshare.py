import time
import pandas as pd
import numpy as np
import calendar as cl


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
    ok = True
    city = input("Would you like to see data for New york city, Chicago or Washington: ")

    while(ok):
        if city.lower() == 'new york city' or city.lower() == 'chicago' or city.lower() == 'washington':
            ok = False

        else:
            city = input("invaild input try again ")


    # TO DO: get user input for month (all, january, february, ... , june)
<<<<<<< HEAD
    month = input("Wich month you want to filter with: january , february , march , april ,may ,june or \'all'? ")

||||||| parent of 23377f4... refactor print statments
    month = input("Wich month you want: january , february , march , april ,may ,june or \'all'? ")
    
=======
    month = input("Wich month you want: january , february , march , april ,may ,june or \'all'? ")

>>>>>>> 23377f4... refactor print statments

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Witch day you want to filter with?: ")


    print('-'*40)
    return city.lower(), month.lower(), day.lower()


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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])


    df['month'] = df['Start Time'].dt.month

    df['day_of_week'] = df['Start Time'].dt.weekday_name

    df['hour'] = df['Start Time'].dt.hour

    if month != 'all':
                 months = ['january', 'february', 'march', 'april', 'may', 'june']
                 month = months.index(month) + 1
                 df= df[df['month']== month]
    if day !='all':
                 df=df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month

    print("The most common month is: " +cl.month_name[df['month'].mode()[0]])



    # TO DO: display the most common day of week
    print("The most common day of week is: "+df['day_of_week'].mode()[0])



    # TO DO: display the most common start hour
    print("The most common start hour is: {}".format(df['hour'].mode()[0]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("The most commnly used start station : "+df['Start Station'].mode()[0])


    # TO DO: display most commonly used end station
    print("The most commnly used end station : "+df['End Station'].mode()[0])



    # TO DO: display most frequent combination of start station and end station trip
    df['combine'] = df['Start Station'].str.cat(df[['End Station']],sep = " , ")
    print("The most frequent trip : "+df['combine'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("The total travel time : {}".format(df['Trip Duration'].sum()))


    # TO DO: display mean travel time
<<<<<<< HEAD
    print("The mean of travel time : "+str(df['Trip Duration'].mean()))

||||||| parent of 23377f4... refactor print statments
    print("The mean of travel time : "+str(df['Trip Duration'].mean()))
    
=======
    print("The mean of travel time : {}".format(df['Trip Duration'].mean()))

>>>>>>> 23377f4... refactor print statments


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print(df['User Type'].value_counts())


    # TO DO: Display counts of gender
    try:
        print(df['Gender'].value_counts())
    except:
        print("No data available")


    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        print("The earliest year of birth : {}".format(df['Birth Year'].min()))
        print("The most recent year of birth : {}".format(df['Birth Year'].max()))
        print("The most common year of birth : {}".format(df['Birth Year'].mode()[0]))
    except:
          print('No data available')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):

    raw_data = input("\nDo you want to see raw data? Enter yes or no. \n")
    n = 0
    if raw_data.lower() == 'yes':
        check = True

        while(check):
            if raw_data.lower() == 'yes':
                print(df.iloc[n:n+5,:9])
                n+=5
                raw_data = input("\nDo you want to see more 5 lines of raw data? Enter yes or no. \n")
            else:
                check = False

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
