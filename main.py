import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def draw_plots():
    df = pd.read_json('deviation.json')
    s = []
    check = []
    for i in df:
        for j in df:
            if i != 'name' and j != 'name' and i != j and {i, j} not in check:  # actually you can check the type of a column but i used 'name' exception
                plt.scatter(df[i], df[j])
                plt.xlabel(i)
                plt.ylabel(j)
                plt.savefig(f"plots/{i}-{j}.png")
                s.append(f"plots/{i}-{j}.png")
                plt.clf()
                check.append({i, j})
    return s


draw_plots()



