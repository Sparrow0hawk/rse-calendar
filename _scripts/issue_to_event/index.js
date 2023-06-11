const fs = require('fs');
const yaml = require('yaml');

// Get the JSON string from the command line argument
const payload = process.argv[2];

try {
    // Parse the JSON string into an object
    const payload_json = JSON.parse(payload);

    // Check if the file exists
    const file_path = '_data/main.yaml';
    const file_exists = fs.existsSync(file_path);

    if (file_exists) {
        // Read the existing YAML file
        const events_yaml_str = fs.readFileSync(file_path, 'utf8');

        // Parse the existing YAML into an object
        const events_yaml = yaml.parseDocument(events_yaml_str);

        // add a new event by editing the events prop
        events_yaml.addIn(["events"], events_yaml.createNode(payload_json))

        // Convert the merged object to YAML
        const merged_events = yaml.stringify(events_yaml, options = { lineWidth: 0 });

        // Write the merged YAML string back to the file
        fs.writeFileSync(file_path, merged_events);

        console.log('YAML entry appended successfully to _data/main.yaml');
    } else {
        // Write the YAML string to a new file
        fs.writeFileSync(file_path, events_yaml_str);

        console.log('Created new file _data/main.yaml with the YAML entry');
    }
} catch (error) {
    console.error('Error converting JSON to YAML:', error);
}
