import tkinter
import time


class TrafficLight:

	def __init__(self):
		self.app = tkinter.Tk()
		self.__color = ["#f00", "#ff0", "#0f0"]
		self.app.geometry("200x200+100+100")
		self.app.title("Светофор")

		self.canv = tkinter.Canvas()
		self.canv.pack(fill=tkinter.Y, expand=1)

		self.running()
		self.app.mainloop()

	def running(self):
		while True:
			for col in self.__color:
				print(f"coloring with {col}", "\n")
				self.canv.delete(all)
				tkinter.Canvas.create_oval(self.canv, 50, 45, 150, 145, fill=col, width=7)
				tkinter.Canvas.update(self.app)
				if col == "#f00" or col == "#0f0":
					time.sleep(7)

				elif col == "#ff0":
					time.sleep(2)


TrafficLight()
