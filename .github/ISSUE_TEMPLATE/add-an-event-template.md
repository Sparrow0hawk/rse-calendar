---
name: Add an event template
about: Describe this issue template's purpose here.
title: "[EVENT TITLE]"
labels: add-event
assignees: ''

---

<!-- Please complete the following template to trigger a GitHub action that adds your event as a pull request to the RSE Calendar site. Please note the duration field can either be hours, minutes, days. This section within HTML comment tags is not down when submitting your issue -->

I want to add the following event to the RSE calendar:

```yaml
summary: event title
description: |
    A description of your event
    over multiple
    lines.
    With URLs wrapped in <www.example.com>
location: A venue
begin: YYYY-mm-DD HH:MM:SS
duration: { minutes: 45 }
event_url: some_url
```
