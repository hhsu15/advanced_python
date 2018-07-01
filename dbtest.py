import sqlite3

"""
Never use this:
symbol = 'data'
execute("select * from table where symbol = %s" % symbol)

Use this:
data = ('data',) 
execute("select * from table where symboe = ?", data)
"""

def main():
	try:		
		con = sqlite3.connect('test.db')
    	
		# create connection
		cur = con.cursor()
		cur.executescript("""DROP TABLE IF EXISTS Pets;	              
				CREATE TABLE Pets(id INT, Name TEXT, Price INT);
				INSERT INTO Pets VALUES(1, 'cat', 400);
				INSERT INTO Pets VALUES(2, 'dog', 1400);
				INSERT INTO Pets VALUES(3, 'mouse', 40);"""
				)
		pets = ((5, "rabit", 100),
		(6, "bird", 40))
		
		cur.executemany("INSERT INTO Pets VALUES(?, ?, ?)", pets)
        # commit the changes -- for changing the db 
		con.commit()
        
		# execute the query 
		cur.execute("SELECT * FROM Pets")
		# fetch the result
		data = cur.fetchall()
        
		for row in data:
			print(row)
		#print(data)
	except sqlite3.Error:
		if con:
			print("Error..rolling back")
			con.rollback()

	finally:
		if con:
			con.close()
	con.close()

if __name__ == "__main__":
	main()

