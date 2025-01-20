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
        Parse the character abbreviation, field name, and changed value from the script.
        """
        abrev = lexer.word()  # Match a word
        
        # Parse the field name (e.g., stamina, hp, etc.)
        field_name = lexer.word()  # Match a word
        if field_name is None:
            lexer.error("Expected a field name (e.g., stamina, hp).")

        # Parse the changed value (e.g., +40, -20)
        changed_value = lexer.float()  # Match a floating-point number
        if changed_value is None:
            lexer.error("Expected a numeric value (e.g., -40, +20).")

        return abrev, field_name, float(changed_value)  # Return abbreviation, field name, and value



    def execute_character(parsed_object):
        """
        Execute the parsed character statement, handling field updates dynamically.
        """
        abrev, field_name, changed_value = parsed_object

        # Resolve the character from the dictionary
        char_obj = characters.get(abrev, None)
        if not char_obj:
            raise Exception(f"Character '{abrev}' is not defined.")

        # Map field names to methods dynamically
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

        # Dynamically call the method on the character object
        try:
            method = getattr(char_obj, method_name)  # Get the method dynamically
            method(abs(changed_value))  # Call the method with the absolute value
        except AttributeError:
            raise Exception(f"Method '{method_name}' not found on character '{abrev}'.")




    # Register the custom statement for specific characters
    renpy.register_statement(
        name="data",
        parse=parse_character,
        execute=execute_character,
        block=False,
    )