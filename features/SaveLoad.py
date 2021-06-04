import pickle

def Save(obj):
    pickle.dump(obj, open('./data/game.dat', 'wb'))

def Load():
    obj = pickle.load(open('./data/game.dat', 'rb'))
    return obj