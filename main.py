import mysql.connector as connector

class DBHelper:
    def __init__(self):
        self.con=connector.connect(host='localhost',
                                   port='3306',
                                   user='root',
                                   password='8139',
                                   database="movies")
        query="create table if not exists movies(movID int primary key,movName varchar(100),movRelYear int,actorName varchar(100),actressName varchar(100),directorName varchar(100))"
        cur=self.con.cursor()
        cur.execute(query)
        print("DB Created")


    #insert
    def insertUser(self,movid,movname,relyear,actname,actsname,dirname):
        query="insert into movies(movID,movName,movRelYear,actorName,actressName,directorName)values({},'{}',{},'{}','{}','{}')".format(movid,movname,relyear,actname,actsname,dirname)
        

        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit() 
        print("User Saved to DB")

    #fetching
    def fetchAll(self):
        query="select * from movies"
        cur=self.con.cursor()
        cur.execute(query)
        for row in cur:
            print("Mov Id:",row[0])
            print("Movie Name:",row[1])
            print("Release Year:",row[2])
            print("Actor Name:",row[3])
            print("Actress Name:",row[4])
            print("Director Name",row[5])
            print( )

    #fetch movie by acotrs name
    def fetchMovieByActors(self):
        #change actor Name according to the table
        query="select * from movies where actorName='Henry Cavill'"
        cur=self.con.cursor()
        cur.execute(query)
        for row in cur:
            print("Mov Id:",row[0])
            print("Movie Name:",row[1])
            print("Release Year:",row[2])
            print("Actor Name:",row[3])
            print("Actress Name:",row[4])
            print("Director Name",row[5])
            print( )


#main coding 
helper=DBHelper()  


#instructions :Uncomment or comment lines according to the usage


#insert (Add movies)
helper.insertUser(100,"Avengers",2012,"Robert Downey Jr","Scarlet","Joss")
helper.insertUser(101,"Justice League",2021,"Henry Cavill","Gal Gadot","Zack Snyder")
helper.insertUser(102,"Endgame",2019,"Robert Downey Jr","Elizabeth","Russo Brothers")
helper.insertUser(103,"Man of Stell",2013,"Henry Cavill","Amy Adams","Zack Snyder")

#fetch all details
#helper.fetchAll()

#fetch details of Movies related to actors name specified
helper.fetchMovieByActors()
