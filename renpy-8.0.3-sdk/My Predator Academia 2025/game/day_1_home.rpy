label Day1_start:
    scene room day at fill_screen with dissolve # show the room background 
    "The day is quiet as the light buzz of a phone alarm sounds off around you, muffled by several layers of blankets and clothes on the bed."
    "The air is nice and brisk as you begin to breath in deeply and try to stretch and sprawl out of the bed in an attempt to further escape the tempting clutches of its soft covers." 
    "Birds faintly chirp just outside the window as the rising sun's light begins to peer through the window like a spotlight, creeping slowly but steadily into your direction."
    "The brisk air, the soft, warm bed, and lazy Monday morning fills your young 22-year-old mind as you groggily open your eyes..." 
    "you begin to see the cyan painted wall peppered with posters of many kinds before you and the state of your room."
    "The floor is somewhat disorderly with clothes laid about lazily on a dirty clothes basket against the wall with a sock next to it, a small trash pile filled with used tissues from the recent flu season."
    "The idealistic posters depicting somewhat sexy pro heroes saying to do your best with a colorful backdrop providing a muted irony to the disorganized piles of paper and random Knick Knacks that lay within just few feet of them."
    "If you can listen closely, you can swear that a car blaring a gas advertisement in Spanish in the far distance along a nearby residential street..."
    menu: 
        "Sleep In":
            jump Day1_sleep_in
        "Find Your Phone & Scroll Through The News":
            jump Day1_scroll_news
        "Get Out Of Bed":
            jump Day1_get_up


label Day1_sleep_in:
    # unfinished


label Day1_scroll_news:
    # unfinished


label Day1_get_up:
    "You get out of bed and begin getting dressed for the day, slipping into some generic casual clothes and grabbing your wallet."
    "and... you don't see your phone..." 
    jes "{i}Crap, I forgot to charge it didn't I{/i}"
    "You look through the area surrounding your nightstand and under your blankets, where you eventually find it."
    "Looking at the glowing screen, you see the date: {i}Sunday, 1/16{/i}"
    if loop is 0:
        "Only a few days left until the hero entrance exam, and you {i}still{/i} have no idea what your quirk is."
        jes "This week's gonna be real tough."
    scene living room day at fill_screen with dissolve
    $ Jessie_Has_His_Wallet = True
    "You slip it into your pocket, grab your wallet and keys off your nightstand, and walk out the door, entering a hallway with a couple other doors in it that opens into the living room."
    scene kitchen day at fill_screen with dissolve
    "You make your way into the kitchen, which is connected to the living room on the right side by an arched entryway (one of those door-shaped openings without doors in them), and slip some toast into the toaster."
    "While it's toasting, your sister walks into the room, pajamas on, and hair in a mess."
    show merry sass at centerZoom5 with dissolve
    "Merry, despite being a rather energetic girl, was certainly not a morning person, and generally was never fully functional 'till an hour or two after waking up."
    "Her hair being a mess wasn't exactly anything new either, she never really took remotely as much care in looking pristine as a typical girl might, she was something of a tomboy in that sense."
    "Groggily waltzing in, and still half asleep, Merry drops like a pillow at the kitchen table, slumped over with her upper body lain against the tabletop."
    "She speaks up with a hint of a whine,"
    mer morning tired "Jessieee... Gimme some toast and OJ..."
    "She lifts both arms up, making grabby motions with her hands in the air at you, clearly accentuating her desire for food and fruit juice."
    mer "Cmoonnn, hurry up already or I'll settle for you..."
    menu:
        "Give In & Feed The Brat.":
            jump Day1_make_merry_breakfast
        '"Make your own breakfast, dork."':
            jump Day1_tell_merry_to_make_own_breakfast
        "Take Her Up On Her Threat":
            jump Day1_offer_self_as_merrys_breakfast


