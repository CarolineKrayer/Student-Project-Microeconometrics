#############################################################################################################################
#############################################################################################################################
########### auxiliary file for replication of regressions
#############################################################################################################################
#############################################################################################################################

import econtools
import econtools.metrics as mt
from econtools import read, outreg, table_statrow, write_notes
from auxiliary import *



# ************************************ TREATMENT EFFECT ESTIMATION **********************************************************


# 2SLS regression for average treatment effect estimate for two types of clustered standard errors
def main_reg(df):
    # store (exogenous) regressors for first and second stage in a list
    regressors_base = ['const', 'mean_hvac_share', 'mean_unempl', 'munempldiff', 'mskattekrdiff', 'mbefdiff', 'ekbistandpc_diff',
                        'dsmastad', 'dstorstad', 'dsv_maj_1', 'dseatsmp_1', 'dseatsop_1', 'panel8891', 'panel9194', 'flyktingandel']
    exog_base = ['const', 'mean_hvac_share', 'mean_unempl', 'munempldiff', 'mskattekrdiff', 'mbefdiff', 'ekbistandpc_diff', 'dsmastad', 
                    'dstorstad', 'dsv_maj_1', 'dseatsmp_1', 'dseatsop_1', 'panel8891', 'panel9194']

    ### standard errors clustered at municipality level
    # first stage
    reg1 = mt.reg(df, y_name = 'nonOECDshare_diff', x_name = regressors_base, cluster = 'kommun')
    # second stage
    iv1 = mt.ivreg(df, y_name = 'soc_bidr_diff', x_name = 'nonOECDshare_diff', z_name = 'flyktingandel', w_name = exog_base, 
                   iv_method = '2sls', cluster = 'kommun')

    ### standard errors clustered at county level
    # first stage
    reg2 = mt.reg(df, y_name = 'nonOECDshare_diff', x_name = regressors_base, cluster = 'countykod')
    # second stage
    iv2 = mt.ivreg(df, y_name = 'soc_bidr_diff', x_name = 'nonOECDshare_diff', z_name = 'flyktingandel', 
                   w_name = exog_base, iv_method = '2sls', cluster = 'countykod')

    # call function from auxiliary file that creates Latex table fragments for Table 2
    get_table2(df, reg1, iv1, reg2, iv2)
    
    
    # perform F-test for relevance of the instrument
    F_stat1 = reg1.Ftest('flyktingandel')[0]
    F_stat2 = reg2.Ftest('flyktingandel')[0]
    
    return(reg1, iv1, reg2, iv2, F_stat1, F_stat2)




