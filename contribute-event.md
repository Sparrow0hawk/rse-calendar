---
layout: page
title: Add an Event
permalink: /add-event/
---

To add an event to the calendar you should suggest a [pull
request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request?tool=webui)
to the repository that updates the [main data file](https://github.com/Sparrow0hawk/git-calendar-test/edit/main/_data/main.yaml) to add a new
event to the events section with the following YAML format:

```yaml
  - summary: title of your event
    description: |
      A description of your event that can be
      over many lines
    location: A location (virtual or in real life)
    begin: YYYY-mm-DD HH:MM:SS
    # duration should contain a unit of time: minute, day, hour 
    # and an numeric value
    duration: { minutes: 45 }
```

We'll do our best to get to your pull request and merge it so your event is
shown on the website and in the calendar feed.
