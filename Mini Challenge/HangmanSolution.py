# coding=utf-8
import random


def get_word( ):
    words = [
        "Andorra",
        "Afghanistan",
        "Anguilla",
        "Albania",
        "Armenia",
        "Angola",
        "Antarctica",
        "Argentina",
        "Austria",
        "Australia",
        "Aruba",
        "Azerbaijan",
        "Barbados",
        "Bangladesh",
        "Belgium",
        "Bulgaria",
        "Bahrain",
        "Burundi",
        "Benin",
        "Bermuda",
        "Brunei",
        "Bolivia",
        "Brazil",
        "Bahamas",
        "Bhutan",
        "Botswana",
        "Belarus",
        "Belize",
        "Canada",
        "Congo",
        "Switzerland",
        "Chile",
        "Cameroon",
        "China",
        "Colombia",
        "Cuba",
        "Curaçao",
        "Cyprus",
        "Czech",
        "Germany",
        "Djibouti",
        "Denmark",
        "Dominica",
        "Algeria",
        "Ecuador",
        "Estonia",
        "Egypt",
        "Eritrea",
        "Spain",
        "Ethiopia",
        "Finland",
        "Fiji",
        "France",
        "Gabon",
        "England",
        "Grenada",
        "Georgia",
        "Guernsey",
        "Ghana",
        "Gibraltar",
        "Greenland",
        "Gambia",
        "Guinea",
        "Guadeloupe",
        "Greece",
        "Guatemala",
        "Guam",
        "Guyana",
        "Hong Kong",
        "Honduras",
        "Croatia",
        "Haiti",
        "Hungary",
        "Indonesia",
        "Ireland",
        "Israel",
        "India",
        "Iraq",
        "Iran",
        "Iceland",
        "Italy",
        "Jersey",
        "Jamaica",
        "Jordan",
        "Japan",
        "Kenya",
        "Kyrgyzstan",
        "Cambodia",
        "Kiribati",
        "Comoros",
        "Korea",
        "Kuwait",
        "Kazakhstan",
        "Lebanon",
        "Liechtenstein",
        "Liberia",
        "Lesotho",
        "Lithuania",
        "Luxembourg",
        "Latvia",
        "Libya",
        "Morocco",
        "Monaco",
        "Moldova",
        "Montenegro",
        "Madagascar",
        "Marshall Islands",
        "Macedonia",
        "Mali",
        "Myanmar",
        "Mongolia",
        "Macau",
        "Martinique",
        "Mauritania",
        "Montserrat",
        "Malta",
        "Mauritius",
        "Maldives",
        "Malawi",
        "Mexico",
        "Malaysia",
        "Mozambique",
        "Namibia",
        "Niger",
        "Nigeria",
        "Nicaragua",
        "Netherlands",
        "Norway",
        "Nepal",
        "Nauru",
        "Niue",
        "Oman",
        "Panama",
        "Peru",
        "Philippines",
        "Pakistan",
        "Poland",
        "Pitcairn",
        "Palestine",
        "Portugal",
        "Palau",
        "Paraguay",
        "Qatar",
        "Réunion",
        "Romania",
        "Serbia",
        "Russia",
        "Rwanda",
        "Seychelles",
        "Sudan",
        "Sweden",
        "Singapore",
        "Slovenia",
        "Slovakia",
        "Senegal",
        "Somalia",
        "Suriname",
        "Syria",
        "Swaziland",
        "Chad",
        "Togo",
        "Thailand",
        "Tajikistan",
        "Tokelau",
        "Turkmenistan",
        "Tunisia",
        "Tonga",
        "Turkey",
        "Tuvalu",
        "Taiwan",
        "Tanzania",
        "Ukraine",
        "Uganda",
        "America",
        "Uruguay",
        "Uzbekistan",
        "Vatican",
        "Venezuela",
        "Vietnam",
        "Vanuatu",
        "Samoa",
        "Yemen",
        "Mayotte",
        "Zambia",
        "Zimbabwe",
    ]
    return random.choice( words ).upper( )


def check( word, guesses, guess ):
    upper = guess.upper( )
    guess = upper
    status = ''
    i = 0
    matches = 0
    for letter in word:
        if letter in guesses:
            status += letter
        else:
            status += '*'

        if letter == guess:
            matches += 1

    if matches > 1:
        print( 'Yes! The word contains', matches, '"' + guess + '"' + 's' )
    elif matches == 1:
        print( 'Yes! The word contains the letter "' + guess + '"' )
    else:
        print( 'Sorry. The word does not contain the letter "' + guess + '"' )

    return status


def main( ):
    word = get_word( )
    # print(word)
    guessesSoFar = [ ]
    correctlyGuess = False
    print( 'The word contains', len( word ), 'letters.' )
    while not correctlyGuess:
        text = 'Please enter one letter or a {}-letter word. '.format( len( word ) )
        userGuessInput = input( text )
        userGuessInput = userGuessInput.upper( )
        if userGuessInput in guessesSoFar:
            print( 'You already correctlyGuess "' + userGuessInput + '"' )
        elif len( userGuessInput ) == len( word ):
            guessesSoFar.append( userGuessInput )
            if userGuessInput == word:
                correctlyGuess = True
            else:
                print( 'Sorry, that is incorrect. ' )
        elif len( userGuessInput ) == 1:
            guessesSoFar.append( userGuessInput )
            result = check( word, guessesSoFar, userGuessInput )
            if result == word:
                correctlyGuess = True
            else:
                print( result )
        else:
            print( 'Invalid entry.' )
    print( 'Yes, the word is', word + '! You got it in', len( guessesSoFar ), 'tries.' )


main( )
