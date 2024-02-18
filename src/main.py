
import click 

from calliope import Model

@click.command()
@click.argument("model_file")
@click.option("--scenario")
@click.option("--override_dict")
def main(model_file, scenario, override_dict):
    model = Model(model_file, scenario=scenario, override_dict=override_dict)
    model.to_csv("workdir/model")
    # TODO: create my own lp model on my own solver using the model data while re-using as much as possible from calliope
    # TODO: solving the model and outputting some form of solution


if __name__ == "__main__":
    main()
        