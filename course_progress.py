import datetime as dt

class CourseProgress:
    def set_sections(self):
        self.sections = [[None for j in i] for i in self.times]
    
    def update_times(self):
        self.tot_items = 0
        for i in range(len(self.times)):
            for j in range(len(self.times[i])):
                self.times[i][j] = self.times[i][j].split(':')
                self.times[i][j] = dt.timedelta(0, int(self.times[i][j][0])*60 + int(self.times[i][j][1]))
                self.sections[i][j] = self.tot_items
                self.tot_items += 1
    
    def set_run_total(self):
        self.run_total = [None for  i in range(self.tot_items)]
        s = 0
        for i in range(len(self.times)):
            for j in range(len(self.times[i])):
                if s == 0:
                    self.run_total[s] = self.times[i][j]
                else:
                    self.run_total[s] = self.times[i][j] + self.run_total[s-1]
                s += 1
    
    def __init__(self,times):
        self.times = times
        self.set_sections()
        self.update_times()
        self.set_run_total()
        self.total_time = max(self.run_total).total_seconds()
        
    def get_completion_perc(self,sect_1=1, sect_2=1):
        try:
            ind = self.sections[sect_1-1][sect_2-1]
        except IndexError:
            print('Such section does not exist.')
            return None
        except:
            raise
        
        self.perc = 100 * self.run_total[ind].total_seconds() / self.total_time
        return "{value:.2f}%".format(value=self.perc)
    
    
