
from mylogging import mylogger
from Training_Raw_data_validation.raw_validation import Raw_Data_validation

class train_validation:
    def __init__(self,path):
        self.raw_data = Raw_Data_validation(path)
        self.file_object = open("Training_Logs/Training_Main_Log.txt", 'a+')
        self.log_writer = mylogger.App_Logger()

    def train_validation(self):
        try:
            self.log_writer.log(self.file_object, 'Start of Validation on files!!')
            # extracting values from prediction schema
            column_names, noofcolumns = self.raw_data.valuesFromSchema()
            # getting the regex defined to validate filename
            regex = self.raw_data.manualRegexCreation()
            # validating filename of prediction files
            self.raw_data.validationFileNameRaw(regex)
            # validating column length in the file
            self.raw_data.validateColumnLength(noofcolumns)
            self.log_writer.log(self.file_object, "Raw Data Validation Complete!!")

            self.file_object.close()

       
        except Exception as e:
            raise e


mypath="C:\\My projects\\Stores Sales Prediction\\Training_Batch_Files"
A=train_validation(mypath).train_validation()
print(A)