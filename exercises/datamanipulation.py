def process_data():
    # Do not alter this line.
    biopics = pd.read_csv("biopics.csv", encoding='latin-1')
    # Write your code here.
    # filter duplicated rows
    biopics= biopics.drop_duplicates()
    # rename variable box office to earnings
    biopics = biopics.rename(columns={"box_office":"earnings"})
    # for rows where earnings null, filter out
    # drop na used
    biopics = biopics[biopics["earnings"].notna()]
    # only movies released in >1990
    biopics = biopics[biopics["year_release"]>=1990]
    # convert 2 col type to categorical
    biopics["type_of_subject"] = biopics["type_of_subject"].astype("category")
    biopics["country"] = biopics["country"].astype("category")
    # new variable 
    biopics["lead_actor_actress_known"] = np.where(biopics["lead_actor_actress"].isna(), False, True)
    # update earnings to millions of dollars
    biopics["earnings"] = biopics["earnings"] /1000000
    #reorder columns
    biopics = biopics[["title","year_release", "earnings","country","type_of_subject","lead_actor_actress", "lead_actor_actress_known"]]
    # sort rows by earnings desc
    biopics = biopics.sort_values(by="earnings", ascending=False)

    # Remember to return the right object.
    return biopics.reset_index(drop=True)