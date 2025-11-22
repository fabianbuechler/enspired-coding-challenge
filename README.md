# enspired coding challenge, Fabian Büchler

## Task

- Company: Apartment And Chair Delivery Limited (AACD)
- Automate reading floor plans and counting number of different chairs
- Output the number of different chair types for apartment and per room
- Total first, rooms sorted alphabetically
- CLI to read floor plan file and print result

### Chair types
- W: wooden
- P: plastic
- S: sofa
- C: china

### Output template
```
total:
W: 3, P: 2, S: 0, C: 0
living room:
W: 3, P: 0, S: 0, C: 0
office:
W: 0, P: 2, S: 0, C: 0
```

### Room plan
- Walls chars: `+-|/\`
- Room names lower case in parenthesis, `\([a-z\s]+\)`, within room
- Chair positions marked as uppercase first char of type, `[WPSC]`

## Architecture

### Entities
- `Apartment`: floor plan, collection of rooms, method to sum chair counts
- `Room`: name, floor plan mask, count of chairs by chair type
- `ChairType`: enum

### Use Case: Parse floor plan
- Convert text file to 2d char array, init apartment floor plan
- Find all room names using regex, remember position at middle of name
- Find all chairs using type char regex, remember position
- Find all rooms by flood-filling the floor plan, identifying islands of non-wall chars
- Create 2d bool array map mask for each room
- Identify rooms by matching room name positions to room map masks
- Assign chairs by matching chair positions to room map masks
- Init and return entities

### Interface Adapters
- Command line controller
  - Triggered by CLI call
  - Read floor plan file
  - Call floor plan parser
- Presenter for legacy system
  - Used by floor plan parser
  - Convert result into output template
  - Pass to CLI output port

## CLI
- Simple argparse CLI, file path as parameter
- Pass file path to command line controller
- Print output of controller
