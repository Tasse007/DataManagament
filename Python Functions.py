########################### IMPORTS ############################




#the libraries are important later
import pandas as pd
import json
from random import seed
from random import randint
from random import random




########################### 1. DATA ###########################




#movies_df needs to be outside load_movies_data function so other functions can also call the variable ("global variable")
movies_df = None

#create the load movies data function F1.1
def load_movies_data():

    #this function should refer to the global variable
    global movies_df

    #read movies csv-file
    movies_df = pd.read_csv('movies.csv')

    #display movies
    #"(F1.1 load_movies_data)" stands for the first chapter's first function and for its name. It should help the reader finding the matching results of the specific function in the output box.
    print("\n(F1.1 load_movies_data) Here are all available movies:\n")
    print(movies_df[["name","genre","rate","likes","shares","views"]])




users_df = None

#create users data function F1.2
def load_users_data():

    #this function should refer to the global variable
    global users_df

    #read users csv-file
    users_df = pd.read_csv('users.csv')

    #display users
    print("\n(F1.2 load_users_data) Here are all registered users:\n")
    print(users_df)




#Some movies have no data yet! In this section the system starts producing data.
#Therefore, some basic functions for liking (F1.3), sharing (F1.4) and rating (F1.5) movies need to be on the top (due to the high number of simulations, the print-functions got commented out during the data-creation for a better readability.):

def like_a_movie_without_printing(movie_id, user_id):

  #get the user's data
  user = users_df[users_df["_id"]==user_id]

  #get the movie's data 
  movie_user_watched = movies_df[movies_df["_id"] ==movie_id]

  #commented out for data-creation:
  #print("(F1.3 like_a_movie_without_printing(movie_id, user_id)) " +user["name"].values.item() +" gives "+movie_user_watched["name"].values.item() + " a like.")

  #get the likes which the movie already has
  likes = movie_user_watched["likes"]

  #increment the amount of likes by one
  likes = likes +1

  #upload the new amount of likes in the movies_df
  movies_df.at[movie_id,'likes']=likes

  #update the last movie of the user
  users_df.iloc[user_id, users_df.columns.get_loc('_id_last_movie')] = movie_id

  #get the updated movie data and print it out
  movie_user_watched = movies_df[movies_df["_id"] ==movie_id]

  #commented out for data-creation:
  #print("\n(F1.3 like_a_movie_without_printing(movie_id, user_id)) These are the updated data: \n")
  #print(movie_user_watched[["name","rate","likes","shares","views"]])
  #print()
  #print(users_df[["name","_id_last_movie"]])





def share_a_movie_without_printing(movie_id):

  #get the movie's data 
  movie_user_watched = movies_df[movies_df["_id"] ==movie_id]

  #get the shares which the movie already has
  shares = movie_user_watched["shares"]
  
  #increment the amount of shares by one
  shares = shares +1
  
  #update the movies_df
  movies_df.at[movie_id,'shares']=shares

  #get the updated movie data and print them out
  movie_user_watched = movies_df[movies_df["_id"] ==movie_id]

  #commented out for data-creation:
  #print out the result
  #print("\n(F1.4 share_a_movie_without_printing(movie_id, user_id)) These are the updated data: \n")
  #print(movie_user_watched[["name","rate","likes","shares","views"]])





def rate_a_movie_without_printing(movie_id, rating):

  global movies_df

  #get the movie's data 
  movie_user_watched = movies_df[movies_df["_id"] ==movie_id]

  #commented out for data-creation:
  #print()
  #print("(F1.5 rate_a_movie_without_printing(movie_id, rating))) Someone gives "+movie_user_watched["name"].values.item() + " a rating of " + str(rating) +".")

  #commented out for data-creation:
  #print("\n(F1.5 rate_a_movie_without_printing(movie_id, rating)) This is the movies current status:\n")
  #print(movie_user_watched[["name", "rate", "number_of_people_rated"]])
  
  #get the rate of this movie
  rate = movie_user_watched["rate"]
  raters = movie_user_watched["number_of_people_rated"]

  #increment the amount of raters by one and update the amount of raters in the movie_df
  raters = raters +1
  movies_df.at[movie_id,'number_of_people_rated']=raters

  #calculate the new rating average and update it in movies_df
  sum = (raters-1)*rate
  sum = sum +rating
  new_rate= sum / raters

  movies_df.at[movie_id,'rate']=new_rate
   
  #commented out for data-creation:
  #for index, row in movies_df[movies_df["_id"] ==movie_id].iterrows():
    #print("\n(F1.5 rate_a_movie_without_printing(movie_id, rating)) This is the movies new status:\n")
    #print("name, rate, number_of_people_rated")
    #print(row["name"], row["rate"], row["number_of_people_rated"])
  
  #print(movies_df[["name", "rate", "number_of_people_rated"]])




