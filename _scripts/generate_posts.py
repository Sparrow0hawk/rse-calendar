from jinja2 import Environment, FileSystemLoader, StrictUndefined
import yaml
import os
import logging

LOG_LEVEL = os.environ.get("LOGLEVEL")
logging.basicConfig(level=LOG_LEVEL)

def main():

    with open("_data/main.yaml", "r") as open_file:
        try:

            data = yaml.safe_load(open_file)

        except yaml.YAMLError as err:
            print(err)

    data = data['events']

    env = Environment(
        loader= FileSystemLoader(searchpath="./_scripts"),
        undefined=StrictUndefined
    )

    template = env.get_template("post_template.md.j2")

    for event in data:

        filename = str(event['begin'].strftime("%Y-%m-%d")) + "-" \
            + event['summary'].strip().replace(" ","_")

        output_path = os.path.join("_posts",filename + ".md")

        if os.path.exists(output_path):
            logging.info(f"Skipping rendering {output_path}. It already exists.")
        else:

            rendered = template.render(event)

            with open(output_path, "w") as output_file:
                output_file.write(rendered)


    return 

if __name__ == '__main__':

    main()
