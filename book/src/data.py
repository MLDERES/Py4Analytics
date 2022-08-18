# Import relevant libraries
from pathlib import Path
import pandas as pd
from pandas.core.dtypes.inference import is_list_like
   
import ast
import logging
import datetime as dt

DATA_DIR = Path.cwd().parents[0]/'data'
FALSE_VALUES = ["No", "no", "n", "N"]
TRUE_VALUES = ["Yes", "yes", "y", "Y"]

TODAY = dt.datetime.today()
_DEBUG = False


def _get_list(item, errors="ignore"):
    """
    Return a list from the item passed.
    If the item passed is a string, put it in a list.
    If the item is list like, then return it as a list.    
    
    Parameters
    ----------
    item: str or list-like
        the thing or list to ensure is a list
    errors: {‘ignore’, ‘raise’, 'coerce}, default ‘ignore’
        If the item is None, then the return depends on the errors state
        If errors = 'raise' then raise an error if the list is empty
        If errors = 'ignore' then return None
        If errors = 'coerce' then return an empty list if possible
    
    Returns
    ------
    list
        the created list
    """
    retVal = None
    if item is None:
        if errors == "coerce":
            retVal = []
        elif errors == "raise":
            raise ValueError(
                f"Value of item was {item} expected either "
                f"a single value or list-like"
            )
    elif is_list_like(item):
        retVal = list(item)
    else:
        retVal = [item]
    return retVal


def _get_column_list(df, columns=None):
    """
    Get a list of the columns in the dataframe.  
    If columns is None, then return all.
    If columns has a value, then it should be a string (col-name) or a list
    
    Parameters
    ----------
    df : DataFrame
    
    columns : str or list-like, default None
        the name of a single column or multiple columns.  
        If None or 'all' return all of the columns
    
    Returns
    -------
    list
        a list of column names
    """
    if columns == "all":
        return list(df.columns)
    else:
        cols = _get_list(columns)
        return (
            list(df.columns)
            if cols is None
            else list(set(df.columns).intersection(cols))
        )


def dump_df_desc(description=""):
    """
    This is a decorator to log the shape of the dataframe prior to running 
    the function and also after running a function
    Parameters
    ----------
    description : str
        the message to log prior to executing the wrapped function
    Example:
    -------
    @dump_df_desc('Removing columns)
    def remove_columns(df, columns):
        return df.drop(columns=columns)
    df = pd.DataFrame({'A':range(8), 'B':range(8)})
    df
    remove_columns(df, 'A')
    INFO: Removing columns
    Shape prior to remove_columns:(2,8)
    Shape after running to remove_columns:(2,8)
    Columns dropped: ['A']
    """

    def wrap(func):
        fname = func.__name__

        def echo_func(*args, **kwargs):
            logging.info(description)
            dataframe = args[0]
            logging.debug(f"Shape prior to {fname}:{dataframe.shape}")
            cols = set(dataframe.columns)
            ret_val = func(*args, **kwargs)
            logging.debug(f"Shape after running {fname}:{ret_val.shape}")
            cols_after = set(ret_val.columns)
            col_diff = cols.difference(cols_after)
            if len(col_diff) == 0:
                logging.debug("No columns dropped.")
            else:
                logging.debug(f"Columns dropped: {col_diff}")
            return ret_val

        return echo_func

    return wrap


def replace_string_in_col_name(df, columns=None, find_val=" ", replace_val=""):
    """
    Replace a substring in a column name and replace it with another name
    For instance, spaces to be removed or replaced with `_` 
    or eliminate post-merge suffixes
    
    Parameters:
    ----------
    df : DataFrame
        the DataFrame to work on
    columns : str or list-like
        columns that are in-scope for the change, 
        if None or 'all' then all columns
    find_val : str, default=' '
        value to replace in the column name
    replace_val: str, default=''
    
    Returns:
    -------
    DataFrame
        new dataframe with the updated column names
    """
    rename_cols = _get_column_list(df, columns)
    rename_cols = df.columns if rename_cols is None else rename_cols
    col_dict = {c: c.replace(find_val, replace_val) for c in rename_cols}
    return df.rename(columns=col_dict)


@dump_df_desc()
def remove_columns(df, columns, errors="ignore"):
    """
    Remove columns from a dataframe. Includes a single column, or multiple
    Parameters:
    ----------
    df : DataFrame
        the DataFrame to work on
    columns : str or list-like
        columns that are in-scope for the change, 
        if None or 'all' then all columns
    
    errors: {‘ignore’, ‘raise’, 'coerce}, default ‘ignore’
        If the item is None, then the return depends on the errors state
        If errors = 'raise' then raise an error if the list is empty
        If errors = 'ignore' then return None
        If errors = 'coerce' then return an empty list if possible
    Return:
    ------
    The modified dataframe
    """
    drop_columns = _get_column_list(df, columns)
    return df.drop(columns=drop_columns, errors=errors)


