import abc
from abc import ABC
import csv
#needs installing - on Mac use python-abc
class ButtonProcessor(ABC):
    # use this to create subclasses for each of the button actions, demonstration of Open/closed from SOLID
    @abc.abstractmethod
    def button_action(self):
        pass
  # use an init for each subclass,as they require differnt arguments, to be in accordance with the Liskov substitution principle
class CalculateProcessor(ButtonProcessor):
    def __init__(self, treeview):
        self.treeview = treeview
    pass
class StatisticsProcessor(ButtonProcessor):
    def __init__(self, treeview):
        self.treeview = treeview
    pass
class EmailProcessor(ButtonProcessor):
    def __init__(self, treeview):
        self.treeview = treeview
    pass

class SaveProcessor(ButtonProcessor):
     def __init__(self,treeview):
         self.treeview = treeview
     def button_action(self):
 #       self.treeview=treeview
        with open("new.csv", "w", newline='') as myfile:
            print("saving")
            csvwriter = csv.writer(myfile, delimiter=',')
            for row_id in self.treeview.get_children():
                row = self.treeview.item(row_id)['values']
                csvwriter.writerow(row)