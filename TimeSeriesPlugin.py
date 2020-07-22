def removeDashes(s):
   t = s
   while (t.find('-') != -1):
      t = t.replace('-','')
   return t
 
def is_number(s):
    try:
        float(s)
        return True
    except:
        return False


class TimeSeriesPlugin:
   def input(self, inputfile):
      self.parameters = dict()
      filestuff = open(inputfile, 'r')
      for line in filestuff:
         contents = line.strip().split('\t')
         self.parameters[contents[0]] = contents[1]

   def run(self):
      csvfile1 = open(self.parameters['dynamic'], 'r')
      csvfile2 = open(self.parameters['static'], 'r')

      # Read dynamic
      self.timeseries = []
      for line in csvfile1:
         self.timeseries.append([])
         contents = line.strip().split(',')
         for element in contents:
            self.timeseries[len(self.timeseries)-1].append(element)

      # Merge static
      firstline = csvfile2.readline().strip()
      contents = firstline.split(',')
      self.timeseries[0] = [self.timeseries[0][0]] + contents[1:] + self.timeseries[0][1:len(self.timeseries[0])]
      for line in csvfile2:
         contents = line.strip().split(',')
         staticsample = contents[0]
         if (staticsample[0] == '\"'):
            staticsample = staticsample[1:len(staticsample)-1]
         for j in range(1, len(self.timeseries)):
            dynamicsample = self.timeseries[j][0]
            if (dynamicsample[0] == '\"'):
               dynamicsample = dynamicsample[1:len(dynamicsample)-1]
            if (dynamicsample == staticsample or
                (dynamicsample.startswith(staticsample) and
                 dynamicsample[len(staticsample)] == '-')): #and
                 #is_number(removeDashes(dynamicsample[len(staticsample)+1:])))):
               self.timeseries[j] = [self.timeseries[j][0]] + contents[1:] + self.timeseries[j][1:]

   def output(self, outputfile):
         outstuff = open(outputfile, 'w')
         for i in range(len(self.timeseries)):
            for j in range(len(self.timeseries[i])):
               outstuff.write(self.timeseries[i][j])
               if (j == len(self.timeseries[i])-1):
                  outstuff.write('\n')
               else:
                  outstuff.write(',')
