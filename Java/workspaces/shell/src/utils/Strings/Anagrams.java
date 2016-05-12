/*
	This is free and unencumbered software released into the public domain.

	Anyone is free to copy, modify, publish, use, compile, sell, or
	distribute this software, either in source code form or as a compiled
	binary, for any purpose, commercial or non-commercial, and by any
	means.

	In jurisdictions that recognize copyright laws, the author or authors
	of this software dedicate any and all copyright interest in the
	software to the public domain. We make this dedication for the benefit
	of the public at large and to the detriment of our heirs and
	successors. We intend this dedication to be an overt act of
	relinquishment in perpetuity of all present and future rights to this
	software under copyright law.

	THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
	EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
	MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
	IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
	OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
	ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
	OTHER DEALINGS IN THE SOFTWARE.

	For more information, please refer to <http://unlicense.org/>
*/

package utils

class Class
{
/* public */

// instance variables

// static fields

// constructors

// instance methods

 // getters

 // setters

// static methods

    public static boolean areAnagrams(String... strings)
    {
        // less than two parameters
        if (strings.length < 2)
            return true;

        // two parameters
        else if (strings.length == 2)
        {
            String   source = stripPunctuation(strings[0]),
                   opponent = stripPunctuation(strings[1]);

            if (source.length() != opponent.length())
                return false;

            // check characters against each other
            char c;
            int opponentPosition;

            System.out.println("####################"); // DEBUG
            System.out.println(source);
            System.out.println(opponent);
            System.out.println();
            for (int sourcePosition = 0; sourcePosition < source.length(); sourcePosition++)
            {
                c = source.charAt(sourcePosition);
                opponentPosition = opponent.indexOf(c, sourcePosition);
                if (opponentPosition < 0)
                    return false;
                if (opponentPosition == sourcePosition)
                    continue;
                assert opponentPosition > sourcePosition : "internal consistency error ; "
                                                            + "opponentPosition: " + opponentPosition
                                                            + "sourcePosition: " + sourcePosition;
                opponent = swapCharacters(opponent, opponentPosition, sourcePosition);
                System.out.println(source); // DEBUG
                System.out.println(opponent);
                System.out.println();
            }

            return true;
        }

        // more than two parameters
        else
        {
            // check for parameters 0-1, 1-2, 2-3, and so on.
            for (int i = 1; i < strings.length; i++)
                if (! areAnagrams(strings[i-1], strings[i]))
                    return false;
            return true;
        }
    }

    private static String stripPunctuation(String string)
    {
        return string.toLowerCase().replaceAll("[ .,;:-]", "");
    }

    private static String swapCharacters(String aString, int index1, int index2)
    {
        char[] string = aString.toCharArray();
        char c = string[index1];
        string[index1] = string[index2];
        string[index2] = c;
        return new String(string);
    }

	public static void main(String[] args)
	{
		if (areAnagrams(args))
		    System.out.printf("anagrams!%n");
		else
		    System.out.printf("not anagrams.%n");
	}

/* private */

// instance variables

// static fields

// constructors

// instance methods

 // getters

 // setters

// static methods

}
