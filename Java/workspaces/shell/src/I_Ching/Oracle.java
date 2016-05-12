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

package I_Ching;

public class Oracle
{
// instance variables

    public int LENGTH = 2;
    private Hexagram[] hexagrams = new Hexagram[LENGTH];

// static fields

/* public */

// constructors

// instance methods

    public void newToss()
    {
        for (int i = 0; i < hexagrams.length; i += 2)
        {
            hexagrams[i]   = new Hexagram();
            hexagrams[i+1] = (Hexagram) hexagrams[i].next();
        }
    }

    public void speak()
    {
        for (int i = 0; i < LENGTH; i++)
            System.out.println(hexagrams[i]);
    }

 // getters

 // setters

// static methods

    public static void main(String[] args)
    {
        Oracle oracle = new Oracle();
        oracle.newToss();
        oracle.speak();
    }

/* private */

// constructors

// instance methods

 // getters

 // setters

// static methods

}
