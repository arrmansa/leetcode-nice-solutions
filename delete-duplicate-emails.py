import pandas as pd

def delete_duplicate_emails(person: pd.DataFrame) -> None:
    needed_index = person.groupby('email')['id'].idxmin()
    idx_to_drop = person.index.difference(needed_index)
    person.drop(idx_to_drop, inplace=True)
