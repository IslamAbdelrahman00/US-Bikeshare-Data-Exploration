import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
city1=""

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
        city = input("\n please enter the full name of one of the following cities:new york city, chicago or washington?\n")
        city=city.lower()
        if city not in ['chicago','new york city','washington']:
            print("sorry the name of the city doesn't match the options")
            continue 
        else : 
            break 
            
            
        


    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("\n please enter the name of the month from the following choics :January, February, March, April, May, June or type 'all' if you do not have any preference?\n")
        month=month.lower()
        if month not in ["january", "february", "march", "april", "may", "june", "all"]:
            print("sorry the name of the month doesn't match the options")
            continue 
        else : 
            break 


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("\n please enter thename of the day from the following options or enter all if you don't have a prefernce:Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or type 'all'\n")
        day=day.lower()
        if day not in ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "all"]:
            print("sorry the name of the day doesn't match the options")
            continue 
        else : 
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
    
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] =pd.to_datetime(df['Start Time']) 

    # extract month and day of week from Start Time to create new columns
    df['month'] =df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name



    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+1
    
        # filter by month to create the new dataframe
        df = df[df['month']==month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # convert the Start Time column to datetime
    df['Start Time'] =pd.to_datetime(df['Start Time']) 
     # Create new columns for month, weekday, hour
    df['month'] = df['Start Time'].dt.month
    df['weekday_name'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    # TO DO: display the most common month
    print("the most common month:",df['month'].value_counts().idxmax())


    # TO DO: display the most common day of week
    print("the most common day of week:",df['weekday_name'].value_counts().idxmax())


    # TO DO: display the most common start hour
    print("the most common start hour:",df['hour'].value_counts().idxmax())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("most commonly used start station",df['Start Station'].value_counts().idxmax())


    # TO DO: display most commonly used end station
    print("most commonly used end station",df['End Station'].value_counts().idxmax())


    # TO DO: display most frequent combination of start station and end station trip
    comman_comb=df.groupby(['Start Station','End Station'])
    pop_comman=comman_comb.size()
    pop_comman_mod=pop_comman.sort_values(ascending=False).head(1)
    print("most frequent combination of start station and end station trip is : ",pop_comman_mod )


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    # Convert seconds to readable time format
    def secs_to_readable_time(seconds):
        m, s = divmod(seconds,60)
        h, m = divmod(m,60)
        d, h = divmod(h,24)
        y, d = divmod(d,365)
        print('Years: {}, Days: {}, Hours: {}, Mins: {}, Secs:{}'.format(y,d,h,m,s))


    # TO DO: display total travel time
    total_travel_time=df['Trip Duration'].sum()
    print('Total Readable travel time:\n')
    secs_to_readable_time(total_travel_time)


    # TO DO: display mean travel time
    print("mean traverl time in seconds : ",df['Trip Duration'].mean())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("counts of user types",df['User Type'].value_counts())


    # TO DO: Display counts of gender
    try:
        
        print("counts of gender",df['Gender'].value_counts())


    # TO DO: Display earliest, most recent, and most common year of birth
        min_yb=df['Birth Year'].min()
        max_yb=df['Birth Year'].max()
        most_yb=df['Birth Year'].value_counts().idxmax()
        print("earliest year of birth:{}, most recent year of birth: {},most comman year of birth:{} . ".format(min_yb,max_yb,most_yb))
    except :
        print("")
      


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)  
def display_data(df):
    """Displays rows on data from the datat frame."""
    commands=['yes','no', 'exit']
    start_loc = 0
    view_data = None
    while(view_data!='exit'):
        view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n').lower()
        if view_data in commands : 
            while (view_data=='yes'):
                print(df.iloc[start_loc:start_loc+5])
                start_loc += 5
                display_further = input("Do you wish to continue?: yes or no\n").lower()
                if display_further=='no' :
                    view_data='exit'
            view_data='exit'                              
        else :
            print ('i did not get that try again')
                             
                            
                             
                             
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