# 2SLS regression for heterogenous treatment effects
def heterog_reg(df):
    # define a function that gets the desired individual characteristic to include and spits out the IV estimate
    def IV_regression(variable):

        if variable == 'Income < p15':
            df['regressor'] = df['Income < p15']
            df['interaction_first'] = df['Refugee inflow * (y < p15)']
            df['interaction_second'] = df['DeltaIM * (y < p15)']
        elif variable == 'Income < p40':
            df['regressor'] = df['Income < p40']
            df['interaction_first'] = df['Refugee inflow * (y < p40)']
            df['interaction_second'] = df['DeltaIM * (y < p40)']
        elif variable == 'Income > p85':
            df['regressor'] = df['Income > p85']
            df['interaction_first'] = df['Refugee inflow * (y > p85)']
            df['interaction_second'] = df['DeltaIM * (y > p85)']
        elif variable == 'Wealth < p40':
            df['regressor'] = df['Wealth < p40']
            df['interaction_first'] = df['Refugee inflow * (w < p40)']
            df['interaction_second'] = df['DeltaIM * (w < p40)']
        elif variable == 'Wealth < p60':
            df['regressor'] = df['Wealth < p60']
            df['interaction_first'] = df['Refugee inflow * (w < p60)']
            df['interaction_second'] = df['DeltaIM * (w < p60)']
        elif variable == 'Wealth > p85':
            df['regressor'] = df['Wealth > p85']
            df['interaction_first'] = df['Refugee inflow * (w > p85)']
            df['interaction_second'] = df['DeltaIM * (w > p85)']
        elif variable == 'tjman_t_1':
            df['regressor'] = df['tjman_t_1']
            df['interaction_first'] = df['Refugee inflow * white-collar']
            df['interaction_second'] = df['DeltaIM * white-collar']
        elif variable == 'arbetare_t_1':
            df['regressor'] = df['arbetare_t_1']
            df['interaction_first'] = df['Refugee inflow * blue-collar']
            df['interaction_second'] = df['DeltaIM * blue-collar']

        exog = ['const', 'mean_hvac_share', 'mean_unempl', 'munempldiff', 'mskattekrdiff', 'mbefdiff', 'ekbistandpc_diff', 'dsmastad', 
                'dstorstad', 'dsv_maj_1', 'dseatsmp_1', 'dseatsop_1', 'panel8891', 'panel9194', 'regressor']
        endog = ['nonOECDshare_diff', 'interaction_second']
        instr = ['flyktingandel', 'interaction_first']
        second_stage = mt.ivreg(df, y_name = 'soc_bidr_diff', x_name = endog, z_name = instr, w_name = exog, iv_method = '2sls',
                                cluster = 'kommun')
        return second_stage

    # store IV regression results in a dictionary
    result = dict()
    
    # perform IV regressions with the different interaction terms
    for variable in ['Income < p15', 'Income < p40', 'Income > p85', 'Wealth < p40', 'Wealth < p60', 'Wealth > p85', 'tjman_t_1', 
                     'arbetare_t_1']:
        result[variable] = IV_regression(variable)

    # call functions from auxiliary file that creates LaTex table fragments for Tables 3, 4 and 5
    get_table3(df, result)
    get_table4(df, result)
    get_table5(df, result)
    
    return(result)
    
    
    
# ***************************************** PLACEBO ANALYSIS **********************************************************
    
    
# 2SLS regression for placebo in treatment
def placebo_reg(df_placebo):
    # store (exogenous) regressors for first and second stage in a list
    regr = ['const', 'mean_hvac_share', 'mean_unempl', 'munempldiff', 'mskattekrdiff', 'mbefdiff', 'ekbistandpc_diff', 'dsmastad', 
            'dstorstad', 'dsv_maj_1', 'dseatsmp_1', 'dseatsop_1', 'flyktingandel_tplus1', 'flyktingandel_tplus2', 'flyktingandel_tplus3']
    exog = ['const', 'mean_hvac_share', 'mean_unempl', 'munempldiff', 'mskattekrdiff', 'mbefdiff', 'ekbistandpc_diff', 'dsmastad', 
            'dstorstad', 'dsv_maj_1', 'dseatsmp_1', 'dseatsop_1']

    # first stage
    reg_placebo1 = mt.reg(df_placebo, y_name = 'nonOECDshare_diff_tplus1', x_name = regr, cluster = 'kommun')
    reg_placebo2 = mt.reg(df_placebo, y_name = 'nonOECDshare_diff_tplus2', x_name = regr, cluster = 'kommun')
    reg_placebo3 = mt.reg(df_placebo, y_name = 'nonOECDshare_diff_tplus3', x_name = regr, cluster = 'kommun')

    # second stage
    iv_placebo = mt.ivreg(df_placebo, y_name = 'soc_bidr_diff', x_name = ['nonOECDshare_diff_tplus1', 'nonOECDshare_diff_tplus2',
    'nonOECDshare_diff_tplus3'], z_name = ['flyktingandel_tplus1', 'flyktingandel_tplus2', 'flyktingandel_tplus3'], w_name = exog, 
                          iv_method = '2sls', cluster = 'kommun')

    # call function from auxiliary file that creates LaTex table fragments for Table 6
    get_table6(df_placebo, reg_placebo1, reg_placebo2, reg_placebo3, iv_placebo)
    
    
    # perform joint test of the three placebo treatments in the second stage regression
    # return p-value of the test
    pvalue = iv_placebo.Ftest(['nonOECDshare_diff_tplus1', 'nonOECDshare_diff_tplus2', 'nonOECDshare_diff_tplus3'])[1]
    
    return(reg_placebo1, reg_placebo2, reg_placebo3, pvalue)
    
    
    
    
    
