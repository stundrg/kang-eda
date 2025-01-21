import pandas as pd
from kang_eda.cli.py import entry_point

def test_first():
    v = entry_point()
    # None 값이 아닌지
    assert v is not None
    # 빈 문자열이 아닌지
    assert v != ""
    # 문자열에 문자도 있고, 숫자도 있는지
    assert any(t.isalpha() for t in v)
    assert any(t.isdigit() for t in v)
    assert all(df_desc['count'].iloc[i] >= df_desc['count'].iloc[i + 1] for i in range(len(df_desc) - 1)), "Data is not sorted in descending order"
    assert all(df_asc['count'].iloc[i] <= df_asc['count'].iloc[i + 1] for i in range(len(df_asc) - 1)), "Data is not sorted in ascending order"
