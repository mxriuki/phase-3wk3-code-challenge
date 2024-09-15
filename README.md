# Object Relations Code Challenge - Concerts

For this assignment, we'll be working with a Concert domain.

We have three models: `Band`, `Concert`, and `Venue`.

For our purposes, a `Band` has many `Concerts`, a `Venue` has many `Concerts`s, and a `Concert` belongs to a `Band` and to a `Venue`.

`Band` - `Venue` is a many to many relationship.

**Note**: You should draw your domain on paper or on a whiteboard _before you start coding_. Remember to identify a single source of truth for your data.

## Topics

- Classes and Instances
- Class and Instance Methods
- Variable Scope
- Object Relationships
- lists and list Methods

## Instructions

To get started, run `pipenv install; pipenv shell` while inside of this
directory.

Build out all of the methods listed in the deliverables. The methods are listed
in a suggested order, but you can feel free to tackle the ones you think are
easiest. Be careful: some of the later methods rely on earlier ones.

**Remember!** This code challenge has `pytest` tests available to you. Run
`pytest` at any time from within your virtual environment.

We've provided you with another tool that you can use to test your code. To use
it, run `python debug.py` from the command line. This will start a `ipdb`
session with your classes defined. You can test out the methods that you write
here. You can add code to the `debug.py` file to define variables and create
sample instances of your objects.

Writing error-free code is more important than completing all of the
deliverables listed - prioritize writing methods that work over writing more
methods that don't work. You should test your code in the console as you write.

Similarly, messy code that works is better than clean code that doesn't. First,
prioritize getting things working. Then, if there is time at the end, refactor
your code to adhere to best practices. When you encounter duplicated logic,
extract it into a shared helper method.

**Before you submit!** Save and run your code to verify that it works as you
expect. If you have any methods that are not working yet, feel free to leave
comments describing your progress.

***

## Deliverables

Write the following methods in the classes in the files provided. Feel free to
build out any helper methods if needed.

> **Note: all setters should raise `Exception` if their criteria are not met.**

### Initializers, Readers, and Writers

#### Band

- `Band __init__(name, hometown)`
  - should initialize with a name (string) and hometown (string)
- `Band property name()`
  - should return the `Band`'s name
  - must be a string of greater than zero characters
- `Band property hometown()`
  - should return the `Band`'s hometown
  - must be a string of greater than zero characters

#### Venue

- `Venue __init__(title, city)`
  - should initialize with a title (string) and city (string)
- `Venue property title()`
  - should return the title of the venue
  - must be a string of greater than zero characters
- `Venue property city()`
  - should return the city of the venue
  - must be a string of greater than zero characters

#### Concert

- `Concert __init__(self, date, band, venue)`
  - should initialize with a date (string), band, and venue
  - date must be a string of greater than zero characters

### Object Relationship Methods and Attributes

#### Concert

- `Concert band`
  - should return the `Band` instance for this concert
- `Concert venue`
  - should return the `Venue` instance for this concert

#### Venue

- `Venue concerts`
  - returns a list of all the concerts for the venue
- `Venue bands`
  - returns a list of all the bands for the venue

#### Band

- `Band property concerts`
  - should return a list of all the concerts that the band has played in

### Aggregate Methods

#### Concert

- `Concert hometown_show()`
  - returns `true` if the concert is in the band's hometown, `false` if it is not
- `Concert introduction()`
  - returns a string with the band's introduction for this concert
  - an introduction is in the form: `"Hello {insert city name here}!!!!!, we are {insert band name here} and we're from {insert hometown here}"`

#### Band

- `Band play_in_venue(venue, date)`
  - takes a venue and date (as a string) as arguments, and creates a new concert for the band in that venue on that date
- `Band all_introductions()`
  - returns a list of strings representing all the introductions for this band
  - each introduction is in the form `"Hello {insert city name here}!!!!!, we are {insert band name here} and we're from {insert hometown here}"`

#### Venue

- `Venue concert_on(date)`
  - takes a date (string) as argument
  - finds and returns the first concert on that date at that venue
  - if there is no concert on that date at that venue, returns `None`