#the following function F1.6 updates movies and users when a movie has been watched
def watch_a_movie_without_printing(movie_id, user_id, time_period, likes, rating, shares):

  
  #get the movie's data 
  movie_user_watched = movies_df[movies_df["_id"] ==movie_id]

  #get the user's data
  user = users_df[users_df["_id"]==user_id]
  
  #commented out for data-creation:
  #print("(F1.6 watch_a_movie_without_printing(movie_id, user_id, time_period, likes, rating, shares)) The user "+user["name"].values.item() +" " +time_period+" the movie  " + movie_user_watched["name"].values.item()+ " and gives it a rating of " +str(rating) +".")


  #if the like_parameter in the function call equals zero, then the movie does not get a like
  if likes != 0:
    like_a_movie_without_printing(movie_id, user_id)


  #if the share_parameter in the function call equals zero, then the movie does not get a share
  if shares != 0:
    #the following code is possible, but calling the function "share_a_movie" is shorter and faster
    #get shares movie already has
    #shares = movie_user_watched["shares"]
    #increment shares by one
    #shares = shares +1
    #movies_df.at[movie_id,'shares']=shares
    share_a_movie_without_printing(movie_id)

  #update the movie rating
  rate_a_movie_without_printing(movie_id, rating)

  #update the views
  #get the amount of views the movie already has
  views = movie_user_watched["views"]

  #increment the views by one
  views = views +1

  #update the amount of views in the movies_df
  movies_df.at[movie_id,'views']=views

  #increment the views depending on the time the movie has been watched
  #these data can be cruical for further decisions of the recommendation system
  if time_period.lower() == "viewed_today":
    views = movie_user_watched["views_today"]
    views = views +1
    movies_df.at[movie_id,"views_today"]=views
  elif time_period.lower() == "viewed_in_last_week":
    views = movie_user_watched["views_in_last_week"]
    views = views +1
    movies_df.at[movie_id,'views_in_last_week']=views
  elif time_period.lower() == "viewed_in_last_month":
    views = movie_user_watched["views_in_last_month"]
    views = views +1
    movies_df.at[movie_id,'views_in_last_month']=views
  elif time_period.lower() == "viewed_in_last_year":
    views = movie_user_watched["views_in_last_year"]
    views = views +1
    movies_df.at[movie_id,'views_in_last_year']=views
  else:
    print("\n(F1.6 watch_a_movie(movie_id, user_id, time_period, likes, rating, shares)) Please choose viewed_today / viewed_in_last_week / viewed_in_last_month / viewed_in_last_year for choosing the time_period the movie was been watched in.\n")

  #get the updated movie data and print them out
  movie_user_watched = movies_df[movies_df["_id"] ==movie_id]
  
  #commented out for data-creation:
  #print("\n(F1.6 watch_a_movie_without_printing(movie_id, user_id, time_period, likes, rating, shares)) This is the updated data:\n")
  #print(movie_user_watched[["name","rate","likes","shares","views"]])
  #print(user[["name", "_id_last_movie"]]) 




#With this function 1.7 we can simulate other users watching movies
def simulate_other_users(numer_of_activities):
  
  #the shape function shows how many rows the movies_df has
  movies_in_system = movies_df.shape[0]

  #the headlines do not count as row and need to be substracted
  movies_in_system = movies_in_system -1

  #the shape function shows how many rows the users_df has
  users_in_system = users_df.shape[0]

  #the headlines do not count as row and need to be substracted
  users_in_system = users_in_system -1

  i=0
  while i<numer_of_activities:
    #for every simulation the watch_a_movie function gets called with random parameters
    movie_id = randint(0, movies_in_system)
    user_id = randint(0, users_in_system)
    time_period_determiner = randint(0, 3)

    if time_period_determiner ==0:
      time_period="viewed_today"
    elif time_period_determiner ==1:
      time_period="viewed_in_last_week"
    elif time_period_determiner ==2:
      time_period="viewed_in_last_month"
    elif time_period_determiner ==3:
      time_period="viewed_in_last_year"
    
    likes=randint(0, 1)
    rating=random()*10
    shares=randint(0,1)


    watch_a_movie_without_printing(movie_id, user_id, time_period, likes, rating, shares)
    i=i+1




###################### DATA FUNCTION CALLS #####################




load_movies_data()

load_users_data()

print("\n(F1.7 simulate_other_users(numer_of_activities)) How many simulations of users watching movies should be started (e.g. 250, this process may take a few seconds)?\n")
number_of_activities = int(input())
simulate_other_users(number_of_activities)
print("Here is the changed movies_df after the simulation:")
print(movies_df[["name","genre","rate","likes","shares","views"]])




########################## 2. SEARCH ###########################




#Function 2.1 get's a searched term which the user typed in and looks for this term in the name and synopsis from the movies in the movies_df
def recommend_by_searched_term(searched_term):


    searched_term = searched_term.lower()
    result_name = movies_df["name"].str.contains(pat=searched_term)
    result_synopsis = movies_df["synopsis"].str.contains(pat=searched_term)

    #the search results of movie name and movie synopsis get merged in the final_result
    final_result = pd.merge(movies_df[result_name], movies_df[result_synopsis], how='outer')
    print("\n(F2.1 recommend_by_searched_term(searched_term)) Here are all movies which contain the searched word "+searched_term+":\n")
    print(final_result[["name","genre","synopsis","rate","likes","shares","views"]])




#Function 2.2 counts how often the searched term is in the name and synopsis and builds a ranking. 
def basic_recommend_by_searched_term(searched_term):

    searched_term = searched_term.lower()
    result_name = movies_df["name"].str.contains(pat=searched_term)
    result_synopsis = movies_df["synopsis"].str.contains(pat=searched_term)
    final_result = pd.merge(movies_df[result_name], movies_df[result_synopsis], how='outer')
    #calling the recommend_by_searched_term(searched_term) would have been also possible

    i = 0
    #The "length" of final_result.shape[i] is the number of rows in final_result
    while (i < final_result.shape[0]):

        #The name gets divided in a list of single words
        separated_name = final_result["name"].iloc[i].split()

        #The synopsis gets divided in a list of single words
        separated_synopsis = final_result["synopsis"].iloc[i].split()

        #the id of the current row gets noted
        id = final_result["_id"].iloc[i]

        word_count = 0
        #The "length" of the movies separated name is the amount of words
        #Each word gets checked if it equals the searched_term
        x = 0
        while (x < len(separated_name)):

            if (separated_name[x] == searched_term):
                #The number of times the searched_term appears in the name gets saved in word_count
                word_count = word_count + 1
            x = x + 1

        #The "length" of the separated synopsis is the amount of words
        #Each word gets checked if it equals the searched_term
        y = 0
        while (y < len(separated_synopsis)):

            if (separated_synopsis[y] == searched_term):
                #The number of times the searched_term appears in the synopsis is saved
                word_count = word_count + 1
            y = y + 1

            #The word_gets written in the movies_df
            final_result.loc[final_result['_id'] == id, 'word_count'] = word_count

        i = i + 1

    #The movie with the highest word_count gets printed out
    max_word_df = final_result.loc[final_result['word_count'].idxmax()]
    print(
        "\n(F2.2 basic_recommend_by_searched_term(searched_term)) You should watch "
        + max_word_df["name"] + " because the searched_term " + searched_term +
        " appeard " + str(max_word_df["word_count"]) + " times:\n")
    print("\nHere you can find more information:\n")
    print(max_word_df[["name","genre","synopsis","rate","likes","shares","views"]])