# ************************************ SENSITIVITY ANALYSES **********************************************************
    
    
# 2SLS regression excluding municipalities that are in one of the three big city counties 
def sens1_reg(df, df_sens1):
    # run regression without dummy for large-sized municipal population as we excluded big city counties
    # otherwise all values of that variable are zero and we cannot invert the regressor matrix
    regressors_sens1 = ['const', 'mean_hvac_share', 'mean_unempl', 'munempldiff', 'mskattekrdiff', 'mbefdiff', 'ekbistandpc_diff', 'dsmastad', 
                        'dsv_maj_1', 'dseatsmp_1', 'dseatsop_1', 'panel8891', 'panel9194', 'flyktingandel']
    exog_sens1 = ['const', 'mean_hvac_share', 'mean_unempl', 'munempldiff', 'mskattekrdiff', 'mbefdiff', 'ekbistandpc_diff', 'dsmastad', 
                  'dsv_maj_1', 'dseatsmp_1', 'dseatsop_1', 'panel8891', 'panel9194']

    # first stage
    reg_sens1 = mt.reg(df_sens1, y_name = 'nonOECDshare_diff', x_name = regressors_sens1, cluster = 'kommun')
    # second stage
    iv_sens1 = mt.ivreg(df_sens1, y_name = 'soc_bidr_diff', x_name = 'nonOECDshare_diff', z_name = 'flyktingandel', 
                        w_name = exog_sens1, iv_method = '2sls', cluster = 'kommun')

    # call function from auxiliary file that creates LaTex table fragments for Table 7
    get_table7(df, reg_sens1, iv_sens1)
    
    return(reg_sens1, iv_sens1)
    
    
    
    
# 2SLS regression excluding panel 91/94
def sens2_reg(df, df_sens2):
    # run regression without dummy for panel period 1991/94 as we excluded the observations of that panel
    # otherwise all values of that variable are zero and we cannot invert the regressor matrix
    regressors_sens2 = ['const', 'mean_hvac_share', 'mean_unempl', 'munempldiff', 'mskattekrdiff', 'mbefdiff', 'ekbistandpc_diff', 
                        'dsmastad', 'dstorstad', 'dsv_maj_1', 'dseatsmp_1', 'dseatsop_1', 'panel8891', 'flyktingandel']
    exog_sens2 = ['const', 'mean_hvac_share', 'mean_unempl', 'munempldiff', 'mskattekrdiff', 'mbefdiff', 'ekbistandpc_diff', 'dsmastad', 
                  'dstorstad', 'dsv_maj_1', 'dseatsmp_1', 'dseatsop_1', 'panel8891']

    # first stage
    reg_sens2 = mt.reg(df_sens2, y_name = 'nonOECDshare_diff', x_name = regressors_sens2, cluster = 'kommun')
    # second stage
    iv_sens2 = mt.ivreg(df_sens2, y_name = 'soc_bidr_diff', x_name = 'nonOECDshare_diff', z_name = 'flyktingandel', w_name = exog_sens2, 
                        iv_method = '2sls', cluster = 'kommun')

    # call function from auxiliary file that creates LaTex table fragments for Table 8
    get_table8(df, reg_sens2, iv_sens2)
    
    
    # perform F-test for relevance of the instrument
    F_stat = reg_sens2.Ftest('flyktingandel')[0]

    return(reg_sens2, iv_sens2, F_stat)