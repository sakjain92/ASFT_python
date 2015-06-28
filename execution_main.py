import stm_main
import os # For file handling (Relative Paths)
from common import *
import execution_header

#Output file handling
report_rpath=r"/output_bin/reports/report.txt"
report_path=os.getcwd()+report_rpath


TESTCOUNT=0
in_test_rpath=r"/output_bin/test/"
in_test_path=os.getcwd()+in_test_rpath
out_test_rpath=r"/output_bin/test/"
out_test_path=os.getcwd()+out_test_rpath



def execute_statement(path,statement):
    global TESTCOUNT

    if ( execution_header.add_stmt_to_path(path,statement) != True ):
        return False
    # Currently sequential. Need to make parallel for more test cases. 
    for constraint in statement.constraint_list:
        if( execution_header.add_constraint_to_path(path,constraint) != True ):
            # TODO:Need to fill this
            return False
            pass
    
    statement.completed=1
    TESTCOUNT=TESTCOUNT+1
    #Creates both in and out text files
    execution_header.create_test_txt(path,in_test_path,out_test_path,TESTCOUNT)
    return True 


def report_incomplete_statements():
    global report_path

    report_fp=open(report_path,'w')
    report_fp.write('Statement Coverage Report:\n')
    report_fp.write('(Showing only registers which not covered)')

    local_statement_list=stm_main.get_statement_list()
    for statement in local_statement_list:
        if(statement.completed==0):
            incomplete_string="Statement: "+"\""+statement.name+"\""+" not covered\n"
            report_fp.write(incomplete_string);
    report_fp.close()



# Execution of main
if __name__ == "__main__":

    stm_main.init_stmt_constraints()
    local_statement_list=stm_main.get_statement_list()

    for statement in local_statement_list:
        if(statement.executed==0):
            path=execution_header.PATH()
            execute_statement(path,statement)
                        
    #Reporting
    #Which statements not able to cover
    report_incomplete_statements()