#Function 2.3 only counts for unseen movies how often the searched term exists in the movie's name and synopsis and builds a ranking afterwards
def advanced_recommend_by_searched_term(searched_term, user):
  
  #access all movies
  global movies_df

  #make a copy of it because the movies which the user has already watched will be deleted in the next steps
  local_movies_df = movies_df

  #extract the user
  chosen_user = users_df[users_df["name"] == user.title()]
  
  #the movies already watched get droped out the available movies
  #therefore, the id's of the watched movies get filtered and separated so they can be accessed individually in a loop
  
  watched_movie_ids = chosen_user["movies_watched"]
  watched_movie_ids_df = watched_movie_ids.str.split(',', expand=True)
  
  #for testing purposes, the id's can be individually called like this:
  #print(watched_movie_ids_df[0][chosen_user["_id"]])
  #print(watched_movie_ids_df[1][chosen_user["_id"]])
  #print(watched_movie_ids_df[2][chosen_user["_id"]])


  a = 0
  #the columns in the watched_movies_ids_df detemerine how many movies the user has already watched
  #the while loop checks every watched movie and deletes it from the local_movies_df
  while (a < len(watched_movie_ids_df.columns)):
    
    ids = int(watched_movie_ids_df[a][chosen_user["_id"]])

    #movies already watched by the user get deleted from the local_movies_df
    local_movies_df = local_movies_df[local_movies_df["_id"] != ids]

    a = a + 1

  print("\n(F2.3. advanced_recommend_by_searched_term(searched_term)) Here are all movies you haven't watched yet:\n")
  print(local_movies_df[["name","genre","synopsis","rate","likes","shares","views"]])

  #now the following code is a copy from F2.2 to count the searched term in the movies names and synopsis
  searched_term = searched_term.lower()
  result_name = local_movies_df["name"].str.contains(pat=searched_term)
  result_synopsis = local_movies_df["synopsis"].str.contains(pat=searched_term)
  final_result = pd.merge(local_movies_df[result_name], local_movies_df[result_synopsis], how='outer')


  i = 0
  #The "length" of final_result.shape[i] is the number of rows in final_result
  while (i < final_result.shape[0]):
    
    #The name gets divided in a list of single words
    separated_name = final_result["name"].iloc[i].split()

    #The synopsis gets divided in a list of single words
    separated_synopsis = final_result["synopsis"].iloc[i].split()

    #the id of the current row gets noted
    id = final_result["_id"].iloc[i]

    word_count = 0
    #The "length" of the movies separated name is the amount of words
    #Each word gets checked if it equals the searched_term
    x = 0
    while (x < len(separated_name)):

      if (separated_name[x] == searched_term):
      #The number of times the searched_term appears in the name is saved
        word_count = word_count + 1
      x = x + 1

    #The "length" of separated synopsis is the amount of words
    #Each word gets checked if it equals the searched_term
    y = 0
    while (y < len(separated_synopsis)):

      if (separated_synopsis[y] == searched_term):
      #The number of times the searched_term appears in the synopsis is saved
        word_count = word_count + 1
      y = y + 1

      #The word count gets written in the movies_df
      final_result.loc[final_result['_id'] ==id, 'word_count'] = word_count

    i = i + 1

  #The movie with the highest word_count gets printed out
  max_word_df = final_result.loc[final_result['word_count'].idxmax()]
  print("\n(F2.3 advanced_recommend_by_searched_term(searched_term)) You should watch "+ max_word_df["name"] + " because the searched_term " + searched_term +" appeard " + str(max_word_df["word_count"]) + " times:\n")
  print("\nHere you can find more information:\n")
  print(max_word_df[["name","genre","synopsis","rate","likes","shares","views"]])





#################### SEARCH FUNCTION CALLS ####################




print("\n(F2.1 recommend_by_searched_term(searched_term)) Please type in what you want to search for:\n")
#searched_term = input()
#recommend_by_searched_term(searched_term)
recommend_by_searched_term("Wrong")

print("\n(F2.2. basic_recommend_by_searched_term(searched_term)) Please type in what you want to search for:\n")
#searched_term = input()
#basic_recommend_by_searched_term(searched_term)
basic_recommend_by_searched_term("Wrong")

print("\n(F2.3 advanced_recommend_by_searched_term(searched_term,user)) Please type in what you want to search for and who is searching:\n")
#searched_term = input()
#user= input().title()
#advanced_recommend_by_searched_term(searched_term, user)
advanced_recommend_by_searched_term("wrong", "dylan")




############################# 3. LIKE #############################
############################# BASICS ##############################




