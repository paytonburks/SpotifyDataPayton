Place your JSON streaming history into the "StreamingHistoryJsonFiles" in order to load into seperate dataframes. The data will be concatenated into one dataframe "spot_df" to be analyzed. It will then be cleaned and have the days of the week for each datapoint be appended to the data and finally sent to a csvfile, "spotifydata.csv".

We then will find the amount of unique artists listened to and list them for the reader.

Next, we convert the total amount of milliseconds listened to the total amount of hours listened while simultaneously storing the data needed for hours listened per each artist.

Using said data, we can plot the top 100 artists with the most listening activity on seperate bar charts.