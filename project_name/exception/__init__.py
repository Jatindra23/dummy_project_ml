import os
import sys

class ProjectException(Exception):

    def __init__(self,error_message:Exception,error_detail:sys):

        super().__init__(error_message)
        self.error_message = error_message


    @staticmethod
    def get_detailed_error_message(error_message:Exception,error_detail:sys)->str:
        """
        error_message: Exception object
        error_details: object of sys modules 
        """ 
        _,_,exec_tb = error_detail.exc_info()
        #return information about the most recent exception caught by an exception caluse in the current stack or in the old stack frame

        line_number = exec_tb.tb_frame.f_lineno
        file_name = exec_tb.tb_code.co_filename
        error_message = f"Error occured in script:[{file_name}] at line number[{line_number}]"
        return error_message
    
    def __str__(self):
        return self.error_message
    
    def __repr__(self) -> str:
        return ProjectException.__name__.str()