def recommend_by_most_liked_in_genre(genre):
    #filter movies by specified genres and likes
    genre_df = movies_df[movies_df["genre"] == genre]
    #sort the data by likes
    results_df = genre_df.sort_values(by=["likes"], ascending=False)
    #use head function to display top 5
    print("\n(F3.1 recommend_by_most_liked_in_genre(genre)) Here are the 5 most liked movies of the genre\n " + genre + ":\n")
    print(results_df[["name","genre","synopsis","rate","likes","shares","views"]].head())




############################# LIKE #############################
########################## ASSIGNMENT ##########################




#the following function F3.2 belongs to the "LIKE" section but was already mentioned above (1. DATA as F1.3) to prevent errors because other functions related to it. This is the full function with additional printed messages:

def like_a_movie(movie_id, user_id):

  #get the user
  user = users_df[users_df["_id"]==user_id]

  #get the movie's data 
  movie_user_watched = movies_df[movies_df["_id"] ==movie_id]

  print("\n(F3.2. like_a_movie(movie_id, user_id)) " +user["name"].values.item().title() +" gives "+movie_user_watched["name"].values.item() + " a like.\n")

  #get the amount of likes which the movie already has
  likes = movie_user_watched["likes"]

  #increment the likes by one
  likes = likes +1

  #update the likes in the movies_df
  movies_df.at[movie_id,'likes']=likes

  #update the last movie of the user
  users_df.iloc[user_id, users_df.columns.get_loc('_id_last_movie')] = movie_id

  #get the updated movie data and print them out
  movie_user_watched = movies_df[movies_df["_id"] ==movie_id]

  print("\n(F3.2. like_a_movie(movie_id, user_id)) These are the updated data: \n")
  print(movie_user_watched[["name","rate","likes","shares","views"]])
  print()
  #get the updated user data and print them out
  user = users_df[users_df["_id"]==user_id]
  print(user[["name","_id_last_movie"]])




#This function F3.3 shows the most liked movies and the user can choose which period of the movies like-history is used to make the recommendation
def show_liked_movies_by_time(time_period):
 if time_period.lower() == "total":
  results_df = movies_df.sort_values(by=["likes"], ascending=False).head(5)
  results_df= results_df[["name","likes"]]
  print("\n(F3.3 show_liked_movies_by_time(time_period)) The 5 most liked movies of all times are:\n")
  print (results_df)

 elif time_period.lower() == "likes_today":
  results_df = movies_df.sort_values(by=["likes_today"], ascending=False).head(5)
  results_df= results_df[["name","likes_today"]]
  print("\n(F3.3 show_liked_movies_by_time(time_period)) The 5 most liked movies of today are:\n")
  print (results_df)

 elif time_period.lower() == "likes_this_week":
  results_df = movies_df.sort_values(by=["likes_this_week"], ascending=False).head(5)
  results_df= results_df[["name","likes_this_week"]]
  print("\n(F3.3 show_liked_movies_by_time(time_period)) The 5 most liked movies of this week are:\n")
  print (results_df)

 elif time_period.lower() == "likes_this_month":
  results_df = movies_df.sort_values(by=["likes_this_month"], ascending=False).head(5)
  results_df= results_df[["name","likes_this_month"]]
  print("\n(F3.3 show_liked_movies_by_time(time_period)) The 5 most liked movies of this month are:\n")
  print (results_df)

 elif time_period.lower() == "likes_this_year":
  results_df = movies_df.sort_values(by=["likes_this_year"], ascending=False).head(5)
  results_df= results_df[["name","likes_this_year"]]
  print("\n(F3.3 show_liked_movies_by_time(time_period)) The 5 most liked movies of this year are:\n")
  print (results_df)

 else:
    print("\n(F3.3 show_liked_movies_by_time(time_period)) Please choose total / likes_today / likes_this_week / likes_this_month / likes_this_year\n")

  


#This advanced function F3.4 is able to make a recommendation with the favourite genre(s) of the user and only gets the user_id as a parameter
def recommend_by_likes_in_users_genre(user_id):

  #get the user's data
  user= users_df[users_df["_id"]==user_id]

  #get the favourite genre(s)
  genre = user["genres_liked"]

  #filter the movies by the specified genres and likes
  genre_df = movies_df[movies_df["genre"] == genre.values.item()]
 
  #sort the data
  results_df = genre_df.sort_values(by=["likes"], ascending=False)
  
  #use the head function to display top 5 movies of the user's favourite genre
  print()
  print("\n(F3.4. recommend_by_likes_in_users_genre(genre)) Here are the 5 most liked movies of the genre " + genre.values.item() + ":\n")
  print(results_df[["name","rate","likes","shares","views"]].head())




###################### LIKE FUNCTION CALLS #####################


  

print("\n(F3.1. recommend_by_most_liked_in_genre(genre)) Please type in your favorite genre:\n")
#searched_genre = input().title()
#recommend_by_most_liked_in_genre(searched_genre)
recommend_by_most_liked_in_genre("Crime")

like_a_movie(6,0)

show_liked_movies_by_time("yesterday")
show_liked_movies_by_time("total")
show_liked_movies_by_time("likes_today")
show_liked_movies_by_time("likes_this_week")
show_liked_movies_by_time("likes_this_month")
show_liked_movies_by_time("likes_this_year")

recommend_by_likes_in_users_genre (0)
recommend_by_likes_in_users_genre (1)




############################# 4. RATE #############################
############################# BASICS ##############################




#This function 4.1 shows all movies of movies_df which have a minimum rate
def recommend_by_rate(min_rating):
    global movies_df

    #filter the movies by a minimum rating
    results_df = movies_df[movies_df["rate"] >= min_rating]
    print("\n(F4.1 recommend_by_rate(min_rating)) Here are all movies with a rating higher or equal than: " + str(min_rating))
    print(results_df[["name","genre","synopsis","rate","likes","shares","views"]])




