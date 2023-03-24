import matplotlib.pyplot as plt
def start():

f = open('C:/GitHub/new_project/react_app/frontend/pyqt_desktop_app/txt/1', "r")
line = f.readlines()
x = []
y = []
z = 1
for i in line:
    if z == 1:
        i = i[0:-1].split(',')
        for s in i:
            x.append(float(s))
    if z == 7:
        i = i[0:-1].split(',')
        for s in i:
            y.append(float(s))
    z += 1
fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()
