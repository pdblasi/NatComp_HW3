import Tkinter as tk
import numpy as np

def index_2d(myList, v):
    for i, x in enumerate(myList):
        if v in x:
            return (i, x.index(v))

class CADisplay(tk.Canvas):
    SIZE = 500

    def __init__(self, parent, ca):
        tk.Canvas.__init__(self, parent, background='black', height=self.SIZE, width=self.SIZE)
        self.parent = parent
        self.parent.title("Paul-way's Game of Life")
        self.ca = ca
        self.rect_size = ((self.SIZE - self.ca.size) // self.ca.size)
        self.init_cells()
        self.started = False

    def init_cells(self):
        self.ca.init_cells()
        self.cells = []
        for i in range(self.ca.size):
            self.cells.append([])
            for j in range(self.ca.size):
                self.cells[i].append(self.create_rectangle(1 + (j * self.rect_size) + j,
                                                           1 + (i * self.rect_size) + i,
                                                           1 + ((j+1) * self.rect_size) + (j+1),
                                                           1 + ((i+1) * self.rect_size) + (i+1),
                                                           fill='white'))
                self.tag_bind(self.cells[i][j], '<1>', self.onCellClicked)

    def onCellClicked(self, event):
        id = event.widget.find_closest(event.x, event.y)
        if self.itemcget(id, 'fill') == 'gray':
            self.itemconfig(id, fill='white')
            self.ca.set_cell(index_2d(self.cells, id[0]), False)
        else:
            self.itemconfig(id, fill='gray')
            self.ca.set_cell(index_2d(self.cells, id[0]), True)

    def draw_cells(self):
        self.ca.step()
        for i in range(self.ca.size):
            for j in range(self.ca.size):
                if self.ca.cell(i,j):
                    self.itemconfig(self.cells[i][j], fill='gray')
                else:
                    self.itemconfig(self.cells[i][j], fill='white')
        if self.started:
            self.__start()

    def toggle_start(self):
        if self.started == False:
            self.started = True
            self.__start()
        else:
            self.started = False

    def __start(self):
        tk.Tk.after(self.parent, 100, self.draw_cells)

    def clear(self):
        self.started = False



class CA:
    def __init__(self, size):
        self.size = size
        self.init_cells()

    def init_cells(self):
        self.cells = np.zeros((self.size+2, self.size+2), dtype=bool)
        self.buffer =  np.zeros((self.size+2, self.size+2), dtype=bool)

    def cell(self, i, j):
        return self.cells[i+1][j+1]

    def set_cell(self, index, val):
        self.cells[index[0]+1][index[1]+1] = val

    def step(self):
        for i in range(1, self.size):
            for j in range(1, self.size):
                live = 0
                for r in range(-1,2):
                    for c in range(-1,2):
                        if not (r == 0 and c == 0):
                            if self.cells[i+r][j+c]:
                                live += 1
                if live < 2 or live > 3:
                    self.buffer[i][j] = False
                if live == 3:
                    self.buffer[i][j] = True
                if live == 2:
                    self.buffer[i][j] = self.cells[i][j]
        for i in range(1, self.size):
            for j in range(1, self.size):
                self.cells[i][j] = self.buffer[i][j]


class GameOfLife(tk.Tk):
    def __init__(self, ca_size):
        tk.Tk.__init__(self)
        self.resizable(width=False, height=False)
        self.display = CADisplay(self, CA(ca_size))
        self.pause = tk.Button(self, text="Start", command=self.toggle_start)
        self.clear = tk.Button(self, text="Clear", command=self.on_clear)

        self.display.grid(row=0, column=0, columnspan=2)
        self.pause.grid(row=1, column=0, sticky="we")
        self.clear.grid(row=1, column=1, sticky="we")

    def toggle_start(self):
        if 'Start' in self.pause.config('text'):
            self.pause['text'] = "Pause"
        else:
            self.pause['text'] = "Start"
        self.display.toggle_start()

    def on_clear(self):
        if 'Pause' in self.pause.config('text'):
            self.pause['text'] = "Start"
            self.display.toggle_start()
        self.display.init_cells()

if __name__ == '__main__':
    gol = GameOfLife(50)
    gol.mainloop()