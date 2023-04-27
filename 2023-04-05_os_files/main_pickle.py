import pickle

a = 1024  # variable to add to .pkl file

with open("a.pkl", "wb") as pickle_out:
    pickle.dump(a, pickle_out)

with open("a.pkl", "rb") as pickle_in:
    new_a = pickle.load(pickle_in)
print(new_a)
