import time
import pandas as pd
import numpy as np
from helper import Helper

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

data_output=dict()

months=['all','jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov','dec']
week_days = ['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']


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
    
    dataenteredIsCorrect=False
    while dataenteredIsCorrect==False:
        city= input("Please type city name (chicago, new york city, washington): ")
        dataenteredIsCorrect= Helper.check_user_input(city,list(CITY_DATA.keys()))
        print(dataenteredIsCorrect)
        if dataenteredIsCorrect:
            break
        else:
            continue
    dataenteredIsCorrect=False
    # TO DO: get user input for month (all, jan, feb, ... dec)
    while dataenteredIsCorrect==False:
        month= input("Please type month  [All,'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov','Dec'] : ")
        dataenteredIsCorrect= Helper.check_user_input(month,months)
        if dataenteredIsCorrect:
            break
        else:
            continue
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    dataenteredIsCorrect=False
    while dataenteredIsCorrect==False:
        day = input("Please type day [All,'Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']: ")
        dataenteredIsCorrect= Helper.check_user_input(day,week_days)
        if dataenteredIsCorrect:
            break
        else:
            continue

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
    
    try:
        df= pd.read_csv(CITY_DATA[city])
        # convert the Start Time column to datetime
        df['Start Time'] = pd.to_datetime(df['Start Time'])
        # extract hour from start date
        df['hour'] = df['Start Time'].dt.hour
        # extract month and day of week from Start Time to create new columns
        df['month'] = df['Start Time'].dt.month
        df['day_of_week'] = df['Start Time'].dt.weekday_name
        
        if month.lower() != 'all':
            # use the index of the months list to get the corresponding int

            month = months.index(month)

            # filter by month to create the new dataframe
            df = df[df['month']==month]

        # filter by day of week if applicable
        if day != 'all':
            # filter by day of week to create the new dataframe
            df = df[df['day_of_week']==day.title()]

        '''
        Run this part of code to data understanding
        df.head()
        df.columns
        df.describe()
        df.shape()
        '''

        return df
    except Exception as e:
        print("Error occured while loading data")

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    data_output['common month']=common_month
    print("The most common month is {}".format(common_month))
    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    data_output['common day']=common_day
    print("The most common day is {}".format(common_day))


    # TO DO: display the most common start hour
    common_hour = df['hour'].mode()[0]
    data_output['common hour']=common_hour
    print("The most common hour is {}".format(common_hour))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    #Check if the column exists in file
    if 'Start Station' in df.columns:
        start_station = df['Start Station'].mode()[0]
        data_output['common start_station']=start_station
        print("most commonly used start station is {}".format(start_station))
    
    # TO DO: display most commonly used end station
    if 'End Station' in df.columns:
        end_station = df['End Station'].mode()[0]
        data_output['common end_station']=end_station
        print("most commonly used end station is {}".format(end_station))

    # TO DO: display most frequent combination of start station and end station trip
    #start_and_end_st = df[['Start Station','End Station']].value_counts()
    
    '''
    Analyze data
    type(start_and_end_st)
    print(start_and_end_st[[0,0]]);
    
    '''
    if 'Start Station' in df.columns and 'End Station' in df.columns:
        start_and_end_st =(df['Start Station'] + ' and ' + df['End Station']).mode()[0]
        data_output['common start_and_end_station']=start_and_end_st
        print('Most frequesnt start and end stations are {}'.format(start_and_end_st))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    
    if 'Trip Duration' in df.columns:
        # TO DO: display total travel time
        total_travel_time = df['Trip Duration'].sum().sum()
        data_output['total_travel_time']=total_travel_time    
        print("The total travel time is {}.".format(Helper.convertSeconds(total_travel_time)))
    
        # TO DO: display mean travel time
        mean_travel_time = df['Trip Duration'].mean()
        data_output['mean_travel_time']=mean_travel_time
        print("The mean travel time is {}.".format(Helper.convertSeconds(mean_travel_time)))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    if 'User Type' in df.columns:
        user_types_dict=dict()
        print("Number of users per user type is")
        user_types =df['User Type'].value_counts()
        for index, value in user_types.items():
            user_types_dict[index]=value
            print(f"User Type : {index}, Count : {value} users")
        data_output["User Types"]=user_types_dict

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender_dict=dict()
        print("Number of users per gender is")
        user_types =df['Gender'].value_counts()
        for index, value in user_types.items():
            gender_dict[index]=value
            print(f"{index} : {value}")
        data_output["Gender"]=gender_dict


    # TO DO: Display earliest, most recent, and most common year of birth
    
    '''
    Clean Data:
        drop the NA values to calculate the correct mean.
    
    '''
    if 'Birth Year' in df.columns:
        year_of_birth =df['Birth Year'].dropna()
        earliest_yofb =int(year_of_birth.unique().min())
        data_output['Earliest year of birth']=earliest_yofb
        print("Earliest year of birth is {}".format(earliest_yofb))
        most_recent_yofb=int(year_of_birth.unique().max())
        data_output['most recent year of birth']=most_recent_yofb
        print("Earliest year of birth is {}".format(most_recent_yofb))
        comon_yofb=int(year_of_birth.mode())
        data_output['comon year of birth']=comon_yofb
        print("Common year of birth is {}".format(comon_yofb))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    '''
    Display the data to the user in pages of 5
    '''
    #Reset the index of the data
    df= df.reset_index()
    counter=0
    view_data =input("Do you want to view the data, press y : ")
    while(view_data.lower()=='y'):
        print(df.iloc[counter:counter+5, :])
        counter+=5
        view_data =input("Do you want to view more data, press y : ")
        
def display_output():
    '''
    Display the output as dictionary of data.
    '''
    answer =input("Press y if you'd like to see all output as dictionary: ")
    if(answer.lower() == 'y'):
        print(data_output)
        
def main():
    
    while True:
        
        city, month, day = get_filters()
        df = load_data(city, month, day)
        if df.shape[0]==0:
            "There is no data for the filters you choose, please choose another filters"
            continue        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_output()
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
