---
name: Add an event template
about: Describe this issue template's purpose here.
title: "[EVENT TITLE]"
labels: add-event
assignees: ''

---

<!-- Please complete the following template to trigger a GitHub action that adds your event as a pull request to the RSE Calendar site. 

See below for some tips about submitting your event:

- The duration field can either be hours, minutes, days. 
- Events should be in the Europe/London timezone, the site currently doesn't support
multiple timezones when displaying events but does build ICalendar files for different timezones.
- If any values include a colon (:) please put that in quotation marks to avoid it being parsed as a
separate YAML field

This section within HTML comment tags is not down when submitting your issue -->

I want to add the following event to the RSE calendar:

```yaml
summary: event title
description: |
    A description of your event
    over multiple
    lines.
    These should all be indented and have the same 
    indentation level as the first line.
    Any URLs should be wrapped in brackets i.e. <www.example.com>
location: A venue
begin: YYYY-mm-DD HH:MM:SS
duration: { minutes: 45 }
event_url: A URL not wrapped in brackets linking to your event page
```
