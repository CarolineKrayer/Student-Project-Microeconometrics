#############################################################################################################################
#############################################################################################################################
########### auxiliary file for creation of latex table fragments containing regression results
########### the corresponding .tex-file named "Table[...].tex" reads in the latex table fragments created here and then
########### creates the output tables displayed in the notebook  
########### all .tex files can be found in the folder named 'Tables'
#############################################################################################################################
#############################################################################################################################

import econtools
import econtools.metrics as mt
from econtools import read, outreg, table_statrow, write_notes

# the following function creates LaTex table fragments for Table 2 stored in the .tex-files 'table2_aux' and 'table2_aux_notes'
# the file Table2.tex then takes those fragments and turns them into a pretty table which is finally displayed in the notebook
def get_table2(df, reg1, iv1, reg2, iv2):
    
    # Put coefficients, standard errors and stars for significance level in a table
    regs = (reg1, iv1, reg2, iv2)
    table_string = outreg(regs,
                          ['flyktingandel', 'nonOECDshare_diff', 'mean_hvac_share', 'mean_unempl', 
                           'munempldiff', 'mskattekrdiff', 'mbefdiff', 'ekbistandpc_diff', 
                           'dsmastad', 'dstorstad', 'dsv_maj_1', 'dseatsmp_1', 'dseatsop_1', 
                           'panel8891', 'panel9194', 'const'],     
                          ['Refugee inflow', 'Change in share of immigrants', 'Vacant housing rate', 'Unemployment rate', 
                           'Change in unemployment rate', 'Change in tax base', 'Change in population size', 
                           'Change in welfare spending', 'Small-sized population',
                          'Large-sized population', 'Socialist majority', 'Green Party', 'New Democrats', 'Panel 1988/91',
                          'Panel 1991/94', 'Constant'],
                          digits = 4, 
                          stars = True
                         )
    
    # Save the table string to a file
    results_path = 'Tables/table2_aux.tex'
    with open(results_path, 'w') as f:
        f.write(table_string)
    
    # Save separate file with table notes
    notes = "Sample size is {}.".format(reg1.N)
    write_notes(notes, results_path)

    
# analogous procedure for Table 3
def get_table3(df, result):
    
    regs = (result['Income < p15'], result['Income < p40'], result['Income > p85'])
    
    # Put coefficients, standard errors and stars for significance level in a table
    table_string = outreg(regs,
                          ['nonOECDshare_diff', 'regressor', 'interaction_second'],     
                          ['Change in share of immigrants', 'Dummy', 'Interaction term'],
                          digits = 4, 
                          stars = True
                         )
    
    # Save the table string to a file
    results_path = 'Tables/table3_aux.tex'
    with open(results_path, 'w') as f:
        f.write(table_string)
        
    
# analogous procedure for Table 4
def get_table4(df, result):
    
    regs = (result['Wealth < p40'], result['Wealth < p60'], result['Wealth > p85'])
    
    # Put coefficients, standard errors and stars for significance level in a table
    table_string = outreg(regs,
                          ['nonOECDshare_diff', 'regressor', 'interaction_second'],     
                          ['Change in share of immigrants', 'Dummy', 'Interaction term'],
                          digits = 4, 
                          stars = True
                         )
    
    # Save the table string to a file
    results_path = 'Tables/table4_aux.tex'
    with open(results_path, 'w') as f:
        f.write(table_string)
    

    
# analogous procedure for Table 5 
def get_table5(df, result):
    
    regs = (result['arbetare_t_1'], result['tjman_t_1'])
    
    # Put coefficients, standard errors and stars for significance level in a table
    table_string = outreg(regs,
                          ['nonOECDshare_diff', 'regressor', 'interaction_second'],     
                          ['Change in share of immigrants', 'Dummy', 'Interaction term'],
                          digits = 4, 
                          stars = True
                         )
    
    # Save the table string to a file
    results_path = 'Tables/table5_aux.tex'
    with open(results_path, 'w') as f:
        f.write(table_string)

