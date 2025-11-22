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

