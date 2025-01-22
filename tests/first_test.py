import pandas as pd
from kang_eda.cli import group_by_count

def test_first():
    row_count = 13
    df = group_by_count("자유", True, row = row_count)
    # None 값이 아닌지
    assert df is not None
    # assert len(df) == 3
    assert isinstance(df, pd.DataFrame)
    assert df.iloc[0]['president'] == '윤보선'
    assert len(df) < row_count
    # 빈 문자열이 아닌지
    #assert v != ""
    # 문자열에 문자도 있고, 숫자도 있는지
    #assert any(t.isalpha() for t in v)
    #assert any(t.isdigit() for t in v)
   #  assert all(df_desc['count'].iloc[i] >= df_desc['count'].iloc[i + 1] for i in range(len(df_desc) - 1)), "Data is not sorted in descending order"
    # assert all(df_asc['count'].iloc[i] <= df_asc['count'].iloc[i + 1] for i in range(len(df_asc) - 1)), "Data is not sorted in ascending order"
    @pytest.mark.parametrize("is_asc,president"[(),()])
def test_정열_및_행수제한("is_asc,president"[(),()]):
    # given
    row_count = 3
    is_asc = True

    # when
    df = group_by_count(keyword = "자유", asc = is_asc, row = row_count)

    # assert
    assert isinstance(df, pd.DataFrame)
    assert df.iloc[0]['president'] == '윤보선'
    assert len(df) == row_count

def test_정열_및_행수제한_asc():
    # given
    row_count = 3
    is_asc = True

    # when
    df = group_by_count(keyword = "자유", asc = is_asc, row = row_count)

    # assert
    assert isinstance(df, pd.DataFrame)
    assert df.iloc[0]['president'] == '윤보선'
    assert len(df) == row_count

def test_정열_및_행수제한_desc():
    # given
    row_count = 3
    is_asc = False

    # when
    df = group_by_count(keyword = "자유", asc = is_asc, row = row_count)

    # assert
    assert isinstance(df, pd.DataFrame)
    assert df.iloc[0]['president'] == '윤보선'
    assert len(df) == row_count


def test_wc():
    # given
    row_count = 3
    is_asc = True
    presidents_speeches = {
    "박정희": 513,
    "이승만": 438,
    "노태우": 399,
    "김대중": 305,
    "문재인": 275,
    "김영삼": 274,
    "이명박": 262,
    "전두환": 242,
    "노무현": 230,
    "박근혜": 111,
    "최규하": 14,
    "윤보선": 1
}
    # when
    df = group_by_count(keyword = "자유")
    # assert
    assert isinstance(df, pd.DataFrame)
    assert df.iloc[0]['president'] == '박정희'
    assert len(df) == 12
    
    assert df.iloc[0]['count'] == 513
    assert df.iloc[1]['count'] == 438
    assert df.iloc[11]['count'] == 1
    
    for p_name, s_count in presidents_speeches.items():
        president_row = df[df['president'] ==p_name]
        assert president_row.iloc[0]['count']==s_count
