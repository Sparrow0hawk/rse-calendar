---
layout: page
title: Add an Event
permalink: /add-event/
---

The calendar site is designed to show events only in one timezone (currently
[Europe/London](https://www.zeitverschiebung.net/en/timezone/europe--london)).
The ICalendar files built as part of the site deployment do support multiple
timezones but when contributing an event it's important to ensure you contribute
your events with times adjusted for [Europe/London](https://www.zeitverschiebung.net/en/timezone/europe--london).

There are 2 main ways to contribute an event to the calendar:

- [Using GitHub Issues Template](#submit-using-github-issues)
- [Submit as a pull request](#submit-an-event-via-a-pull-request)

### Submit using GitHub Issues

You can use the [Add event GitHub Issue
template](https://github.com/Sparrow0hawk/rse-calendar/issues/new?assignees=&labels=add-event&projects=&template=add-an-event-template.md&title=%5BEVENT+TITLE%5D)
to submit an issue that includes a yaml block with details of your event.
This will trigger a GitHub action workflow that automatically submits a pull request
with your event details to the project. Allowing you to contribute an event
without touching any code!

When submitting using the GitHub issue you should ensure:

- If any field you enter contains a colon, you should wrap the field in
  quotation marks to avoid the YAML parser interpreting the colon as a new key
  i.e.

  ❌ `event_url: https://www.example.com`

  ✅ `event_url: "https://www.example.com"`
- If you enter a field over multiple lines like the description field make sure
  the indentation level is the same across all lines
  i.e.
  ```yaml
  ❌  description: |
              My fantastic event
            is going to be
          amazing!

  ✅ description: |
              My fantastic event
              is going to be
              amazing!
  ```

### Submit an event via a pull request

To add an event to the calendar you can suggest a [pull
request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request?tool=webui)
to the repository that updates the [main data file](https://github.com/Sparrow0hawk/git-calendar-test/edit/main/_data/main.yaml) to add a new
event to the events section with the following YAML format:

```yaml
- summary: title of your event
  description: |
    A description of your event
    over multiple
    lines.
    These should all be indented and have the same 
    indentation level as the first line.
    Any URLs should be wrapped in brackets i.e. <www.example.com>
  location: A location (virtual or in real life)
  begin: YYYY-mm-DD HH:MM:SS
  # duration should contain a unit of time: minute, day, hour 
  # and an numeric value
  duration: { minutes: 45 }
  event_url: A URL not wrapped in brackets linking to your event page 
```

We'll do our best to get to your pull request and merge it so your event is
shown on the website and in the calendar feed.