# analogous procedure for Table 6
def get_table6(df, reg1, reg2, reg3, iv):
    
    # Put coefficients, standard errors and stars for significance level in a table
    regs = (reg1, reg2, reg3, iv)
    table_string = outreg(regs,
                          ['flyktingandel_tplus1', 'flyktingandel_tplus2', 'flyktingandel_tplus3', 'nonOECDshare_diff_tplus1',
                            'nonOECDshare_diff_tplus2', 'nonOECDshare_diff_tplus3'],     
                          ['Refugee inflow 85/88', 'Refugee inflow 88/91', 'Refugee inflow 91/94', 
                           'Change in share of immigrants 85/88', 'Change in share of immigrants 88/91',
                            'Change in share of immigrants 91/94'],
                          digits = 4, 
                          stars = True
                         )
    
    # Save the table string to a file
    results_path = 'Tables/table6_aux.tex'
    with open(results_path, 'w') as f:
        f.write(table_string)
    
    # Save separate file with table notes
    notes = "Sample size is {}.".format(reg1.N)
    write_notes(notes, results_path)
    
    
# analogous procedure for Table 7
def get_table7(df, reg_sens1, iv_sens1):
    
    # Put coefficients, standard errors and stars for significance level in a table
    regs = (reg_sens1, iv_sens1)
    table_string = outreg(regs,
                          ['flyktingandel', 'nonOECDshare_diff', 'mean_hvac_share', 'mean_unempl', 
                           'munempldiff', 'mskattekrdiff', 'mbefdiff', 'ekbistandpc_diff', 
                           'dsmastad', 'dsv_maj_1', 'dseatsmp_1', 'dseatsop_1', 
                           'panel8891', 'panel9194', 'const'],     
                          ['Refugee inflow', 'Change in share of immigrants', 'Vacant housing rate', 'Unemployment rate', 
                           'Change in unemployment rate', 'Change in tax base', 'Change in population size', 
                           'Change in welfare spending', 'Small-sized population', 'Socialist majority', 
                           'Green Party', 'New Democrats', 'Panel 1988/91', 'Panel 1991/94', 'Constant'],
                          digits = 4, 
                          stars = True
                         )
    
    # Save the table string to a file
    results_path = 'Tables/table7_aux.tex'
    with open(results_path, 'w') as f:
        f.write(table_string)
    
    # Save separate file with table notes
    notes = "Sample size is {}.".format(reg_sens1.N)
    write_notes(notes, results_path)
    

# analogous procedure for Table 8
def get_table8(df, reg_sens2, iv_sens2):
    
    # Put coefficients, standard errors and stars for significance level in a table
    regs = (reg_sens2, iv_sens2)
    table_string = outreg(regs,
                          ['flyktingandel', 'nonOECDshare_diff', 'mean_hvac_share', 'mean_unempl', 
                           'munempldiff', 'mskattekrdiff', 'mbefdiff', 'ekbistandpc_diff', 
                           'dsmastad', 'dstorstad', 'dsv_maj_1', 'dseatsmp_1', 'dseatsop_1', 
                           'panel8891', 'const'],     
                          ['Refugee inflow', 'Change in share of immigrants', 'Vacant housing rate', 'Unemployment rate', 
                           'Change in unemployment rate', 'Change in tax base', 'Change in population size', 
                           'Change in welfare spending', 'Small-sized population',
                           'Large-sized population', 'Socialist majority', 'Green Party', 'New Democrats', 'Panel 1988/91',
                           'Constant'],
                          digits = 4, 
                          stars = True
                         )
    
    # Save the table string to a file
    results_path = 'Tables/table8_aux.tex'
    with open(results_path, 'w') as f:
        f.write(table_string)
    
    # Save separate file with table notes
    notes = "Sample size is {}.".format(reg_sens2.N)
    write_notes(notes, results_path)