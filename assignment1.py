"""
Replace the contents of this module docstring with your own details
Name:Nguyen Duong Khai
Date started:
GitHub URL:https://github.com/JCUS-CP1404/assignment-01-nguyenduongkhai
"""


import csv
import operator
movieList=[]

#open movie file  and copy to  list of movieList

with open('movies.csv', 'r') as cvs_file:
    reader = csv.reader(cvs_file)
    movieList=list(reader)
    movieList.sort(key=lambda movieList: int(movieList[1]))

def User_Input(data):
    while True:
        Check_input=input("{}:".format(data))
        if(not(Check_input.strip())):
            print("Input cannot be blank")
        else:

            return Check_input
def User_InputInt(data,number):
    while True:
        Check_input=input("{}:".format(data))
        if(Check_input.lstrip('-').isdigit()):

            if((int(Check_input))<0):
                print("Number must be >=0")
            elif((int(Check_input))>number):
                print("Number is not available");
            else:
                return Check_input;
        else:

             print("Invalid input;enter a valid number")
0
def Menu():
    print("L-List movies")
    print("A-Add new movies")
    print("W-Watch a movie")
    print("Q-Quit")

def PrintListMovie():
    count_watched = 0
    count_notwatched = 0
    for i, movie in enumerate(movieList):
        if movie[3] == "u":

            print("{} .*{:<50s} - {:<5s} ({})".format(i,movie[0], movie[1], movie[2]))
            count_notwatched += 1
        elif movie[3]=="w":
            print("{} . {:<50s} - {:<5s} ({})".format(i, movie[0], movie[1], movie[2]))
            count_watched += 1


    if count_notwatched == 0:
        print("{} movies save to movies.csv".format(count_watched))
    else:
        print("{} movies watched, {} movies still to watch".format(count_watched, count_notwatched))

#Add new Movies

def NewMovies():

    # Create new Movies with title,year,catergory and of course unwatched movies

    title=User_Input("Title")
    year=User_InputInt("Year",2020) #2020:Can not available at year:2000
    category =User_Input("Catergory")


    newMovies = [title, year, category, "u"]
    #Add new movies to movieList
    movieList.append(newMovies)

    #After add new movie,we should arrage movie list in order to year
    movieList.sort(key=lambda movieList: int(movieList[1]))
def CheckMovieWatch():
    for movie in movieList:
        if movie[3] != "w":
            return False
    return True
def WatchMovie():
    if(CheckMovieWatch()==True):
        print("No more movies to watch")
    else:
        Watch=User_InputInt("Enter the number of a movie to mark as watched",len(movieList))

        position=int(Watch);


        if movieList[position][3]=="w":
            print("You have already watched",movieList[position][0])
        else:
            movieList[position][3] = "w"
            print("{} from {} watched".format(movieList[position][0],movieList[position][1]))



def main():
    print("Movies To Watch 1.0 - by <Your Name>")

    quit=False
    while not quit:
        Menu()
        selection = input(">>>")
        selection=selection.lower()
        if(selection=='l'):
            PrintListMovie()

        elif(selection=='a'):
            NewMovies()
        elif (selection== 'w'):
            WatchMovie()
        elif (selection == 'q'):
            quit=True
        else:
            print("Invalid input,please try again.")

    with open('movies_backup.csv','w') as movies_backup:
        movies_writer=csv.writer(movies_backup,delimiter=',')
        for movies in movieList:
            movies_writer.writerow(movies)

    print("{} movies save to backup.csv".format(len(movieList)))
    print("Have a nice day :)")

if __name__ == '__main__':
    main()