#This function 4.2 reads in a genre and then prints out movies of the genre with a high rate
def recommend_by_top_rating_in_genre(genre):
    global movies_df

    #first of all, the system filters movies by the specified genre
    genre_df = movies_df[movies_df["genre"] == genre]

    #second, the data gets sorted by rate and printed out
    results_df = genre_df.sort_values(by=["rate"], ascending=False)
    print("\n(F4.2 recommend_by_top_rating_in_genre(genre)) Here are the 4 best rated movies in the genre " + genre + ":\n")
    print(results_df[["name","genre","synopsis","rate","likes","shares","views"]].head(4))




############################# RATE ##############################
########################### ASSIGNMENT ##########################




#the following function F4.3 belongs to the "RATE" section but was already mentioned above (1. DATA as F1.5) to prevent errors because other functions related to it. This is the full function with additional printed messages:

def rate_a_movie(movie_id, rating):

  global movies_df

  #get the movie's data 
  movie_user_watched = movies_df[movies_df["_id"] ==movie_id]

  print()
  print("(F4.3 rate_a_movie(movie_id, rating))) Someone gives "+movie_user_watched["name"].values.item() + " a rating of " + str(rating) +".")

  print("\n(F4.3. rate_a_movie(movie_id, rating)) This is the movies current status:\n")
  print(movie_user_watched[["name", "rate", "number_of_people_rated"]])
  
  #get the rate and the number of raters of this movie
  rate = movie_user_watched["rate"]
  raters = movie_user_watched["number_of_people_rated"]

  #increment the amount of raters by one and update the raters in the movie_df
  raters = raters +1
  
  #update movies_df with the new amount of raters
  movies_df.at[movie_id,'number_of_people_rated']=raters

  #calculate new the new rating with an average calculation
  sum = (raters-1)*rate
  sum = sum +rating
  new_rate= sum / raters

  #upload and update the new rate in movies_df
  movies_df.at[movie_id,'rate']=new_rate
   

  for index, row in movies_df[movies_df["_id"] ==movie_id].iterrows():
    print("\n(F4.3. rate_a_movie(movie_id, rating)) This is the movies new status:\n")
    print("name, rate, number_of_people_rated")
    print(row["name"], row["rate"], row["number_of_people_rated"])
  
  #print(movies_df[["name", "rate", "number_of_people_rated"]])




#This function F4.4 shows the best rated movies and the user can choose which period of the movies rating-history is used to make the recommendation
def show_rated_movies_by_time(time_period):

 print("\n(F4.4 show_rated_movies_by_time(time_period)) Shows best rate_today/ rates_this_week / rates_this_month / rates_this_year\n")
 
 if time_period.lower() == "rate_today":
   results_df = movies_df.sort_values(by=["rate"], ascending=False).head(5)
   results_df= results_df[["name","rate"]]
   print("\n(F4.4 show_rated_movies_by_time(time_period)) The 5 movies with the best rating today are:\n")
   print (results_df)

 elif time_period.lower() == "rates_this_week":
   results_df = movies_df.sort_values(by=["rates_this_week"], ascending=False).head(5)
   results_df= results_df[["name","rates_this_week"]]
   print("\n(F4.4 show_rated_movies_by_time(time_period)) The 5 best rated movies of this week are:\n")
   print (results_df)

 elif time_period.lower() == "rates_this_month":
   results_df = movies_df.sort_values(by=["rates_this_month"], ascending=False).head(5)
   results_df= results_df[["name","rates_this_month"]]
   print("\n(F4.4 show_rated_movies_by_time(time_period)) The 5 best rated movies of this month are:\n")
   print (results_df)

 elif time_period.lower() == "rates_this_year":
   results_df = movies_df.sort_values(by=["rates_this_year"], ascending=False).head(5)
   results_df= results_df[["name","rates_this_year"]]
   print("\n(F4.4 show_rated_movies_by_time(time_period)) The 5 best rated movies of this year are:\n")
   print (results_df)

 else:
    print("\n(F4.4 show_rated_movies_by_time(time_period)) Please choose rate_today/ rates_this_week / rates_this_month / rates_this_year\n")




#This advanced function F4.5 is able to make a recommendation with the favourite genre(s) of the user and only gets the user_id as a parameter
def recommend_by_best_rated_in_genre(user_id):

  #get the user's data
  user= users_df[users_df["_id"]==user_id]

  #get the genre(s) the user likes
  genre = user["genres_liked"]

  #filter movies by specified genres
  genre_df = movies_df[movies_df["genre"] == genre.values.item()]

  #sort the data, e.g. by rate this month
  results_df = genre_df.sort_values(by=["rates_this_month"], ascending=False)
  results_df= results_df[["name","rates_this_month","likes","shares","views"]]

  #use the head-function to display the top 5 rated movies
  print()
  print("(F4.5 recommend_by_best_rated_in_genre(genre)) Here are this months 5 best rated movies of the genre "+ genre.values.item() + ":")
  print(results_df.head())




###################### RATE FUNCTION CALLS ######################




print("\n(F4.1 recommend_by_rate(min_rating)) Please insert your minimum rating expected for the movie you want to watch:\n")
#searched_min_rating = int(input())
#recommend_by_rate(searched_min_rating)
recommend_by_rate(8)

print("\n(F4.2 recommend_by_top_rating_in_genre(genre)) Please insert your favourite genre:\n")
#searched_genre = input().title()
#recommend_by_top_rating_in_genre(searched_genre)
recommend_by_top_rating_in_genre("Crime")

