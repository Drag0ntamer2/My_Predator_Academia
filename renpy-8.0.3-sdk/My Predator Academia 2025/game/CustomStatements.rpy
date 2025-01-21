python early:
    characters = {}  # Global dictionary to store character objects

    def parse_random(lexer):
        """
        Parse the random statement with weighted options.
        """
        # Get a lexer for the subblock of this statement
        subblock_lexer = lexer.subblock_lexer()

        # List to store parsed choices
        choices = []

        # Default weight
        weight = 1

        # Process each line in the subblock
        while subblock_lexer.advance():
            with subblock_lexer.catch_error():
                if subblock_lexer.keyword("weight"):  # Check for "weight" keyword
                    # Parse the weight
                    weight_str = subblock_lexer.integer()
                    if weight_str is not None:
                        # Convert the weight to an integer
                        weight = int(weight_str)
                    else:
                        # If "weight" is specified but no number is given, raise an error
                        subblock_lexer.error("Expected an integer after 'weight'.")
                else:
                    # Parse the line as a Ren'Py statement
                    statement = subblock_lexer.renpy_statement()

                    # Append the statement with the current weight
                    choices.append((weight, statement))

                    # Reset the weight to the default for subsequent lines
                    weight = 1

        return choices

    def next_random(choices):
        """
        Select a random statement based on weights.
        """
        import random

        # Calculate the total weight
        total_weight = sum(weight for weight, _ in choices)

        # Choose a random number between 1 and the total weight
        pick = random.uniform(0, total_weight)

        # Iterate through choices and pick based on weight
        cumulative_weight = 0
        for weight, statement in choices:
            cumulative_weight += weight
            if pick <= cumulative_weight:
                return statement

    def lint_random(parsed_object):
        """
        Lint the parsed object for errors.
        """
        for weight, statement in parsed_object:
            # Check for any text tag errors in the statement
            check = renpy.check_text_tags(statement.block[0].what)
            if check:
                renpy.error(check)

    # Register the statement
    renpy.register_statement(
        name="random",
        block=True,
        parse=parse_random,
        next=next_random,
        lint=lint_random,
    )

        
    
    def parse_character(lexer):
        """
        Parse the character abbreviation, field name, action, and value from the script.
        """
        # Parse the character abbreviation
        abrev = lexer.word()
        if abrev is None:
            lexer.error("Expected a character abbreviation (e.g., 'jes').")

        # Parse the field name
        field_name = lexer.word()
        if field_name is None:
            lexer.error("Expected a field name (e.g., stamina, hp).")

        # Parse the rest of the line
        temp = lexer.rest().strip()  # Remove leading/trailing whitespace

        # Extract the action (first character of temp) and remaining value
        action = temp[0]  # First character is the action ('=', '+', or '-')
        if action not in "=+-":
            lexer.error("Expected an action ('=', '+', or '-').")

        # Parse the numeric value (remaining part of the line)
        try:
            changed_value = float(temp[1:].strip())  # Convert the rest to a float
        except ValueError:
            lexer.error("Expected a numeric value (e.g., -40, +20).")

        return abrev, field_name, action, changed_value




    def execute_character(parsed_object):
        """
        Execute the parsed character statement, handling field updates dynamically.
        """
        abrev, field_name, action, changed_value = parsed_object

        # Resolve the character from the dictionary
        char_obj = characters.get(abrev, None)
        if not char_obj:
            raise Exception(f"Character '{abrev}' is not defined.")

        try:
            if action in "+-":
                # Handle additive/subtractive updates
                method_name = None
                if field_name == "stamina":
                    method_name = "addStam" if changed_value > 0 else "loseStam"
                elif field_name == "hp":
                    method_name = "addHp" if changed_value > 0 else "loseHp"
                elif field_name == "dis":
                    method_name = "addDis" if changed_value > 0 else "disDecay"
                elif field_name == "arousal":
                    method_name = "addArousal" if changed_value > 0 else "arousalDecay"
                elif field_name == "compression":
                    method_name = "addComp" if changed_value > 0 else "loseComp"
                elif field_name == "shp":
                    method_name = "addShp" if changed_value > 0 else "loseShp"
                else:
                    raise Exception(f"Unsupported field name: '{field_name}'.")

                # Dynamically invoke the method
                method = getattr(char_obj, method_name)
                method(abs(changed_value))  # Pass the absolute value to the method

            elif action == '=':
                # Handle assignment
                if hasattr(char_obj, field_name):
                    setattr(char_obj, field_name, changed_value)  # Directly set the field value
                else:
                    raise Exception(f"Field '{field_name}' does not exist on character '{abrev}'.")

        except AttributeError as e:
            raise Exception(f"Error processing '{field_name}': {str(e)}")


    # Register the custom statement
    renpy.register_statement(
        name="data",
        parse=parse_character,
        execute=execute_character,
        block=False,
    )
