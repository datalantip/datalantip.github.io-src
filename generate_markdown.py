from jinja2 import Environment, FileSystemLoader
import os
import numpy as np
import pandas as pd
import pathlib

BASE_PATH = pathlib.Path(__file__).parent.resolve()
DATA_PATH = BASE_PATH.joinpath("data").resolve()
CHARTS_PATH = BASE_PATH.joinpath("chartjs_templates").resolve()


def create_dataframe(filename="data/pengeluaran-sayur-sebulan-jateng.csv"):
    """Create Pandas DataFrame from local CSV."""
    """ Persentase Pengeluaran per Kapita Sebulan Jawa Tengah 2018-2021 """
    df = pd.read_csv(filename)
    return df

def generate_markdown(template_filename='pengeluaran-sayur-sebulan-jateng.jinja2', dataframe=pd.DataFrame()):
    root = os.path.dirname(os.path.abspath(__file__))
    templates_dir = os.path.join(root, 'chartjs_templates')
    env = Environment( loader = FileSystemLoader(templates_dir) )
    template = env.get_template(template_filename)
     
     
    filename = os.path.join(root, 'content', template_filename.replace('.jinja2','.md'))
    with open(filename, 'w') as fh:
        fh.write(template.render(
            x_values = dataframe[dataframe.columns[0]],
            y_values = dataframe[dataframe.columns[1]]
        ))

if __name__ == '__main__':

    for subdir, dirs, files in os.walk(str(CHARTS_PATH)):
        for file in sorted(files):
            print("# Generating Markdown from {} ...".format(file))
            data_path = str(DATA_PATH.joinpath(file.replace('.jinja2','.csv')))
            generate_markdown(file,create_dataframe(data_path))
            print("## {} is generated".format(file.replace('.jinja2','.md')))