rate_a_movie(3, 1)
rate_a_movie(1, 10)

show_rated_movies_by_time("rate_today")
show_rated_movies_by_time("rates_this_week")
show_rated_movies_by_time("rates_this_month")
show_rated_movies_by_time("rates_this_year")
show_rated_movies_by_time("tomorrow")

recommend_by_best_rated_in_genre(0)
recommend_by_best_rated_in_genre(1)




############################# 5. VIEW #############################
############################## BASICS #############################



#This function 5.1 prints out movies where the amount of views is higher than the minimum views the user requires.
def recommend_by_views(min_views):
    global movies_df

    #extract the movies which exceed the minimum requirement
    results_df = movies_df[movies_df["views"] >= min_views]

    #sort the movies by the amount of views they have
    results_df = results_df.sort_values(by=["views"], ascending=False)

    #print out the result
    print("\n(F5.1 recommend_by_views(min_views)) Here are all movies with views higher or equal than: "+ str(min_views) +"\n")
    print(results_df[["name","genre","synopsis","rate","likes","shares","views"]])



#This function 5.2 prints out movies of a required genre sorted by the amount of views the movies have
def recommend_by_most_views_in_genre(genre):
    global movies_df

    #filter movies by the specified genre
    genre_df = movies_df[movies_df["genre"] == genre]

    #sort the data by views
    results_df = genre_df.sort_values(by=["views"], ascending=False)

    #print out the three most viewed movies in the genre
    print("\n(F5.2 recommend_by_most_views_in_genre(genre)) Here are the 3 most viewed movies in the genre "+ genre + ":\n")
    print(results_df[["name","genre","synopsis","rate","likes","shares","views"]].head(3))




############################# VIEW #############################
########################## ASSIGNMENT ##########################




#the following function F5.3 belongs to the "VIEW" section but was already mentioned above (1. DATA as F1.6) to prevent errors because other functions related to it. This is the full function with additional printed messages:
def watch_a_movie(movie_id, user_id, time_period, likes, rating, shares):

  #get the movie's data 
  movie_user_watched = movies_df[movies_df["_id"] ==movie_id]

  #get the user's data
  user = users_df[users_df["_id"]==user_id]
  
  print("(F5.3 watch_a_movie(movie_id, user_id, time_period, likes, rating, shares)) The user "+user["name"].values.item().title() +" " +time_period+" the movie  " + movie_user_watched["name"].values.item()+ " and gives it a rating of " +str(rating) +".")

  #if the like_parameter in the function call equals zero, then the movie does not get a like
  if likes != 0:
    like_a_movie(movie_id, user_id)


  #if the share_parameter in the function call equals zero, then the movie does not get a share
  if shares != 0:
    #the following code is possible but calling the function share_a_movie is shorter
    #get shares movie already has
    #shares = movie_user_watched["shares"]
    #increment shares by one
    #shares = shares +1
    #movies_df.at[movie_id,'shares']=shares
    share_a_movie_without_printing(movie_id)

  #update the movie rating
  rate_a_movie(movie_id, rating)

  #update the views
  #get the amount of views the movie already has
  views = movie_user_watched["views"]

  #increment the views by one
  views = views +1

  #update the amount of views in the movies_df
  movies_df.at[movie_id,'views']=views

  #increment the views depending on the time the movie has been watched
  #these data can be cruical for further decisions of the recommendation system
  if time_period.lower() == "viewed_today":
    views = movie_user_watched["views_today"]
    views = views +1
    movies_df.at[movie_id,"views_today"]=views
  elif time_period.lower() == "viewed_in_last_week":
    views = movie_user_watched["views_in_last_week"]
    views = views +1
    movies_df.at[movie_id,'views_in_last_week']=views
  elif time_period.lower() == "viewed_in_last_month":
    views = movie_user_watched["views_in_last_month"]
    views = views +1
    movies_df.at[movie_id,'views_in_last_month']=views
  elif time_period.lower() == "viewed_in_last_year":
    views = movie_user_watched["views_in_last_year"]
    views = views +1
    movies_df.at[movie_id,'views_in_last_year']=views
  else:
    print("\n(F5.3 watch_a_movie(movie_id, user_id, time_period, likes, rating, shares)) Please choose viewed_today / viewed_in_last_week / viewed_in_last_month / viewsed_in_last_year for choosing the time_period the movie was watched\n")

  #get updated movie data 
  movie_user_watched = movies_df[movies_df["_id"] ==movie_id]

  print("\n(F5.3 watch_a_movie(movie_id, user_id, time_period, likes, rating, shares)) This is the updated data:\n")
  print(movie_user_watched[["name","rate","likes","shares","views"]])
  print(user[["name", "_id_last_movie"]]) 
  print()