label Day1_make_merry_breakfast:
    "You know she was {i}mostly{/i} joking about that last part, but you get the feeling that she'd hapiliy follow through on it if you push her, so you give her what she wants."
    "She wouldn't digest you, of course, at least not permanently, but the idea of being eaten by your sister just feels weird."
    "Even if it would be entirely non-sexual from her perspective, but as a young man, it would be impossible for you to avoid getting {i}certain feelings{/i} from being {i}that{/i} close to a girl with her proportions."
    "Once it pops up, you take the toast, which you'd initially planned on eating yourself, and toss it over to her."
    "It slides across the table, bouncing into her waiting mouth before you put a new pair of slices into the toaster for yourself."
    "While it's toasting, you grabb her the juice she asked for."
    "Merry didn't even acknowledge the juice, her eyes still shut as she munched on the toast, not even using her hands to hold it, simply chewing with the thing still protruding out her mouth, causing the thing to flop up and down in rhythm with her jaw."
    "You hear what vaguely sounds like a 'thank you' from her stuffed face, but frankly it was totally unintelligible amongst the happy munching 'Mmm' noises she was making."
    "After a few seconds of chewing, she lazily opens her eyes halfway as she looks at you, mouth still full of toast," 
    mer "O, rh ou ona oo aht aka-emmy hing e..?"
    "totally unintelligible... Typical Merry..."    
    "You take a minute to try to parse through what she was trying to say."
    "Eventually you land on it being something along the lines of 'So, are you gonna do that academy thingy?'"
    jes "Mhm. I know I probably won’t get in, but it’s not like it hasn’t happened before."
    "Your toast pops up, so you spread butter on it and begin eating."
    "Seeing the unconvinced look in her eyes, you continue,"
    jes "C'mon, I know I've explained this to you before! It's not entirely based on having a good quirk, there's also skill and intelligence involved."
    jes "Yes, it's a battle royale type thing, but all I need is one good showing."
    jes "There'd be plenty of cover, and I could find someone else who's quirk is not combat oriented, show some creative tactics, and I'll have a real shot at getting in!"
    "She stares at you, maintaining her unimpressed expression as the toast slowly disappeared between her lips like a CD into a disc reader."
    "After a second, she smiles smugly and begins to speak,"
    mer "Five bucks says you don't even make it {i}to{/i} the test solid."
    mer "I bet you'll be titty mush before you make it onto school grounds." 
    mer "Anyways, are you sure you're even cut out for being a hero?"
    mer "I've seen videos of them at work online, and they go up against some freaky motherfuckers..." 
    "She pauses, looking aside for a moment before continuing with her voice a little quieter,"
    mer "I'm a little worried you'll go out and get totally pancaked by some lunatic, we both know your quirk is bogus, you're functionally quirkless y'know..."
    "With that, she lifts herself up to sit properly, still leaning on the table with her elbow, holding up her head with a sort of distant expression."
    "Then, a smug smile creeps up her lips, and she looks back at you,"
    mer "Y'know, if you're so intent on becoming a hero despite knowing you'll just fill out some psycho's top measurements, I can help you expedite the end goal~"
    "She opens her maw wide, giving a little playful tongue wiggle to mess with you, before snapping it shut in a toothy grin."
    menu:
        "'Thanks for the encouragement...'":
            jump Day1_TBD
        "'I'll show you.'":
            jump Day1_TBD
        "'I'll take you up on that offer!'":
            jump Day1_accept_merrys_offer_to_eat_you


label Day1_tell_merry_to_make_own_breakfast:
    # unfinished


label Day1_offer_self_as_merrys_breakfast:
    # unfinished


label Day1_accept_merrys_offer_to_eat_you:
    "You think her words over for a second, and an idea comes to your mind. It's a stupid idea, so you try to shove it back down."
    jes "{i}Don't do it, you'll regret it!{/i}"
    "Eventually, however, against your better judgement, you decide to play along, and tease her back." 
    jes "You'd really do that for me?"  
    jes "{i}Crap! that came out too genuine sounding!{/i}"
    "There is a moment of silence between the two of you as you stare at each other." 
    "Merry looks at you intently, eyebrows raised, as your brain scrambles to find a way out of this situation."
    "After a minute of silence she grins ear to ear, as her eye's close halfway in a smug expression."
    # show merry smug with dissolve
    "She climbs out of her chair and begins walking over to you, giving you a great view of her figure which she'd built up with many {i}former{/i} men much bigger and stronger than you,"
    "Her big tits were enough of a warning to her experience with vore."
    "She stops in front of you with her hand thrust against the wall, pinning you against it." 
    "She brings a hand up to your chin, lifting it up to straighten your gaze into her maw as it opens wide."
    hide merry with dissolve
    scene mouth at fill_screen with dissolve
    "As she leans in, you see nothing but an abyss before you."
    scene kitchen day at fill_screen with dissolve
    show merry sass at centerZoom5 with dissolve
    "Just before you begin your journey to your sister's waistline, however, her lips snap shut less than an inch in front of your face."
    "She kisses you on the forehead before letting off you with a impish smile,"
    mer morning sass "Gosh that 5 dollars might be sooner in my future than I thought~" 
    "She grins devilishly at you, before spinning something on her fingertip, and as she stopps it and grips it properly, you see that it's your wallet..."
    $ Jessie_Has_His_Wallet = False
    mer "I'll hold onto this to make sure I get my Five bucks undigested when you inevitably end up padding out some chicks bra."
    mer "Oh! But before she liquifies you make sure to get her number and send it to me~"
    "While it might have seemed that last part was a joke, she definitely meant it, Merry was about as straight as a curly fry."
    menu:
        "Wha-? Hey! Give it back!":
            jump Day1_fight_merry_for_wallet
        "Damn it...":
            jump Day1_forget_about_wallet
            

label Day1_forget_about_wallet:
    # unfinished


