from president_speech.db.parquet_interpreter import get_parquet_full_path
import pandas as pd
from tqdm import tqdm
import time
import typer

def add_keyword_count(df: pd.DataFrame, keyword: str) -> pd.DataFrame:
    """
    DataFrame에 keyword_count 컬럼을 추가하여 반환합니다.
    각 speech_text에서 keyword가 등장하는 횟수를 계산합니다.
    """
    # keyword_count 컬럼 추가
    df['keyword_count'] = df['speech_text'].str.count(keyword)
    return df

def group_by_count(keyword: str, asc: bool=False, row: int=12,keyword_sum: bool=False) -> pd.DataFrame:
    data_path = get_parquet_full_path()
    df = pd.read_parquet(data_path)
    fdf = df[df['speech_text'].str.contains(keyword, case = False)]

    if(keyword_sum):
        fdf = add_keyword_count(fdf.copy(), keyword)
        gdf = fdf.groupby("president").agg(
                count = ("speech_text", 'size'), # 연설 개수  
                keyword_sum = ("keyword_count", 'sum') # keyword 발생 횟수 합산 
                )
        sdf = gdf.sort_values(by=["keyword_sum", "count"], ascending = [asc, asc]).reset_index()
    else:
        gdf = fdf.groupby("president").size().reset_index(name = "count")
        sdf = gdf.sort_values(by='count', ascending = asc).reset_index(drop = True)
    
    rdf = sdf.head(row)
    return rdf

def print_group_by_count(keyword: str, asc: bool=False, row: int=12, keyword_sum: bool = False):
    df = group_by_count(keyword, asc, row, keyword_sum)
    # 프로그래스바 추가 -  df 의 컬럼 숫자 * row 숫자 +sleep
    r = len(df.columns) * len(df)
    for i in tqdm(range(r)):
        time.sleep(0.1)
    hs2 = df.columns
    from tabulate import tabulate
    t = tabulate(df, headers= hs2 ,tablefmt = 'github')
    print(t)

    # hs = ['president', 'count']
    # if keyword_sum:
    # hs.append("keyword_sum")
    #print(df.to_string(index = False))
#       print(tabulate(df))
    import termplotlib as tpl
    fig = tpl.figure()

    fig.barh(df['count'],df['president'], force_ascii = True)
    fig.show()

    ## TODO = keyword_sum이 활성화 되면 keyword_sum 들어가게 하
    if keyword_sum:
        fig.barh(df['count'],df['president'], force_ascii = True)
        fig.show()

    

def entry_point():
    typer.run(print_group_by_count)
