# git-calendar for $organization

Manage calendar events (converting them to an iCalendar feed, which
can be imported into different calendar programs.  The complied feeds
are available (with instructions) via Github Pages.

## Using the calendars

- You can import these calendars into your own calendar program.
- Visit the GitHub pages site of this repo - this has more
  instructions.
- You can find various calendars available with their descriptions.
  Take the link to the .ics file, and add it by URL to your calendar
  program (instructions are on the page).  This normally appears as a
  separate calendar which you can toggle on and off (you need to copy
  the events to your own calendar to show the time as busy).
- Your calendar program will poll the feed periodically, and any
  updates will appear on your calendar program.  This can be anywhere
  from a few hours to a few days.


## Adding events

- Find the relevant calendar under `calendars/`, to which you will add
  your new event.
- Add your event there
  - Realistically, copy an existing event
  - See the [yaml2ics
    test_calendar](https://github.com/scientific-python/yaml2ics/blob/main/example/test_calendar.yaml)
    as an example.
- Push or create a pull request.


## See also

- https://github.com/coderefinery/git-calendar - the build system
- https://github.com/coderefinery/git-calendar-template - template if
  you want to use this yourself.
- https://github.com/scientific-python/yaml2ics - core tool to convert
  yaml to ics.
