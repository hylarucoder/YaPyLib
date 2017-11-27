"""
note: 由于这些函数的使用目前来说都是在 IPython Notebook 中
所以, 保留大量的Print语句用于对数据本身产生
"""
import pandas as pd

"""
PART 1 统计类工具类
pandas 在加载少量数据的时候, 会依照自己的理解对 dataframe 的每一个 column 进行类型推导.

这会存在两个隐性的问题:
- 第一,当数据量大的时候,pandas不进行类型推导. type基本上就是object
- 第二,即便数据量不够大,做了类型推导,也需要注意一些比较奇怪的问题,比如一列中可能出现类型不统一的情况.或者,有的是int的0,有的是字符串的'0',有的是浮点数或者是字符串的0.0.

如果进行 value_counts的话,会发现这个问题.
"""


def check_columns(_df):
    """
    :param _df:
    :return:
    """
    pass


def stats_dataframe(_df):
    """
    :param _df:
    :return:
    统计 dataframe 的一些我想了解的参数
    """
    basic_info = {
        "行数": len(_df),
        "列数": len(_df.columns),
        "内存": 0
    }
    basic_info_df = pd.DataFrame(basic_info, index=[0])
    return basic_info_df
    """
    TODO: 每一列统计哪些东西呢?
    1. 空值,(如果是str的话)blank值
    2. 推断是否为类型值的概率 比如 10000 中 就 30种值,那么,就可能为类型值
    """
    col_infos = []
    for col in _df.columns:
        col_info = {
            "列名": col,
            "列类型": _df[col].type,
            "非NaN值数": _df[col],
            "NaN值数": _df[col],
            "NaN值率": _df[col],
            "唯一值数目": len(set(_df[col])),
            "唯一值e.g": list(set(_df[col]))[0:10],
        }
        col_infos.append(col_info)
        _df[col].value_counts()


def stats_series(_df):
    """
    :param _df:
    :return:
    统计 series 的一些参数
    """
    pass


"""
PART 2 查看类工具类
"""


def head_preview(_df, n=5):
    """
    :param _df:
    :param n:
    :return:
    """
    return _df.head(n).T


def tail_preview(_df, n=5):
    """
    :param _df:
    :param n:
    :return:
    """
    return _df.tail(n).T


def sample_preview(_df, n=5):
    """
    :param _df:
    :param n:
    :return:
    """
    return _df.sample(n).T


"""
PART 3 抽样类工具类
1. 按照百分位点进行抽取数据 比如 0.05 < p < 0.95
2. 按照
"""


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


"""
PART 4 过滤类工具类
"""


def search(_df, content, all_columns=True, excludes=False):
    """
    搜索包含 content 的
    """
    pass


def l(df1):
    """
    拉格朗日插值法, 用于补充少量缺失数据
    :return:
    应该返回四张表, 更新记录,删除记录,更新后的表
    """
    pass


"""
PART 5 DIFF 工具类
1. 抽样
2. 
"""


def diff_two_series(s1, s2):
    pass


def diff_two_dataframes(raw_df, new_df, on=True, unique_col="编号"):
    """
    :param raw_df:
    :param new_df:
    :param on:
    :return:
    使用本方法的
    否则无法区分是否为原来的记录
    应该返回四张表, 更新记录,删除记录,更新后的表
    """
    if unique_col not in raw_df.columns:
        raise ValueError("缺乏用于标识新旧记录的ID, 比如用户表里面的用户ID,主键之类的.")
    else:
        raw_df["版本"] = "旧"
        new_df["版本"] = "新"

        # Join all rows
        full_set_df = pd.concat([raw_df, new_df], ignore_index=True)

        changed_set_df = full_set_df.drop_duplicates(keep="last")
        dupe_unique_col_values = changed_set_df.set_index(unique_col).index.get_duplicates()
        dupes_set_df = changed_set_df[changed_set_df[unique_col].isin(dupe_unique_col_values)]

        changed_set_new_df = dupes_set_df[(dupes_set_df["版本"] == "新")]
        changed_set_raw_df = dupes_set_df[(dupes_set_df["版本"] == "旧")]

        changed_set_new_df = changed_set_new_df.drop(['版本'], axis=1)
        changed_set_raw_df = changed_set_raw_df.drop(['版本'], axis=1)

        changed_set_new_df.set_index(unique_col, inplace=True)
        changed_set_raw_df.set_index(unique_col, inplace=True)

        def report_diff(x):
            return x[0] if x[0] == x[1] else '{} ---> {}'.format(*x)

        # Now we can diff because we have two data sets of the same size with the same index
        diff_panel = pd.Panel(dict(df1=changed_set_raw_df, df2=changed_set_new_df))
        diff_output = diff_panel.apply(report_diff, axis=0)

        def judge_row(row):
            def judge(x):
                if isinstance(x, str):
                    if "--->" in x:
                        return True
                return False

            return any([judge(v) for k, v in row.iteritems()])

        for index, row in diff_output.iterrows():
            diff_output.set_value(index, "是否修改", judge_row(row))

        # Diff'ing is done, we need to get a list of removed items

        # Flag all duplicated account numbers
        changed_set_df['是否重复'] = changed_set_df["编号"].isin(dupe_unique_col_values)

        # Identify non-duplicated items that are in the old version and did not show in the new version
        removed_set = changed_set_df[(changed_set_df["是否重复"] is False) & (changed_set_df["版本"] == "旧")]

        # We have the old and diff, we need to figure out which ones are new

        # Drop duplicates but keep the first item instead of the last
        new_set = full_set_df.drop_duplicates(keep='first')

        # Identify dupes in this new dataframe
        new_set['是否重复'] = new_set["编号"].isin(dupe_unique_col_values)

        # Identify added accounts
        added_set = new_set[(new_set["是否重复"] is False) & (new_set["版本"] == "新")]

        return {
            "旧表记录": raw_df,
            "新表记录": new_df,
            "差异记录": diff_output,
            "删除记录": removed_set,
            "增加记录": added_set,
        }


"""
PART 7 Convert Util
"""


def convert_type(df):
    """
    :param df:
    :return:
    """
    pass


"""
PART 8 Performance
"""

"""
PART 9 I/O
"""


def to_excels(filename, **df_dicts):
    writer = pd.ExcelWriter("{}.xlsx".format(filename))
    for name, df in df_dicts.items():
        df.to_excel(writer, "{}".format(name), index=False)
    writer.save()
