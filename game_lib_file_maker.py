import pickle

games = {1:['RPG', 'Oblivion ', 'Bethesda', 'Bethesda', 'All', '2006', '6',
            'Singleplayer', '$5.00', 'Yes', '01-15-2008', 'This games blows chunks']}

datafile = open("game_libr.pickle", "wb")
pickle.dump(games, datafile)
datafile.close()

