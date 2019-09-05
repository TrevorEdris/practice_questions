# Ratio Finder

[Link to source](https://medium.com/@alexgolec/google-interview-problems-ratio-finder-d7aa8bf201e3)

## Question

Given a list of conversion rates (formatted in the language of your choice) as a collection of origin unit, destination unit, and multiplier,
for example:

```txt
foot inch 12
foot yard 0.3333333
etc…
```

Such that `ORIGIN * MULTIPLIER = DESTINATION`, design an algorithm that takes two arbitrary unit values and returns the conversion rate between them.

## Solution

_See the source article for detailed explanation_

## Usage

```txt
$ python main.py -h
usage: main.py [-h] [-i INPUT] origin_value origin_unit dest_unit

positional arguments:
  origin_value          The value to convert
  origin_unit           The starting unit
  dest_unit             The unit to convert to

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        Full filepath to the input file
```

## Example

```txt
$ python main.py 1 light_year hand
1.0 light_year converted to hand = 9.3117492373e+16
```