#This function F5.4 shows the most viewed movies and the user can choose which period of the movies view-history is used to make the recommendation
def show_viewed_movies_by_time(time_period):

 print("\n(F5.4 show_viewed_movies_by_time(time_period)) Shows most viewed movies total / views_today / views_in_last_week / views_in_last_month / views_in_last_year\n")

 if time_period.lower() == "total":
  results_df = movies_df.sort_values(by=["views"], ascending=False).head(5)
  results_df= results_df[["name","views"]]
  print("\n(F5.4 show_viewed_movies_by_time(time_period)) The 5 most viewed movies of all times are:\n")
  print (results_df)

 elif time_period.lower() == "views_today":
  results_df = movies_df.sort_values(by=["views_today"], ascending=False).head(5)
  results_df= results_df[["name","views_today"]]
  print("\n(F5.4 show_viewed_movies_by_time(time_period)) The 5 most viewed movies of today are:\n")
  print (results_df)

 elif time_period.lower() == "views_in_last_week":
  results_df = movies_df.sort_values(by=["views_in_last_week"], ascending=False).head(5)
  results_df= results_df[["name","views_in_last_week"]]
  print("\n(F5.4 show_viewed_movies_by_time(time_period)) The 5 most viewed movies of this week are:\n")
  print (results_df)

 elif time_period.lower() == "views_in_last_month":
  results_df = movies_df.sort_values(by=["views_in_last_month"], ascending=False).head(5)
  results_df= results_df[["name","views_in_last_month"]]
  print("\n(F5.4 show_viewed_movies_by_time(time_period)) The 5 most viewed movies of this month are:\n")
  print (results_df)

 elif time_period.lower() == "views_in_last_year":
  results_df = movies_df.sort_values(by=["views_in_last_year"], ascending=False).head(5)
  results_df= results_df[["name","views_in_last_year"]]
  print("\n(F5.4 show_viewed_movies_by_time(time_period)) The 5 most viewed movies of this year are:\n")
  print (results_df)

 else:
    print("\n(F5.4 show_viewed_movies_by_time(time_period)) Please choose total / views_today / views_in_last_week / views_in_last_month / views_in_last_year\n")




#This function F5.5 finds out what the user has recently watched. Going back to this movie's genre, the recommendation system shows movies of the same genre
def recommend_for_user_by_last_movie_watched(user):
    global movies_df

    #extract the user
    chosen_user = users_df[users_df["name"] == user.title()]

    #extract the last movie watched and print it out
    id_of_last_movie_user_watched = chosen_user["_id_last_movie"].values.item()
    last_movie_user_watched = movies_df[movies_df["_id"] ==id_of_last_movie_user_watched]

    print("\n(F5.5 recommend_for_user_by_last_movie_watched(user)) Here is the last movie the user watched:\n")
    print(last_movie_user_watched[["name","genre","synopsis","rate","likes","shares","views"]])

    #find movies in the same genre of last movie watched
    preffered_genre = last_movie_user_watched["genre"].values.item()
    print("\n(F5.5 recommend_for_user_by_last_movie_watched(user)) Here is the genre of the last movie the user watched:\n")
    print(preffered_genre)

    #get recommendations for the liked genre(s) of the user with one of many available functions, e.g.:
    recommend_by_most_views_in_genre(preffered_genre)
    




###################### VIEW FUNCTION CALLS ######################




print("\n(F5.1 recommend_by_views(min_views)) Please insert the minimum amount of views you expect for the movie you want to watch:\n")
#searched_min_views = int(input())
#recommend_by_views(searched_min_views)
recommend_by_views(1500000)

print("\n(F5.2 recommend_by_most_views_in_genre(genre)) Please insert your favourite genre:\n")
#searched_genre = input().title()
#recommend_by_most_views_in_genre(searched_genre)
recommend_by_most_views_in_genre("Animation")

watch_a_movie(7, 0, "viewed_in_last_week", 1, 8.0, 0)
watch_a_movie(1, 1, "viewed_today", 0, 4.0, 1)

show_viewed_movies_by_time("total")
show_viewed_movies_by_time("views_today")
show_viewed_movies_by_time("views_in_last_week")
show_viewed_movies_by_time("views_in_last_month")
show_viewed_movies_by_time("views_in_last_year")
show_viewed_movies_by_time("tomorrow")

print("\n(F5.5 recommend_for_user_by_last_movie_watched(user)) Please type in the users name:\n")
#myUser = input().title()
#recommend_for_user_by_last_movie_watched(myUser)
recommend_for_user_by_last_movie_watched("tassilo")




############################ 6. SHARE ###########################
############################# BASCIS ############################




#This function 6.1 prints out movies where the amount of shares is higher than the minimum shares the user requires.
def recommend_by_shares(min_shares):
    global movies_df

    #get the movies which have a higher amount of shares than the minimum of shares required by the user
    results_df = movies_df[movies_df["shares"] >= min_shares]

    #sort the result_df by the amount of shares and print it out
    results_df = results_df.sort_values(by=["shares"], ascending=False)
    print("\n(F6.1 recommend_by_shares(min_shares)) Here are all the movies with shares higher or equal than: "+ str(min_shares))
    print(results_df[["name","genre","synopsis","rate","likes","shares","views"]])




#This function 6.2 prints out movies of a required genre sorted by the amount of shares the movies have
def recommend_by_most_shares_in_genre(genre):
    global movies_df

    #filter the movies by the specified genre(s)
    genre_df = movies_df[movies_df["genre"] == genre]

    #sort the movies by shares and print them out
    results_df = genre_df.sort_values(by=["shares"], ascending=False)
    print("\n(F6.2 recommend_by_most_shares_in_genre(genre)) Here are the 3 most shared movies in the genre "+ genre + ":\n")
    print(results_df[["name","genre","synopsis","rate","likes","shares","views"]].head(3))




############################ SHARE ############################
########################## ASSIGNMENT #########################




#the following function F6.3 belongs to the "SHARE" section but was already mentioned above (1. DATA as F1.4) to prevent errors because other functions related to it. This is the full function with additional printed messages:
def share_a_movie(movie_id):

  #get the movie's data 
  movie_user_watched = movies_df[movies_df["_id"] ==movie_id]

  #get the amount of shares which the movie already has
  shares = movie_user_watched["shares"]
  
  #increment the amount of shares by one
  shares = shares +1
  
  #update the amount of shares in the movies_df
  movies_df.at[movie_id,'shares']=shares

  #get the updated movie data 
  movie_user_watched = movies_df[movies_df["_id"] ==movie_id]

  #print out the result
  print("\n(F6.3 share_a_movie(movie_id) These are the updated data: \n")
  print(movie_user_watched[["name","rate","likes","shares","views"]])



