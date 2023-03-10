import pandas as pd
import numpy as np
import glob

ONA_csv = {"CW" : "CW_v1_ONA_", "FL4F" : "FL_4F_v1_ONA_", "FL4T" : "FL_4T_v1_ONA_", "FL8F" : "FL_8F_v1_ONA_", "FL8T" : "FL_8T_v1_ONA_", "Taxi" : "Taxi_v1_ONA_", "FB" : "FB_v1_ONA_"}
Q_csv = {"CW" : "CW_v1_Q_", "FL4F" : "FL_4F_v1_Q_", "FL4T" : "FL_4T_v1_Q_", "FL8F" : "FL_8F_v1_Q_", "FL8T" : "FL_8T_v1_Q_", "Taxi" : "Taxi_v1_Q_", "FB" : "FB_v1_Q_"}

def myCSV(env, alg, metric_X, input_file_dir, save_file_dir):
  # Get a list of all CSV files in the directory
  if alg=="ONA":
      file_name = input_file_dir+ONA_csv[env]
      save_name= save_file_dir+ONA_csv[env][:-1]+'.csv' 
  if alg=="Q":
      file_name = input_file_dir+Q_csv[env] 
      save_name= save_file_dir+Q_csv[env][:-1]+'.csv'
  csv_files = glob.glob(file_name+'*.csv') 
  # Initialize an empty list to store the dataframes
  dataframes = []
  # Read all CSV files and store them in a list
  for file in csv_files:
      df = pd.read_csv(file)
      dataframes.append(df)
  # Get all unique success values across all dataframes
  all_s = sorted(set.union(*[set(df[metric_X]) for df in dataframes]))
  # Create new dataframes with all_s values
  new_dfs = []
  for df in dataframes:
      # Initialize new dataframe with all_s values
      new_df = pd.DataFrame({metric_X: all_s})
      # Merge with original dataframe to inherit other columns
      new_df = pd.merge(new_df, df, on=metric_X, how='left')
      new_df = new_df.set_index(metric_X)  # Set metric_X column as index
      new_dfs.append(new_df)
  # Interpolate missing data for each column separately
  for i in range(len(new_dfs)):
      df = new_dfs[i]  
      for col in df.columns:
          if col == metric_X:
              continue
          df[col] = df[col].interpolate(method="index") #(method="linear", limit_direction="both", axis=0)
  # Concatenate dataframes and group by metric_X
  df_concat = pd.concat(new_dfs)
  # Calculate average and standard deviation for each column at each metric_X value
  grouped = df_concat.groupby(metric_X).agg(['mean','std'])
  grouped.columns = ['_'.join(col).strip() for col in grouped.columns.values]
  ## Save the resulting dataframe to a new CSV file
  grouped.to_csv(save_name) #, index=False

Envs=["CW","FL4F","FL4T","FL8F","FL8T", "Taxi", "FB"]
Algorithm=["ONA","Q"]
input_file_dir= './'
save_file_dir= './'
Metrics_X=["successes"]
for env in Envs:
  for alg in Algorithm:
    for metric_X in Metrics_X:
        myCSV(env, alg, metric_X, input_file_dir, save_file_dir)