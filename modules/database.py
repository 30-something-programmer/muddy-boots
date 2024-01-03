# Database class
from configparser import ConfigParser
import json
import psycopg2
import psycopg2.extras

class Database:

    # set vars
    connection = None   # The database connection (sub-class)
    cursor = None   # The cursor (sub-class of connection)

    def __init__(self, inifile) -> None:

        # Load in the config
        self.inifile = inifile        
        self.get_config()

    def get_config(self) -> None: 
        """
            Retrieve config from the ini file.
            Left non-private to allow for a refresh
        """
        # create a parser 
        parser = ConfigParser() 
        # read config file 
        parser.read(self.inifile) 
    
        # get section, default to postgresql 
        self.config = {} 
        if parser.has_section("database"): 
            params = parser.items("database") 
            for param in params: 
                self.config[param[0]] = param[1] 
        else: 
            raise Exception('Section {0} not found in the {1} file'.format("database", self.inifile)) 
        
    def _connect_to_db(self) -> None:
        self.connection = None
        try: 

            # Connect to the PostgreSQL server 
            print('Connecting to the PostgreSQL database...') 
            self.connection = psycopg2.connect(**self.config)

            # Generate a cursor - use dict to assist with json transfer
            self.cursor = self.connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
            print("Connection complete")

        except (Exception, psycopg2.DatabaseError) as error: 
            print(error) 
            
    def _disconnect_from_db(self) -> None:
        """ Remove the connection from the PostGreSQL db """

        if self.connection is not None:
            self.cursor.close()
            print('Database connection closed')

    def run_query(self, query, fetch = 0, dbChange = False) -> json:
        """
            Connects to the database, executes the command,
            retrieves the data then disconnects
            query : str - the query to be executed on the db
            fetch : int - 0 = fetch all, 1 = 1, X = x amount
            dbChange : boo - if the query requires a commit statement to make changes
        """
        self._connect_to_db()
        print(f"Running query {query}")
        self.cursor.execute(query)
       
        if query is None:
            print("ERROR - no query given")
            return None

        # Commit a change if the db is to be changed, otherwise fetch data
        if dbChange: 
            self.cursor.commit()
            self._disconnect_from_db()
            return None
        
        # Return the requested number of fetches
        if fetch == 0:
            data = self.cursor.fetchall()
        elif fetch == 1:
            data = self.cursor.fetchone()
        else:
            data = self.cursor.fetchmany(fetch)

        # Return the data and dc from database
        self._disconnect_from_db()
        return json.dumps(data, default=str)

    def test_connection(self) -> None:  
        """ Test a connection to the PostgreSQL database server """
        self._connect_to_db()
        
        print('PostgreSQL database version:') 
        self.cursor.execute('SELECT version()') 
  
        # display the PostgreSQL database server version 
        db_version = self.cursor.fetchone() 
        print(db_version) 
         
        # close the communication with the PostgreSQL 
        self._disconnect_from_db()

# Generate a db class
db = Database("Database.ini")