@dump_df_desc(description="Convert columns to True/False from 1/0")
def convert_to_bool(df, columns, inplace:bool=False):
    """
    Convert the list of columns, provided in the
    
    Parameters:
    ----------
    df : DataFrame
        the DataFrame to work on
    columns : str or list-like
        columns that are in-scope for the change, 
        if None or 'all' then all columns
    Return:
    ------
    The modified dataframe
    """
    d_map = {0: False, 1: True}
    for col in _get_column_list(df, columns):
        if df[col].dtype != "bool":
            logging.debug(f"Converting column to boolean - {col}")
            df[col] = df[col].map(d_map, na_action="ignore")
            df[col] = df[col].convert_dtypes(
                infer_objects=False, convert_string=False, convert_integer=False
            )
    return df


@dump_df_desc(description="Convert boolean columns to 1/0")
def convert_from_bool(df, columns, true_value=1, false_value=0,inplace:bool=False):
    """
    Convert boolean columns to 1/0
    
    Parameters:
    ----------
    df : DataFrame
        the DataFrame to work on
    columns : str or list-like
        columns that are in-scope for the change, 
        if None or 'all' then all columns
    true_value : any, default 1
        the value to use in place of True in new dataframe
    false_value : any, default 0
        the value to use in place of False in new dataframe
    inplace : bool, default false
        if True, then change the dataset provided
        otherwise return the dataset
    Return:
    ------
    The modified dataframe
    """
    d_map = {False: false_value, True: true_value}
    for col in _get_column_list(df, columns):
        if df[col].dtype == "bool":
            logging.debug(f"Converting column from boolean - {col}")
            df[col] = df[col].map(d_map, na_action="ignore")
    return None if inplace else df
    


@dump_df_desc(description="Convert columns to date columns")
def convert_to_date(df, columns):
    """
    Convert the list of columns to date only columns
    
    Parameters:
    ----------
    df : DataFrame
        the DataFrame to work on
    columns : str or list-like
        columns that are in-scope for the change, 
        if None or 'all' then all columns
    Return:
    ------
    The modified dataframe
    """
    for col in _get_column_list(df, columns):
        logging.debug(f"Converting column to datetime - {col}")
        df[col] = pd.to_datetime(df[col], errors="ignore")
    return df

@dump_df_desc(description="Convert columns to categorical")
def convert_to_categorical(df, columns):
    """
    Convert the list of columns to categorical
    
    Parameters:
    ----------
    df : DataFrame
        the DataFrame to work on
    columns : str or list-like
        columns that are in-scope for the change, 
        if None or 'all' then all columns
    Return:
    ------
    The modified dataframe
    """
    for col in _get_column_list(df, columns):
        logging.debug(f"Converting column to categorical - {col}")
        df[col] = df[col].astype('category')
    return df

@dump_df_desc(description="Convert columns to ordinal")
def convert_to_ordinal(df, columns):
    """
    Convert the list of columns to ordinal
    
    Parameters:
    ----------
    df : DataFrame
        the DataFrame to work on
    columns : str or list-like
        columns that are in-scope for the change, 
        if None or 'all' then all columns
    Return:
    ------
    The modified dataframe
    """
    for col in _get_column_list(df, columns):
        logging.debug(f"Converting column to ordinal - {col}")
        df[col] = pd.Categorical(df[col], ordered=True)
    return df


@dump_df_desc(description="Dropping rows with not enough relevant data")
def remove_na_rows(df, how="any", threshold=None, subset=None):
    """
    Drop out any rows that don't have at least `threshold` 
    number of values in the columns specified
    
    Parameters:
    ----------
    df : DataFrame
        the DataFrame to work on
   
    Return:
    ------
    The modified dataframe
    Notes:
    -----
    A wrapper for Pandas dropna function, with a wrapper to
    allow for capturing the change in dataframe shape.
    """
    return df.dropna(axis=0, how=how, thresh=threshold, subset=subset)


# TODO: Write a test for this function
@dump_df_desc("Removing duplicate columns based on index")
def remove_duplicates(df):
    """
    Remove duplicated rows
    Where there is more than one row that have the same index value,
    this function will create a dataframe with only one copy of that
    row.
    Parameters:
    ----------
    df : DataFrame
        the DataFrame to work on
    
    Return:
    ------
    The modified dataframe
    """
    return df.groupby(df.index).first()


