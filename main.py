import pandas as pd


def compare_environments():
    """Compare two files each containing all the packages of an environment."""
    base_file = 'base.txt'
    machine_learning_project_file = 'list_machine-learning-project.txt'

    df_base = make_df(base_file)
    df_machine = make_df(machine_learning_project_file)

    diff = df_base.merge(right=df_machine, on='Name', how='left', indicator=True)
    diff.to_excel('diff.xlsx', index=False)
    for idx, x in enumerate(diff.itertuples(index=False)):
        print(f'{idx:>5} {x}')
    

def make_df(file: str) -> pd.DataFrame:
    """Create dataframe from file.
    - base_file : file where are stored data\n
    Return a dataframe.
    """
    f = open(file=file, mode="r")
    file_content = f.read()
    file_content_list = file_content.split(sep='\n')
    file_content_list.pop(0)
    file_content_list.pop(0)
    splited_list = []
    for idx, x in enumerate(file_content_list):
        if len(x):
            splited_list.append(x.split())
        if idx == 0:
            splited_list[0].pop(0)

    df = pd.DataFrame(data=splited_list)
    df.columns = df.iloc[0]
    df = df[1:]
    return df


if __name__ == "__main__":
    compare_environments()