label Day1_fight_merry_for_wallet:
    "It takes a few seconds for the shock to wear off, but when it does, you immediately grab for your wallet."
    jes "Hey, that's mine! I need to get some things at the store today!"
    "She holds your head away with an outstreatched arm as she moves the wallet as far away from you as possible, and sticks out her tongue to tease you"
    mer "Blehhhh, No chance, dork! If you needed to buy anything important you wouldn't have tried to soften up my tits~"
    "She briefly lets go of your head, causing you to fall forwards, only to be caught in a headlock as she presses your face into the side of her tits."
    mer "You wanna be part of these, huh? Dork~?"
    mer "Is that important thing you needed to buy a new bra for me~?"
    "Holding the hand with the wallet way up in the air, far from your reach, she gasps in sarcastic surprise as she continues,"
    mer "Oh! That must be why you wanted me to churn you, huh?"
    mer "You haven't even bought the bra yet dummy~ Really put the cart before the horse on that one, huh?"
    "She shoves you back against the wall before stuffing your wallet deep into her cleavage."
    "You won't be getting that back any time soon, unless..."
    menu:
        "'You want to play that way? Fine, let's play dirty... (Dig for what's yours...)'":
            jump Day1_fight_dirty_to_get_wallet
        "'Guess it's as good of time as any to start budgeting...'":
            jump Day1_forget_about_wallet

label Day1_fight_dirty_to_get_wallet:
    jes "{i}... well, I do need to go to the store... and she did basically just imply that I was too much of a wimp to try to take it from there...{/i}"
    jes "{i}I can't exactly let her have the win here, right?{/i}"
    jes "{i}What could possibly go wrong?{/i}" 
    "Just as you think those words, all of the many {b}many{/b} ways this could go wrong race through your head."
    "As you're about to reach in and grab it, you trip."
    "Whether it was your own mistake, or something she did to you, you don't know, but the result is the same."
    "Instead of grabbing your wallet with your hands, you end up slamming your face directly into her cleavage!"
    $ Tit_Fishing_Item_Depth = 5
    call minigame_start([Jes], Mer, [False, True, False, True, False ], [False, True, False, True] )
    data jes arousal +0.5    # add 0.5 to Jessie's arousal
    "Merry could have stepped out of the way, she chose not to."
    "You fall right smack into Merry's fat rack, and before you can pull out your head, she puts her hand over it to hold it down, thus you find it difficult to retreat from her soft canyon."
    data mer arousal +0.5
    mer "Naughty boy~ Doing this to your own sister~?" 
    "She jeers, pressing your head in a little harder,"
    mer "Well if you want it back that bad, let's play bobbing for wallets, go on~"
    "She jiggles her chest a little, which only serves to sink your face in more."
    data jes arousal +0.5
    menu:
        "Commit (Search, %%chance of success)":
            random:
                jump Day1_tit_fishing_for_wallet_with_merry_success
                weight 5
                jump Day1_tit_fishing_for_wallet_with_merry_fail
        "Screw it, I'll just let her have it (Try to break free, higher %%chance of success)":
            random:
                jump Day1_escape_tit_fishing_for_wallet_with_merry_success
                weight 3
                jump Day1_escape_tit_fishing_for_wallet_with_merry_fail



label Day1_tit_fishing_for_wallet_with_merry_fail:
    "You fumble in your attempt to fish for your wallet with your mouth."
    "In response, Merry jiggles her chest, causing you to sink in even deeper."
    "She clearly is enjoying herself as she makes motorboat noises and teasing you,"
    mer "I think you nearly got it that time~ Keep it up you might just get it back~" 
    data mer arousal +0.5
    data jes arousal +1
    "The jiggling pushes the wallet up a little more into view, you can see it more clearly."
    $ Tit_Fishing_Item_Depth -= 1
    menu:
        "Commit":
            random:
                jump Day1_tit_fishing_for_wallet_with_merry_success
                weight 5
                jump Day1_tit_fishing_for_wallet_with_merry_fail
        "Go Back":
            random:
                jump Day1_escape_tit_fishing_for_wallet_with_merry_success
                weight 3
                jump Day1_escape_tit_fishing_for_wallet_with_merry_fail
        "Play With Her Tits" if Jes.arousal >= 3:
            jump Day1_tit_fishing_for_wallet_with_merry_play_with_boobs


label Day1_tit_fishing_for_wallet_with_merry_success:
    

label Day1_tit_fishing_for_wallet_with_merry_play_with_boobs:
    "Even though she's your sister, few guys could resist being turned on in a situation like this."
    "And, since she was basically asking for it at this point, you decide to let yourself have some fun."
    "Of course, you still try to get your wallet back, but with less focus."
    "You push your face slightly deeper and playfully snappe your mouth for your wallet, however, you miss, ending up with nothing but skin"
    data jes arousal +0.6
    data jes stamina -10
    data mer arousal +0.4
    "As you begin to have some fun with your sister you begin to slowly sweat a little as your growing thirst and lust begin to take hold."
    "A small shiver runs down your back and you feel some sweat forming as well…"