#This function F6.4 shows the most shared movies and the user can choose which period of the movies share-history is used to make the recommendation
def show_shared_movies_by_time(time_period):

 print("\n(F6.4 show_shared_movies_by_time(time_period)) Shows most shared movies total / shares_today / shares_in_last_week / shares_in_last_month / shares_in_last_year\n")

 if time_period.lower() == "total":
  results_df = movies_df.sort_values(by=["shares"], ascending=False).head(5)
  results_df= results_df[["name","shares"]]
  print("\n(F6.4 show_shared_movies_by_time(time_period)) The 5 most shared movies of all times are:\n")
  print (results_df)

 elif time_period.lower() == "shares_today":
  results_df = movies_df.sort_values(by=["shares_today"], ascending=False).head(5)
  results_df= results_df[["name","shares_today"]]
  print("\n(F6.4 show_shared_movies_by_time(time_period)) The 5 most shared movies of today are:\n")
  print (results_df)

 elif time_period.lower() == "shares_in_last_week":
  results_df = movies_df.sort_values(by=["shares_in_last_week"], ascending=False).head(5)
  results_df= results_df[["name","shares_in_last_week"]]
  print("\n(F6.4 show_shared_movies_by_time(time_period)) The 5 most shared movies of this week are:\n")
  print (results_df)

 elif time_period.lower() == "shares_in_last_month":
  results_df = movies_df.sort_values(by=["shares_in_last_month"], ascending=False).head(5)
  results_df= results_df[["name","shares_in_last_month"]]
  print("\n(F6.4 show_shared_movies_by_time(time_period)) The 5 most shared movies of this month are:\n")
  print (results_df)

 elif time_period.lower() == "shares_in_last_year":
  results_df = movies_df.sort_values(by=["shares_in_last_year"], ascending=False).head(5)
  results_df= results_df[["name","shares_in_last_year"]]
  print("\n(F6.4 show_shared_movies_by_time(time_period)) The 5 most shared movies of this year are:\n")
  print (results_df)

 else:
    print("\n(F6.4 show_shared_movies_by_time(time_period)) Please choose total / shares_today / shares_in_last_week / shares_in_last_month / shares_in_last_year\n")




#This advanced function F6.5 is able to make a recommendation with the favourite genre(s) of the user and only gets the user_id as a parameter
def recommend_by_most_shared_in_genre(user_id):

 #get the user's data
 user= users_df[users_df["_id"]==user_id]

 #get the user's favourite genre
 genre = user["genres_liked"]

 #filter the movies by the users favourite genre
 genre_df = movies_df[movies_df["genre"] == genre.values.item()]

 #sort the data by rate this month
 results_df = genre_df.sort_values(by=["shares_in_last_week"], ascending=False)
 results_df= results_df[["name","rate","likes","shares_in_last_week","views"]]
 #use head function to display top 5
 print()
 print("(F6.5 recommend_by_most_shared_in_genre(genre)) Here are this weeks 5 most shared movies of the genre "+ genre.values.item() + ":")
 print(results_df.head())




###################### SHARE FUNCTION CALLS ######################




print("\n(F6.1 recommend_by_shares(min_shares)) Please insert the minimum amount of shares you expect for the movie you want to watch:\n")
#searched_min_shares = int(input())
#recommend_by_shares(searched_min_shares)
recommend_by_shares(52000)

print("\n(F6.2 recommend_by_most_shares_in_genre(genre)) Please insert your favourite genre:")
#searched_genre = input().title()
#recommend_by_most_shares_in_genre(searched_genre)
recommend_by_most_shares_in_genre("Crime")

share_a_movie(1)

show_shared_movies_by_time("total")
show_shared_movies_by_time("shares_today")
show_shared_movies_by_time("shares_in_last_week")
show_shared_movies_by_time("shares_in_last_month")
show_shared_movies_by_time("shares_in_last_year")
show_shared_movies_by_time("tomorrow")

recommend_by_most_shared_in_genre(0)
recommend_by_most_shared_in_genre(1)




############################ 7. OTHER ############################



#This simple function 7.1 shows movies of a specified genre
def recommend_by_genre(genre):
    global movies_df

    #filter the movies by a specified genre
    results_df = movies_df[movies_df["genre"] == genre]
    print("\n(F7.1. recommend_by_genre(genre))Here are all movies of the genre "
          + genre + ":\n")
    print(results_df[["name","genre","synopsis","rate","likes","shares","views"]])



#This function 7.2 shows movies of the genre which the user likes
def recommend_for_user_by_genre(user):

    #extract the user's data
    chosen_user = users_df[users_df["name"] == user.title()]

    #extract the liked genres of the user and print them out
    liked_genres_of_the_user = chosen_user["genres_liked"].values.item()

    print("\n(F7.2 recommend_for_user_by_genre(user)) Here are the users favorite genres:\n")
    print(liked_genres_of_the_user)

    #get recommendations for liked genres of the user, e.g. with
    recommend_by_most_liked_in_genre(liked_genres_of_the_user)
    







###################### OTHER FUNCTION CALLS ######################




print("\n(F7.1 recommend_by_genre(genre)) Please type in your favorite genre:\n")
#searched_genre = input().title()
#recommend_by_genre(searched_genre)
recommend_by_genre("Crime")

print("\n(F7.2 recommend_for_user_by_genre(user)) Please type in the users name:\n")
#myUser = input().title()
#recommend_for_user_by_genre(myUser)
recommend_for_user_by_genre("tassilo")