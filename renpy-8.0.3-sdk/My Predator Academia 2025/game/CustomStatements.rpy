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

        


    def parse_character(abrev, lexer):
        """
        Parse the character abbreviation and dialogue text from the script.
        """
        amt = None
        dialogue = None

        # Check for the keyword "change arousal" and parse accordingly
        if lexer.keyword("change"):
            if lexer.keyword("arousal"):
                amt = float(lexer.float())  # Parse the float value
                if amt < 0:
                    dialogue = "arousalDecay"  # Negative values correspond to decay
                else:
                    dialogue = "addArousal"   # Positive values correspond to addition
            elif lexer.keyword("stamina"):
                amt = float(lexer.float())  # Parse the float value
                if amt < 0:
                    dialogue = "loseStam"  # Negative values correspond to decay
                else:
                    dialogue = "addStam"   # Positive values correspond to addition
        else:
            dialogue = lexer.rest()  # Parse the rest as standard dialogue

        return abrev, dialogue, amt  # Return abbreviation, dialogue, and amount

    def execute_character(parsed_object):
        """
        Execute the parsed character statement.
        """
        abrev, dialogue, amt = parsed_object

        # Resolve the character from the dictionary
        char_obj = characters.get(abrev, None)
        if not char_obj:
            raise Exception(f"Character '{abrev}' is not defined.")

        if amt is not None:
            # Dynamically call the method on the character object
            try:
                method = getattr(char_obj, dialogue)  # Get the method dynamically
                method(amt)  # Call the method with the amount
            except AttributeError:
                raise Exception(f"Method '{dialogue}' not found on character '{abrev}'.")
            return

        # If no amount is provided, treat as standard dialogue
        return renpy.exports.say(char_obj.c, dialogue)

    # Register a custom statement for a specific character (example: 'jes')
    renpy.register_statement(
        name="jes",
        parse=lambda lexer: parse_character("jes", lexer),  # Corrected parse function
        execute=execute_character,
        block=False,  # No block associated with this statement
    )
    renpy.register_statement(
        name="sof",
        parse=lambda lexer: parse_character("sof", lexer),  # Corrected parse function
        execute=execute_character,
        block=False,  # No block associated with this statement
    )
    renpy.register_statement(
        name="mer",
        parse=lambda lexer: parse_character("mer", lexer),  # Corrected parse function
        execute=execute_character,
        block=False,  # No block associated with this statement
    )
    renpy.register_statement(
        name="lea",
        parse=lambda lexer: parse_character("lea", lexer),  # Corrected parse function
        execute=execute_character,
        block=False,  # No block associated with this statement
    )
    renpy.register_statement(
        name="fel",
        parse=lambda lexer: parse_character("fel", lexer),  # Corrected parse function
        execute=execute_character,
        block=False,  # No block associated with this statement
    )
    renpy.register_statement(
        name="ash",
        parse=lambda lexer: parse_character("ash", lexer),  # Corrected parse function
        execute=execute_character,
        block=False,  # No block associated with this statement
    )
    renpy.register_statement(
        name="yul",
        parse=lambda lexer: parse_character("yul", lexer),  # Corrected parse function
        execute=execute_character,
        block=False,  # No block associated with this statement
    )
    renpy.register_statement(
        name="ste",
        parse=lambda lexer: parse_character("ste", lexer),  # Corrected parse function
        execute=execute_character,
        block=False,  # No block associated with this statement
    )
    renpy.register_statement(
        name="ast",
        parse=lambda lexer: parse_character("ast", lexer),  # Corrected parse function
        execute=execute_character,
        block=False,  # No block associated with this statement
    )
