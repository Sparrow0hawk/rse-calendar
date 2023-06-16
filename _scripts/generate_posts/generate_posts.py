from jinja2 import Environment, FileSystemLoader, StrictUndefined
import yaml
import os
import datetime
import argparse
import logging

LOG_LEVEL = os.environ.get("LOGLEVEL")
logging.basicConfig(level=LOG_LEVEL)


def main(override=False):
    with open("_data/main.yaml", "r") as open_file:
        try:
            data = yaml.safe_load(open_file)

        except yaml.YAMLError as err:
            print(err)

    data = data["events"]

    env = Environment(
        loader=FileSystemLoader(searchpath="./_scripts/generate_posts"),
        undefined=StrictUndefined,
    )

    template = env.get_template("post_template.md.j2")

    today = datetime.datetime.today()

    for event in data:

        # calculate a post end date 
        postEndDate = event["begin"] + datetime.timedelta(**event["duration"])

        if postEndDate >= today:
            filename = (
                str(event["begin"].strftime("%Y-%m-%d"))
                + "-"
                + event["summary"].strip().replace(" ", "_")
            )

            output_path = os.path.join("_posts", filename + ".md")

            if (os.path.exists(output_path)) & (~override):
                logging.info(f"Skipping rendering {output_path}. It already exists.")
            else:
                rendered = template.render(event)

                with open(output_path, "w") as output_file:
                    output_file.write(rendered)

    return


if __name__ == "__main__":
    parser = argparse.ArgumentParser("RSE Events page post generator")
    parser.add_argument("--override", action="store_true")
    args = parser.parse_args()

    main(override=args.override)
