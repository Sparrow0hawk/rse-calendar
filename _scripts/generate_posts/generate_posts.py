from jinja2 import Environment, FileSystemLoader, StrictUndefined
import yaml
import os
import datetime
import argparse
import logging

LOG_LEVEL = os.environ.get("LOGLEVEL")
logging.basicConfig(level=LOG_LEVEL)


def main(override=False):

    NoDatesSafeLoader.remove_implicit_resolver('tag:yaml.org,2002:timestamp')

    with open("_data/main.yaml", "r") as open_file:
        try:
            data = yaml.load(open_file, Loader = NoDatesSafeLoader)

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

class NoDatesSafeLoader(yaml.SafeLoader):
    """
    Copied under CC-BY-SA 3.0
    https://stackoverflow.com/a/37958106/10651182
    """
    @classmethod
    def remove_implicit_resolver(cls, tag_to_remove):
        """
        Remove implicit resolvers for a particular tag

        Takes care not to modify resolvers in super classes.

        We want to load datetimes as strings, not dates, because we
        go on to serialise as json which doesn't have the advanced types
        of yaml, and leads to incompatibilities down the track.
        """
        if not 'yaml_implicit_resolvers' in cls.__dict__:
            cls.yaml_implicit_resolvers = cls.yaml_implicit_resolvers.copy()

        for first_letter, mappings in cls.yaml_implicit_resolvers.items():
            cls.yaml_implicit_resolvers[first_letter] = [(tag, regexp) 
                                                         for tag, regexp in mappings
                                                         if tag != tag_to_remove]


if __name__ == "__main__":
    parser = argparse.ArgumentParser("RSE Events page post generator")
    parser.add_argument("--override", action="store_true")
    args = parser.parse_args()

    main(override=args.override)
