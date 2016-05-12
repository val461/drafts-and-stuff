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

public enum Trigrams
{
    EARTH       (0, "earth"),
    MOUNTAIN    (1, "mountain"),
    CANYON      (2, "water"),
    WIND        (3, "wind"),
    THUNDER     (4, "thunder"),
    FIRE        (5, "fire"),
    LAKE        (6, "lake"),
    SKY         (7, "heaven");

    private static final int length = values().length;

    private final int id;
    private final String name;


    Trigrams(int id, String name)
    {
        this.id = id;
        this.name = name;
    }

    public static Trigrams withId(int id)
    {
        return (0 <= id && id < length) ? values()[id] : null;
    }

    public static void main(String[] args)
    {
        System.out.println(Trigrams.withId(2));
    }

    public int     id()          { return id;                   }
    public String  toString()    { return name;                 }
}
