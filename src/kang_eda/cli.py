from president_speech.db.parquet_interpreter import get_parquet_full_path
import pandas as pd
import typer

def group_by_count(keyword: str, asc: bool, row: int):
    # TODO : ascending, 출력 rows size
    # pytest 코드를 만들어  볼까요
    data_path = get_parquet_full_path()
    df = pd.read_parquet(data_path)
    fdf = df[df['speech_text'].str.contains(keyword, case = False)]
    gdf = fdf.groupby("president").size().reset_index(name = "count")
    sdf = gdf.sort_values(by='count', ascending = asc).reset_index(drop = True)
    print(sdf.head(row).to_string(index = False))

def entry_point():
    typer.run(group_by_count)
