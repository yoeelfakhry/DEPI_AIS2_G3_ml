import pandas as pd 

def columns_info(df):
  """
  Function that show the Data types, missing values and unique values in each column in dataset
  Paramter
    df (Pandas) : The input DataFrame to analyze.

  Return
      
    pandas.DataFrame : A transposed DataFrame containing :
    - Row 0: Data types of each column
    - Row 1: Count of missing (null) values in each column
    - Row 2: Count of unique values in each column
  """
  col_types = df.dtypes
  sumofnulls = df.isnull().sum()
  unique_values = df.nunique()
  return pd.DataFrame({"Data types": col_types , "Nulls": sumofnulls , "Unique Values": unique_values }).T




def object_to_category(df):
  """
  Function that replace object type to category type

  Parameter
  df ( pandas.DataFrame) : The input DataFrame 
  
  Return 
  df (pandas.DataFrame) : The data frame after replace the columns
  """
  object_columns = df.select_dtypes(include=['object']).columns
  df[object_columns] = df[object_columns].astype("category")
  return df


