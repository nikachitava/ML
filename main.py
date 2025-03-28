import numpy as np

def print_hi(name):
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.



m = np.array([6, 2, 18, 5, 6, 23])


min_val = np.min(m)
max_val = np.max(m)
min_max_slaced = (m - min_val) / (max_val - min_val)

if __name__ == '__main__':

    print("scaled: ", min_max_slaced)