def count_empty_rows(df, column):
    """
    Get a count of rows with NA or 0 values
    Parameters:
    ----------
    df : DataFrame
        the DataFrame to work on
    columns : str or list-like
        columns that are in-scope for the change, 
        if None or 'all' then all columns
    Return:
    ------
    int
        the number of rows that are NA or have a 0 value
    """
    return (df[column].isna().sum()) + (df[column] == 0).sum()


def get_dict_from_string(s):
    try:
        d = eval(s)
    except Exception as e:
        d = {}
        logging.error(e)
    return d


def split_merged(df):
    """
    Given a merged dataset return the two parts (those that matched
    and those that didn't)
       
    Parameters:
    ----------
    df : DataFrame
        the DataFrame to work on
    Return:
    ------
    The modified dataframe
    """
    df_missing = df[df["_merge"] != "both"]
    df = df[df["_merge"] == "both"]
    df.drop(columns=["_merge"], errors="ignore", inplace=True)
    df_missing.drop(columns=["_merge"], errors="ignore", inplace=True)
    return df, df_missing


# TODO: Need a test for this method
def force_data_types(df, map, columns="all", errors="ignore"):
    """
    Parameters:
    ----------
    df : DataFrame
        the DataFrame to work on
    columns : str or list-like
        columns that are in-scope for the change, 
        if None or 'all' then all columns
    Return:
    ------
    The modified dataframe
    """
    cols = _get_column_list(df, columns)
    for c in cols:
        col_type = map.get(c, None)
        if col_type is None:
            logging.debug(f"No conversion available for column {c}.")
            continue
        if col_type == "date":
            df[c] = pd.to_datetime(df[c]).date()
        else:
            df[c] = df[c].as_type(col_type)


def text_to_dict(df, columns="all"):
    """
    
    Parameters:
    ----------
    df : DataFrame
        the DataFrame to work on
    columns : str or list-like
        columns that are in-scope for the change, 
        if None or 'all' then all columns
    Return:
    ------
    The modified dataframe
    """
    cols = _get_column_list(df, columns)
    for column in cols:
        df[column] = df[column].apply(
            lambda x: {} if pd.isna(x) else ast.literal_eval(x)
        )
    return df

# def reorder_columns(df: pd.DataFrame, fixed_columns:Union[str, Sequence[str]])->pd.DataFrame:
#     '''
#     Restructure a dataframe to put the provided columns first in the output
#     Parameters:
#     ----------
#     df : DataFrame
#         the DataFrame to work on
#     columns : str or list-like
#         the columns that should be put first
#     Return:
#     ------
#     The modified dataframe
#     Example:
#     --------
#     >>> import pandas as pd
#     >>> df = pd.DataFrame({'A':range(5),'B':range(5), 'C':range(5)})
#     >>> df
#        A  B  C
#     0  0  0  0
#     1  1  1  1
#     2  2  2  2
#     3  3  3  3
#     4  4  4  4
#     >>> reorder_columns(df, ['C','A'])
#        C  A  B
#     0  0  0  0
#     1  1  1  1
#     2  2  2  2
#     3  3  3  3
#     4  4  4  4
#     '''


def load_data(fileName: str, **kwargs) -> pd.DataFrame:
    data_file = DATA_DIR/f'{fileName}.csv'
    print(data_file)
    return pd.read_csv(DATA_DIR / f"{fileName}.csv", **kwargs)


def load_excel(fileName: str, **kwargs) -> pd.DataFrame:
    return pd.read_excel(DATA_DIR / f"{fileName}.xlsx", **kwargs)


def normalize(df:pd.DataFrame, columns, drop_old=False)-> pd.DataFrame:
    data = df.copy(deep=True)
    for c in columns:
        new_column_name = f"{c}_NORM"
        data[new_column_name] = (data[c] - data[c].min()) / (data[c].max() - data[c].min())
    if drop_old:
        data.drop(columns=columns,inplace=True)
    return data


def standardize(df:pd.DataFrame, columns, drop_old=False)-> pd.DataFrame:
    data = df.copy(deep=True)
    for c in columns:
        new_column_name = f"{c}_STD"
        data[new_column_name] = (data[c] - data[c].mean()) / data[c].std()
    if drop_old:
        data.drop(columns=columns,inplace=True)
    return data

if __name__ == "__main__":
    test_df = pd.DataFrame({'a':[1,0,1,0]})
    print(convert_to_bool(test_df,'a').head())

    


