import pandas as pd


def stats_dataframe(_df):
    """
    :param _df:
    :return:
    统计 dataframe 的一些我想了解的参数
    """
    pass


def stats_series(_df):
    """
    :param _df:
    :return:
    统计 series 的一些参数
    """
    pass


def percentile_group(raw_df, groups, p_col, start_p, end_p):
    """
    通过增加辅助列的方式可能会存在一些误差,应该填充每一个值为
    colname_value
    :param raw_df:
    :param groups:
    :param p_col:
    :param start_p:
    :param end_p:
    :return:
    """
    cols = raw_df.columns
    merged_cols_name = "grp_" + "".join(cols)
    if merged_cols_name in cols:
        raise ValueError("大哥,我吧列名起的这么冷门你都能重名,我也真的是给跪了")

    raw_df[merged_cols_name] = ""
    for group in groups:
        raw_df[merged_cols_name] += raw_df[group].fillna("{}_nan".format(group)).astype(str)


def percentile_dataframe_by_groups_value_counts(raw_df, groups, v_col, p_col, start_p, end_p):
    """
    :param raw_df:
    :param groups:
    :param v_col:
    :param p_col:
    :param start_p:
    :param end_p:
    :return:
    """
    pass


def percentile_dataframe_by_col(raw_df, p_col, start_p=0.05, end_p=0.95, copy=True):
    """
    :param raw_df:
    :param p_col:
    :param start_p:
    :param end_p:
    :param copy:
    :return:

    依照指定列 p_col (比如说金额) 进行 percentile
    """

    df = raw_df[(raw_df[p_col].quantile(start_p) < raw_df[p_col]) & (raw_df[p_col] < raw_df[p_col].quantile(end_p))]
    if copy:
        return df.copy()
    else:
        return df


def percentile_dataframe_by_value_counts(raw_df, v_col, p_col, start_p, end_p):
    """
    依照单个类别进行划分
    PS: 如果需要按照多个类别进行划分的话, 可以增加辅助列,然后进行划分
    """
    items = raw_df[v_col].value_counts().items()
    if len(items) <= 30:
        pass

    dfs = []
    for category, counts in items:
        category_df = raw_df[raw_df[v_col] == category].copy()
        df = percentile_dataframe_by_col(category_df, p_col, start_p, end_p)
        dfs.append(df)

    return pd.concat(dfs)


def diff_two_dataframes(df1, df2, left_on=True, right_on=True):
    """
    :param df1:
    :param df2:
    :param left_on:
    :param right_on:
    :return:
    应该返回四张表, 更新记录,删除记录,更新后的表
    """
    pass

def l(df1):
    """
    拉格朗日插值法, 用于补充少量缺失数据
    :return:
    应该返回四张表, 更新记录,删除记录,更新后的表
    """
    pass
