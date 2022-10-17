
from data_ingestion import data_loader
from mylogging import mylogger

class trainModel:

    def __init__(self):
        self.log_writer = mylogger.App_Logger()
     
        self.file_object = open("Training_logs/ModelTrainingLog.txt", 'a+')



    def trainingModel(self):
        # Logging the start of Training
        self.log_writer.log(self.file_object, 'Start of Training')
        
        # Getting the data from the source
        data_getter=data_loader.Data_Getter(self.file_object,self.log_writer).get_data()
        # here we are calling method inside method in self.log_writer
        print(data_getter)


a=trainModel()
print(a.trainingModel())