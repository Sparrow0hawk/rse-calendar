# RSE Calendar project

This repository contains code for building a Jekyll site that shows upcoming
events and builds and hosts .ics calendar files of those events that can be
subscribed to. It was built with the idea of providing a central website
containing research software engineering events in the UK that can be
contributed to easily.

## Contributing an event to the calendar

To add an event to the calendar you should suggest a [pull
request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request?tool=webui)
to the repository that updated the [main data file](./_data/main.yaml) to add a new
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


## Acknowledgements

This projects builds on:

- The coderefinery [git-calendar tool](https://github.com/coderefinery/git-calendar-template)
- Themes from [Jekyll minima](https://github.com/jekyll/minima)
>  # git-calendar for $organization
>
>  Manage calendar events (converting them to an iCalendar feed, which
>  can be imported into different calendar programs.  The complied feeds
>  are available (with instructions) via Github Pages.
>
>  ## Using the calendars
>
>  - You can import these calendars into your own calendar program.
>  - Visit the GitHub pages site of this repo - this has more
>    instructions.
>  - You can find various calendars available with their descriptions.
>    Take the link to the .ics file, and add it by URL to your calendar
>    program (instructions are on the page).  This normally appears as a
>    separate calendar which you can toggle on and off (you need to copy
>    the events to your own calendar to show the time as busy).
>  - Your calendar program will poll the feed periodically, and any
>    updates will appear on your calendar program.  This can be anywhere
>    from a few hours to a few days.
>
>
>  ## Adding events
>
>  - Find the relevant calendar under `calendars/`, to which you will add
>    your new event.
>  - Add your event there
>    - Realistically, copy an existing event
>    - See the [yaml2ics
>      test_calendar](https://github.com/scientific-python/yaml2ics/blob/main/example/>test_calendar.yaml)
>      as an example.
>  - Push or create a pull request.
>
>
>  ## See also
>
>  - https://github.com/coderefinery/git-calendar - the build system
>  - https://github.com/coderefinery/git-calendar-template - template if
>    you want to use this yourself.
>  - https://github.com/scientific-python/yaml2ics - core tool to convert
>    yaml to ics.
>
