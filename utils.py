import json
import pandas as pd
import matplotlib.pyplot as plt
import datetime 
import calendar 
'''
pre: json files exist
post: converts json files into pandas DataFrames
'''
def load_data(jsonfile):
    data = pd.read_json(jsonfile)
    return data

'''
pre: DataFrame exists
post: cleans data by replacing '$' with 'S', replacing my local files with Playboi Carti as the artist, and labeling podcasts as such
'''
def clean_spot_df(df):
    ser = df["artistName"].copy()
    for i in range(0, len(ser), 1):
        curr = str(ser[i])
        if "$" in curr:
            curr = curr.replace("$", "S")
            ser[i] = curr
        if "Unknown Artist" in curr:
            ser[i] = "Playboi Carti"
        if "The Official Podcast" in curr or "Who Are These Podcasts" in curr or "Podcast Reviews and First Impressions" in curr:
            ser[i] = "podcast"       
    df["artistName"] = ser
    
'''
pre: DataFrame['artistName'] has been outfitted to label podcasts as such
post: podcasts are removed from the DataFrame
'''
def rm_pod(df):
    ser = df["artistName"].copy()
    for i in range(0, len(ser), 1):
        if ser[i] == "podcast":
            df.drop(i, inplace=True)
            
'''
pre: data for bar chart has been compiled
post: bar chart is exported to Figures
'''
def artist_bar_chart(data, filename, title):
    plt.ioff()
    plt.figure(figsize=(15, 10))
    x_ser = data['Artist']
    y_ser = data['Hours Listened']
    i = 0
    for item in x_ser:
        plt.bar(item, y_ser[i], color='r')
        i+=1
    plt.title(title)
    plt.xticks(rotation=45, horizontalalignment='right')
    plt.xlabel("Artists")
    plt.ylabel("Hours Listened")
    plt.savefig("Figures/Artists x Hours Listened (Bar Graphs)/"+filename)
    if filename == "1-10":
        plt.show()
    plt.close()
    
'''
pre: data is collected for unique artists, hours per unique artist in organized lists
post: new DataFrame is created
'''
def create_artist_x_hours_df(artist_perArtist, totalHours_perArtist):
    artist_x_hours_df = pd.DataFrame()
    artist_x_hours_df['Artist'] = artist_perArtist
    artist_x_hours_df['Hours Listened'] = totalHours_perArtist
    artist_x_hours_df = artist_x_hours_df.sort_values(by=['Hours Listened'], ascending=False)
    artist_x_hours_df = artist_x_hours_df.reset_index()
    del artist_x_hours_df['index']
    return artist_x_hours_df

'''
pre: date is in form day-month-year
post: returns a day of the week
'''
def findDay(date):
    born = datetime.datetime.strptime(date, '%d %m %Y').weekday() 
    return (calendar.day_name[born])
    #function found at https://www.geeksforgeeks.org/python-program-to-find-day-of-the-week-for-a-given-date/

'''
pre: DataFrame['endTime'] exists
post: returns a list of raw dates in the form day-month-year
'''
def get_date_list(df):
    raw_dates = []
    ser = df["endTime"].copy()
    for i in range(0, len(ser), 1):
        curr = str(ser[i])
        year = curr[0:4]
        day = curr[8:10]
        month = curr[5:7]
        newEntry = day + " " + month + " " + year
        raw_dates.append(newEntry)
    return raw_dates